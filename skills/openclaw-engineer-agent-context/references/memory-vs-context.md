# Memory vs Context

Use memory for durable project facts and preferences. Use active context for the current task state.

## Persistent Memory

Store only information likely to remain useful across future tasks:

- Project conventions that are not already obvious from files.
- User preferences that repeatedly affect implementation choices.
- Durable decisions, constraints, or integration facts.
- Stable warnings about dangerous commands, environments, or deployment paths.

Do not store temporary facts, one-off bug details, raw logs, or guesses.

## Active Context

Keep this visible while working:

- Current user goal.
- Latest user corrections.
- Relevant constraints and acceptance criteria.
- Current plan and next action.
- Recently observed evidence.
- Open risks and blockers.
- Recovery pointers for omitted long material.

## File-Backed Task State

Use files for material too large or too volatile for active context:

- Session summaries.
- Context maps.
- Run logs and test output.
- Audit reports.
- Source maps for long docs.
- Rollback notes for risky migrations.

## Update Rules

- Update memory only after confirming the fact is stable and useful beyond this task.
- Update active context after material changes in goal, plan, evidence, or risk.
- Update file-backed summaries before compaction, handoff, or pausing a long task.
- Remove stale active context once it is superseded and recoverable elsewhere.
