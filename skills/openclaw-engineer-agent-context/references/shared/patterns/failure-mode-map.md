# Pattern: Failure Mode Map

## Applicable Situation

Use when designing an agent for workflows where failure recovery matters as much as happy-path completion.

## Inputs

- Goal
- Tool loop
- Known constraints
- Likely failure classes

## Default Workflow

1. List failure modes before writing the main workflow.
2. Map each failure to detection evidence.
3. Define recovery behavior: retry, search alternative, ask, stop, or escalate.
4. Keep failed attempts visible when they teach the next action.
5. Verify the final result against both success and failure criteria.

## Branch Rules

- If a failure is caused by missing information, ask or inspect.
- If a failure is caused by tool state, retry only after changing a variable.
- If repeated failures produce no new evidence, stop and report.

## Anti-Patterns

- Retrying the same call without changing inputs.
- Erasing failure traces from the working context.
- Reporting success because the agent produced output.

## Acceptance Criteria

- Every major failure has a detection signal.
- The agent knows when to stop.
- The handoff includes unresolved risks.

## Conflict Notes

Some clean-context advice conflicts with retaining failed attempts. Retain concise failure evidence when it prevents repeated mistakes; externalize verbose logs to files.

## Evidence Level

B
