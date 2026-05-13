# Context Principles

Use these principles when designing repository-level agent instructions, context-related skills, summaries, and long-running agent workflows.

## Core Rules

- Keep active context small enough to steer the next action.
- Make context restorable through paths, IDs, URLs, command names, or source titles.
- Separate stable policy from volatile task state.
- Put bulky material in files and load it only when needed.
- Keep the current goal, constraints, open risks, and latest evidence visible during long tasks.
- Preserve failed attempts when they prevent repeated loops.
- Prefer explicit refresh points over hoping the agent remembers old details.

## Repository Artifacts

- `AGENTS.md`: concise repo policy, trigger rules, commands, ownership boundaries, and safety notes.
- `SKILL.md`: context-related workflow and references; do not use it as a dumping ground.
- Reference files: detailed policies, examples, maps, and reusable guidance.
- Memory files: durable preferences, project facts, and decisions that should survive across tasks.
- Session summaries: task-local checkpoints for compaction, handoff, or recovery.

## Anti-Patterns

- Copying full reference material into `AGENTS.md`.
- Mixing temporary task notes into persistent memory.
- Summarizing logs without preserving enough source pointers to verify them later.
- Giving every subagent the whole conversation by default.
- Treating context compression as cleanup instead of a recovery design problem.
- Letting old observations remain active after the code or plan has changed.

## Practical Test

A context policy is working when a fresh Codex instance can:

- Understand the current goal without rereading the whole thread.
- Find the relevant long sources without pasted bulk.
- Avoid known failed paths.
- Recover after compaction.
- Decide what to load next before editing code.
