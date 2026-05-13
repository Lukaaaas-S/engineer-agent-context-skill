# Pattern: Stable Prefix Cache

## Applicable Situation

Use when designing prompts or runtime context for long-running agents where latency, cost, and consistency matter.

## Inputs

- System/developer instructions
- Tool schemas
- Runtime metadata
- Repeated task loop

## Default Workflow

1. Keep stable instructions at the beginning of the context.
2. Avoid inserting volatile values into the early prompt prefix.
3. Keep tool schemas stable during the session.
4. Append new observations instead of rewriting history.
5. Use explicit cache breakpoints only when the runtime supports them.

## Branch Rules

- If exact current time is needed, put it in a late task-local section.
- If tools must be restricted, mask availability rather than rewriting tool definitions when possible.
- If history is too large, compress into a restorable reference rather than deleting evidence blindly.

## Anti-Patterns

- Putting changing timestamps at the top of the prompt.
- Reordering JSON keys or tool definitions between turns without need.
- Editing old observations in place.

## Acceptance Criteria

- Stable prefix content changes rarely.
- Volatile task data is isolated.
- Context changes are append-only unless there is a deliberate reset.

## Conflict Notes

This pattern matters most for productized agent runtimes. For one-off Codex tasks, apply the principle lightly: keep instructions stable and put volatile details near the current task.

## Evidence Level

B
