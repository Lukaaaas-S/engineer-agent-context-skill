# Context Principles

Use these principles when designing repository-level agent instructions, context-related skills, summaries, and long-running agent workflows.

This skill governs four moves: Write, Select, Compress, and Isolate.

## Write

Save important intermediate state outside the context window.

Use for:

- Task plans that must survive interruption.
- Decisions, constraints, and acceptance criteria.
- Recovery notes and rollback points.
- Failed attempts that prevent repeated loops.
- Durable project preferences that are not already obvious from source files.

Do not write:

- Temporary guesses.
- Raw logs that are reproducible and have no diagnostic value.
- Sensitive material unless the repository policy explicitly allows it.
- Generated summaries without pointers back to source-of-truth files.

## Select

Load only the relevant slice for the current task.

Use:

- Source maps and reference guides before reading long documents.
- File paths, anchors, command names, trace IDs, and URLs as recovery pointers.
- Explicit loading budgets: must read, may read, should not read.
- Reread rules before making concrete claims, editing stale files, or closing risky tasks.

Avoid:

- Pasting whole reference libraries into active context.
- Loading broad chat history after a newer session summary supersedes it.
- Letting old observations remain active after code, goals, or constraints changed.

## Compress

Summarize long-running work into decision-grade state.

Keep:

- Current user goal and latest correction.
- Non-negotiable constraints.
- Current plan and completed steps.
- Files changed or inspected.
- Decisions made.
- Failed attempts and why they matter.
- Evidence paths.
- Open risks, blockers, and next safe action.

Drop only when explicitly safe:

- Duplicate observations confirmed by newer evidence.
- Dead-end hypotheses that do not affect future choices.
- Low-value tool output that is reproducible and not needed for diagnosis.

## Isolate

Move noisy exploration out of the main context when it would pollute the current task.

Use scratchpads, source maps, or subagents when:

- The search space is large.
- Work can be split into independent read or write scopes.
- Exploration may produce many false starts.
- A risky branch should not crowd out the current goal.

Do not isolate by default. A single main agent is preferred for ordinary context design, `AGENTS.md` edits, context-related `SKILL.md` edits, and session-summary work.

## Repository Artifacts

- `AGENTS.md`: concise trigger rules and a few hard constraints.
- `SKILL.md`: task-specific context workflow and reference map.
- Reference files: detailed policies, examples, maps, and reusable guidance.
- Memory files: durable preferences, project facts, and decisions that should survive across tasks.
- Scratchpads: temporary execution notes that can be archived or deleted after summary.
- Session summaries: task-local checkpoints for compaction, handoff, or recovery.

## Practical Test

A context policy is working when a fresh Codex instance can:

- Understand the current goal without rereading the whole thread.
- Find the relevant long sources without pasted bulk.
- Avoid known failed paths.
- Recover after compaction.
- Decide what to load next before editing code.
