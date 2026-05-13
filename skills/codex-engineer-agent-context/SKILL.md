---
name: codex-engineer-agent-context
description: "Engineer context systems for Codex repository work. Use when Codex needs to design, audit, or improve agent-facing context artifacts: AGENTS.md trigger rules, context-related SKILL.md files, agent memory files, context loading policies, session summaries, context compression, subagent context isolation, coding-agent coordination, long-task recovery notes, rollback notes, or context bloat controls. Do not use for ordinary feature work, bug fixes, or general skill authoring unless the artifact controls agent context, memory, loading, compression, or recovery."
---

# Codex Engineer Agent Context

Use this skill to make agent context management practical, restorable, and small enough for Codex to act on. Focus on repository artifacts that control agent context, not generic AI theory or ordinary coding workflow.

## Operating Frame

- Treat context as task state, not storage.
- Put stable context policy in `AGENTS.md`, context-related `SKILL.md` files, or explicit reference files.
- Put bulky facts, logs, traces, source excerpts, and run history in files with paths.
- Keep active context limited to the goal, constraints, current plan, latest evidence, open risks, and recovery pointers.
- Separate memory that should persist across runs from context needed only for the current turn.

## Workflow

1. Identify the context artifact being designed or reviewed: `AGENTS.md` trigger rule, context-related `SKILL.md`, memory file, summary, subagent prompt, context policy, or recovery note.
2. Map stable instructions, volatile task facts, external references, tool observations, and failure evidence.
3. Decide what stays active, what moves to files, and what can be dropped only after a restorable pointer exists.
4. Add refresh rules for long tasks: when to restate the goal, reread source files, update plans, and summarize progress.
5. Define compression rules: what is preserved verbatim, summarized, linked by path, or intentionally discarded.
6. Check subagent boundaries: what each subagent receives, owns, edits, reports back, and must not inherit.
7. Produce a concrete patch, policy, or audit report with file paths and next actions.

## Reference Guide

Read only the reference needed for the current job:

- `references/context-principles.md`: baseline rules for stable, restorable context systems.
- `references/context-loading-policy.md`: what to load, when to reread, and how to avoid bloat.
- `references/compression-policy.md`: safe compression and long-task summary rules.
- `references/memory-vs-context.md`: persistent memory versus active context window separation.
- `references/subagent-isolation-policy.md`: delegation, isolation, and result-merging rules.

## Templates

Use the templates when producing durable artifacts:

- `templates/context-map.template.md`: map active context, external references, and risks.
- `templates/session-summary.template.md`: checkpoint long tasks or recover after compaction.
- `templates/context-audit-report.template.md`: review context bloat, drift, and recovery gaps.

## Review Checklist

- Keep `AGENTS.md` short and trigger-oriented; move detailed policy into skills or references.
- Keep context-related `SKILL.md` files procedural; move long examples and deep policy into one-hop references.
- Make every compression restorable unless the loss is explicit and acceptable.
- Preserve failure evidence when it prevents repeated mistakes.
- Record rollback and recovery notes close to the files or workflow they protect.
- Give subagents the minimum context needed for their owned task and ask for concise handoff output.
- Prefer paths, IDs, and command names over pasted logs when the source is recoverable.

## Output Shape

When designing or auditing context systems, include:

- Active context: what must stay visible now.
- External references: file paths, URLs, trace IDs, or source names.
- Memory boundary: what persists beyond this task and why.
- Compression rule: what can be summarized and how to recover it.
- Refresh cadence: when the agent updates plans, summaries, and source reads.
- Subagent rule: what is isolated, shared, and merged.
- Risks: bloat, drift, stale source claims, lost failures, or over-broad memory.
