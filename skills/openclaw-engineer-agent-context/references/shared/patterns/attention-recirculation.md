# Pattern: Attention Recirculation

## Applicable Situation

Use for long multi-step tasks where the agent may drift from the original goal.

## Inputs

- Current goal
- Plan or checklist
- Recent observations
- Remaining risks

## Default Workflow

1. Maintain a compact checklist or working state.
2. Update status after meaningful progress.
3. Re-state the active goal before choosing the next major action.
4. Keep unresolved constraints visible near the current step.
5. Remove completed detail from active context only when it is recorded elsewhere.

## Branch Rules

- For coding tasks, use a plan checklist only when the task is non-trivial.
- For research tasks, keep a source log and a current hypothesis.
- For high-risk tasks, keep the acceptance criteria in the current context until final verification.

## Anti-Patterns

- Letting old observations push the task into a different objective.
- Updating the plan only at the end.
- Keeping a long todo list that no longer reflects reality.

## Acceptance Criteria

- The next action is connected to the current goal.
- The checklist reflects actual state.
- Final handoff explains what was verified.

## Conflict Notes

Some simple tasks do not need formal planning. Use attention recirculation when drift risk exceeds planning overhead.

## Evidence Level

B
