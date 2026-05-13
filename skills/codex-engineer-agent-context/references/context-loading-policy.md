# Context Loading Policy

Use this policy to decide what Codex should read before acting and what should stay out of active context.

## Loading Layers

- Layer 0: System and platform instructions.
- Layer 1: Global user Codex rules.
- Layer 2: Repo-level `AGENTS.md`.
- Layer 3: Directory-specific `AGENTS.md` or override instructions.
- Layer 4: Skill metadata: `name`, `description`, and path.
- Layer 5: Full `SKILL.md` after explicit or allowed implicit trigger.
- Layer 6: Selected references from the skill reference guide.
- Layer 7: Raw sources, logs, traces, screenshots, generated artifacts, and code slices.
- Layer 8: Scratchpads, session summaries, context maps, and recovery notes.

Prefer lower-numbered layers only for small, stable, high-priority rules. Push bulky, volatile, or task-specific material into later layers with restorable pointers.

## Load First

- The user's current request and any newer corrections.
- The nearest `AGENTS.md` files that govern the working directory.
- The specific files being edited or reviewed.
- The smallest source slice that proves the claim or supports the patch.
- Existing task summaries, context maps, or recovery notes when resuming work.

## Load On Demand

- Long logs: search with `rg`, then read only relevant sections.
- Large specs: read the table of contents, section headings, or source map first.
- Prior attempts: load when debugging repeated failures or validating rollback notes.
- Related skills: load only when the task triggers them, then follow their own reference map.
- Historical decisions: load when they affect current behavior, compatibility, or constraints.
- Shared patterns: load only the directly linked pattern card, not the whole shared library.

## Avoid Loading

- Entire generated outputs when a path and checksum or summary is enough.
- Full dependency trees, build artifacts, lockfile diffs, or vendored code unless directly relevant.
- Old chat history that is superseded by a newer summary.
- Broad web or repository searches after the relevant local source has been identified.
- Domain knowledge unrelated to agent context governance, even if it appears in a nearby shared reference.

## Reread Rules

Reread source material before:

- Making a concrete claim about a file, policy, API, or user instruction.
- Editing after a long interruption or context compaction.
- Merging subagent output into files you also touched.
- Updating persistent memory or repo-level policy.
- Closing a task that involved failures, rollbacks, or partial verification.

## Loading Budget

For each task, state the loading boundary in plain terms:

- Must read: sources needed to act safely.
- May read: sources useful if uncertainty remains.
- Should not read: sources likely to add noise or stale detail.

## Placement Test

Before adding context to an always-loaded file, ask:

- Is it stable across many tasks?
- Does it affect agent behavior before any task-specific trigger?
- Is it short enough to preserve attention?
- Would a path to a reference file work just as well?

If the answer is no, place it in a skill, reference, scratchpad, session summary, or archive instead.
