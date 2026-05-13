# Publishing Checklist

- [ ] `skills/codex-engineer-agent-context/SKILL.md` validates.
- [ ] `scripts/check_reference_paths.py` passes.
- [ ] `scripts/audit_context_files.py` passes or only reports accepted warnings.
- [ ] `policy.allow_implicit_invocation` is `false`.
- [ ] No absolute local paths remain.
- [ ] No private company information remains.
- [ ] No API keys, tokens, emails, credentials, or secrets remain.
- [ ] No backup folders or generated state files are committed.
- [ ] Reference and template paths resolve from `SKILL.md`.
- [ ] README explains that cloning does not install the skill.
- [ ] README warns about same-name conflicts.
- [ ] README includes a concise `AGENTS.md` trigger block.
- [ ] README examples use `codex-engineer-agent-context`.
- [ ] Changelog describes the release.

## Commands

```bash
SKILL_CREATOR_DIR="${SKILL_CREATOR_DIR:-$HOME/.codex/skills/.system/skill-creator}"
PYTHONPATH="${PYTHONPATH:-/tmp/codex-skill-validate-pyyaml}" \
python3 "$SKILL_CREATOR_DIR/scripts/quick_validate.py" skills/codex-engineer-agent-context

python3 skills/codex-engineer-agent-context/scripts/check_reference_paths.py \
skills/codex-engineer-agent-context

python3 skills/codex-engineer-agent-context/scripts/audit_context_files.py .

python3 -m py_compile \
skills/codex-engineer-agent-context/scripts/check_reference_paths.py \
skills/codex-engineer-agent-context/scripts/audit_context_files.py
```
