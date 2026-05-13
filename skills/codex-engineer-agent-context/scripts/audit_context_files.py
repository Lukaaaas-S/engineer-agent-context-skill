#!/usr/bin/env python3
"""Audit agent-context files for bloat, drift, and obvious leaks.

This is a conservative mechanical check. It does not replace human review, but
it catches the common mistakes that make context-governance skills hard to
publish safely: oversized always-loaded files, broken skill paths, old names,
local absolute paths, and credential-shaped strings.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".txt", ".py"}
CONTEXT_FILENAMES = {
    "AGENTS.md",
    "AGENTS.override.md",
    "SKILL.md",
    "CLAUDE.md",
    "GEMINI.md",
}
CONTEXT_NAME_RE = re.compile(
    r"(context[-_ ]?map|session[-_ ]?summary|scratchpad|memory|handoff|rollback)",
    re.IGNORECASE,
)
PATH_PATTERN = re.compile(
    r"(?:`|\(|\"|')"
    r"(?P<path>(?:\./)?(?:references|templates|scripts|assets|agents)/"
    r"[A-Za-z0-9._/\-]+)"
    r"(?:`|\)|\"|')"
)
SECRET_PATTERNS = [
    re.compile("OPENAI" + "_" + "API" + "_" + "KEY"),
    re.compile("api" + r"[_-]?key\s*=", re.IGNORECASE),
    re.compile("tok" + r"en\s*=", re.IGNORECASE),
    re.compile("sec" + r"ret\s*=", re.IGNORECASE),
    re.compile("pass" + r"word\s*=", re.IGNORECASE),
    re.compile("cred" + r"ential\s*=", re.IGNORECASE),
]
LOCAL_PATH_PATTERN = re.compile(r"/Us" + r"ers/[A-Za-z0-9._-]+")
OLD_NAME_PATTERN = re.compile(
    "Open" + "Claw|"
    "open" + "claw|"
    r"\$" + "open" + "claw|"
    "skills/" + "open" + "claw|"
    r"name:\s*" + "open" + "claw|"
    r"name:\s*" + "engineer" + "-agent-context|"
    r"\$" + "engineer" + r"-agent-context\b"
)


@dataclass
class Finding:
    severity: str
    path: Path
    message: str


def iter_text_files(root: Path) -> list[Path]:
    ignored_parts = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        "node_modules",
        "dist",
        "build",
    }
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ignored_parts.intersection(path.parts):
            continue
        if path.suffix in TEXT_EXTENSIONS:
            files.append(path)
    return sorted(files)


def is_context_file(path: Path) -> bool:
    return path.name in CONTEXT_FILENAMES or bool(CONTEXT_NAME_RE.search(path.name))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def scan_text(path: Path) -> str:
    text = read_text(path)
    if path.name != "audit_context_files.py":
        return text

    filtered_lines = []
    for line in text.splitlines():
        if any(
            marker in line
            for marker in (
                "SECRET_PATTERNS",
                "LOCAL_PATH_PATTERN",
                "OLD_NAME_PATTERN",
                "OPENAI",
                "api",
                "tok",
                "sec",
                "pass",
                "cred",
                "/Us",
                "Open",
                "engineer",
            )
        ):
            continue
        filtered_lines.append(line)
    return "\n".join(filtered_lines)


def normalize_reference(raw: str) -> str:
    return raw[2:] if raw.startswith("./") else raw


def skill_dir_for(path: Path, root: Path) -> Path | None:
    parts = path.relative_to(root).parts
    if len(parts) >= 3 and parts[0] in {".agents", "skills"}:
        if parts[0] == "skills":
            return root / parts[0] / parts[1]
        if parts[0] == ".agents" and parts[1] == "skills" and len(parts) >= 4:
            return root / parts[0] / parts[1] / parts[2]
    return None


def audit(root: Path, max_instruction_bytes: int) -> list[Finding]:
    findings: list[Finding] = []
    text_files = iter_text_files(root)
    context_files = [path for path in text_files if is_context_file(path)]
    agents_files = [path for path in context_files if path.name in {"AGENTS.md", "AGENTS.override.md"}]

    if len(agents_files) > 1:
        findings.append(
            Finding(
                "INFO",
                root,
                f"Multiple AGENTS instruction files found: {len(agents_files)}. Check merge order and overrides.",
            )
        )

    for path in context_files:
        size = path.stat().st_size
        if size > max_instruction_bytes:
            findings.append(
                Finding(
                    "WARN",
                    path,
                    f"Context file is {size} bytes, above {max_instruction_bytes}. Move detail into references.",
                )
            )

    for path in text_files:
        text = scan_text(path)
        rel = path.relative_to(root)

        if LOCAL_PATH_PATTERN.search(text):
            findings.append(Finding("ERROR", path, "Contains a local absolute /Users/... path."))

        if OLD_NAME_PATTERN.search(text):
            findings.append(Finding("ERROR", path, "Contains an old or private skill name."))

        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(Finding("ERROR", path, f"Matches sensitive pattern: {pattern.pattern}"))

        if path.name == "SKILL.md":
            if "name:" not in text or "description:" not in text:
                findings.append(Finding("ERROR", path, "SKILL.md is missing name or description metadata."))

        skill_dir = skill_dir_for(path, root)
        if skill_dir is not None:
            if path.suffix in {".md", ".yaml", ".yml", ".txt"}:
                for match in PATH_PATTERN.finditer(text):
                    ref = normalize_reference(match.group("path"))
                    if not (skill_dir / ref).exists():
                        findings.append(Finding("ERROR", path, f"Broken skill-relative path: {ref}"))

        if ".backup" in str(rel) or rel.name.endswith((".bak", ".tmp")):
            findings.append(Finding("WARN", path, "Looks like backup or generated state committed."))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="Repository root to audit",
    )
    parser.add_argument(
        "--max-instruction-bytes",
        type=int,
        default=32 * 1024,
        help="Warn when context files exceed this size",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        return 2

    findings = audit(root, args.max_instruction_bytes)
    if not findings:
        print("Context audit passed: no findings.")
        return 0

    print("Context audit findings:")
    for finding in findings:
        if finding.path == root:
            label = "."
        else:
            label = str(finding.path.relative_to(root))
        print(f"- [{finding.severity}] {label}: {finding.message}")

    return 1 if any(f.severity == "ERROR" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
