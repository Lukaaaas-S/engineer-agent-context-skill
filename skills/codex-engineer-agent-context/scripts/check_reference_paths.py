#!/usr/bin/env python3
"""Validate paths referenced by a Codex skill.

By default this script checks the skill directory that contains it:

    python3 scripts/check_reference_paths.py

It scans Markdown, YAML, and text files for skill-relative paths such as
reference files, templates, scripts, assets, and agent metadata.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATH_PATTERN = re.compile(
    r"(?:`|\(|\"|')"
    r"(?P<path>(?:\./)?(?:references|templates|scripts|assets|agents)/"
    r"[A-Za-z0-9._/\-]+)"
    r"(?:`|\)|\"|')"
)

TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".txt"}


def default_skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def iter_text_files(skill_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in skill_dir.rglob("*")
        if path.is_file()
        and path.suffix in TEXT_EXTENSIONS
        and "__pycache__" not in path.parts
    )


def referenced_paths(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [match.group("path") for match in PATH_PATTERN.finditer(text)]


def normalize_reference(raw: str) -> str:
    return raw[2:] if raw.startswith("./") else raw


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "skill_dir",
        nargs="?",
        type=Path,
        default=default_skill_dir(),
        help="Skill directory containing SKILL.md",
    )
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        print(f"ERROR: {skill_dir} does not contain SKILL.md", file=sys.stderr)
        return 2

    missing: list[tuple[Path, str]] = []
    checked: list[tuple[Path, str]] = []

    for source in iter_text_files(skill_dir):
        for raw in referenced_paths(source):
            rel = normalize_reference(raw)
            checked.append((source, rel))
            if not (skill_dir / rel).exists():
                missing.append((source, rel))

    if missing:
        print("Broken skill reference paths:")
        for source, rel in missing:
            print(f"- {source.relative_to(skill_dir)} -> {rel}")
        return 1

    print(f"Reference paths valid: {len(checked)} checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
