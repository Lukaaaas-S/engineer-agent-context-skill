# Codex Engineer Agent Context Skill

Cloning this repository does not install the skill. To activate it, copy the skill folder into a Codex-recognized skills directory.

This repository packages a Codex skill for designing and auditing context management policies for coding agents, long-running agent workflows, subagents, memory files, session summaries, compression, and recovery design.

The design goal is narrow trigger, strong workflow, light always-loaded context, and heavier on-demand references:

```text
AGENTS.md = trigger rules
SKILL.md = workflow
references = deeper policy
templates = output shapes
scripts = mechanical checks
task files = project-specific state
```

## Skill Name

`codex-engineer-agent-context`

Use it explicitly:

```text
Use $codex-engineer-agent-context.
Audit this agent workflow context policy and propose concrete fixes.
```

## Safety

This skill is an instruction and reference package for Codex. It does not connect to external services, read user data, create automations, send messages, label, archive, or delete anything by itself.

Implicit invocation is disabled by default:

```yaml
policy:
  allow_implicit_invocation: false
```

## Install Globally

Recommended official user-scope path:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/codex-engineer-agent-context "$HOME/.agents/skills/"
```

Restart Codex if the skill does not appear.

## Install Into One Repository

```bash
mkdir -p .agents/skills
cp -R skills/codex-engineer-agent-context .agents/skills/
```

This only affects that repository.

## Compatibility Note

Some Codex setups may still recognize `~/.codex/skills` for user-local skills. If your installation already uses that path, you can copy the skill there instead:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skills/codex-engineer-agent-context "$HOME/.codex/skills/"
```

## Existing Skill Conflicts

If you already have a skill with the same `name`, Codex will not merge them. Both may appear in the skill selector. Rename or disable one if needed.

This public package uses `codex-engineer-agent-context` to reduce conflict risk with local skills named `engineer-agent-context`.

## Recommended AGENTS.md Trigger

Keep repository instructions short. Put only the trigger rule in `AGENTS.md`; leave the workflow and deeper policy inside the skill.

```md
# Agent Context Management Rules

## Mandatory Skill Usage

Use `$codex-engineer-agent-context` before making or reviewing changes that affect:

- Codex, agent, or subagent context loading
- `AGENTS.md`, context-related `SKILL.md`, `CLAUDE.md`, `GEMINI.md`, or similar instruction files
- file-backed memory, scratchpads, session summaries, or long-task state
- retrieval, reference selection, or source-map policies
- context compression, task handoff, recovery, or rollback design
- multi-agent or subagent context isolation

Do not use this skill for ordinary code edits, copywriting, or product content tasks unless the request explicitly involves agent context management.
```

## What This Skill Is For

- `AGENTS.md` design
- Context-related `SKILL.md` design
- Context loading policies
- Memory versus context-window separation
- Session summaries
- Context compression
- Subagent isolation
- Recovery and rollback notes
- Context bloat audits

## What This Skill Is Not For

- Ordinary coding tasks
- Generic AI theory
- Connecting to Gmail, Slack, or other external services
- Sending, deleting, labeling, or modifying user data

## Example Uses

Audit a repository's context design:

```text
Use $codex-engineer-agent-context.

Audit this repository's AGENTS.md and .agents/skills design.
Tell me what should be always-loaded, skill-loaded, reference-loaded, or removed.
Output a context-map.md and a concise AGENTS.md trigger block.
```

Design a new skill's context architecture:

```text
Use $codex-engineer-agent-context.

I want to create a Codex skill for editing a specific codebase.
Design the context architecture:
- what belongs in AGENTS.md
- what belongs in SKILL.md
- what belongs in references
- what should be loaded only when editing code
- what should never be loaded by default
```

Create a long-task recovery summary:

```text
Use $codex-engineer-agent-context.

Create a session summary for this long Codex task.
Preserve decisions, modified files, pending steps, failed attempts, and the next safe action.
Do not include low-value logs.
```

Diagnose context bloat:

```text
Use $codex-engineer-agent-context.

Codex is getting confused in this repo.
Audit context bloat and conflicting instructions.
Find duplicated rules, stale project facts, oversized references, and unsafe always-loaded content.
Recommend a cleanup plan.
```

## Validate

If you have the Codex skill-creator validator available:

```bash
SKILL_CREATOR_DIR="${SKILL_CREATOR_DIR:-$HOME/.codex/skills/.system/skill-creator}"
PYTHONPATH="${PYTHONPATH:-/tmp/codex-skill-validate-pyyaml}" \
python3 "$SKILL_CREATOR_DIR/scripts/quick_validate.py" skills/codex-engineer-agent-context

python3 skills/codex-engineer-agent-context/scripts/check_reference_paths.py \
skills/codex-engineer-agent-context

python3 skills/codex-engineer-agent-context/scripts/audit_context_files.py .
```
