# Codex Engineer Agent Context Skill

Cloning this repository does not install the skill. To activate it, copy the skill folder into a Codex-recognized skills directory.

This repository packages a Codex skill for designing and auditing context management policies for coding agents, long-running agent workflows, subagents, memory files, session summaries, compression, and recovery design.

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

## Validate

If you have the Codex skill-creator validator available:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/codex-engineer-agent-context
```
