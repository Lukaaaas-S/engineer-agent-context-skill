---
name: codex-engineer-agent-context
description: "Design or audit context management for Codex and coding-agent workflows: AGENTS.md trigger rules, context-related SKILL.md files, file-backed memory, session summaries, context loading, retrieval/reference selection, compression, handoff, recovery, rollback notes, and subagent isolation. Use only when agent context management is the main task. Do not use for ordinary coding, content writing, product strategy, or generic AI discussion."
---

# Codex Engineer Agent Context

Use this skill to make agent context management practical, restorable, and small enough for Codex to act on. This is a context-governance skill, not a general coding helper or knowledge base.

## Purpose

Design, audit, and improve the context architecture around long-running Codex or coding-agent work.

This skill separates:

- Always-loaded instructions.
- Task-triggered skill instructions.
- Selected references.
- File-backed memory and scratchpads.
- Session summaries and handoff notes.
- Raw logs, traces, source files, and generated artifacts.

## Trigger Boundary

Use this skill for:

- `AGENTS.md`, context-related `SKILL.md`, `CLAUDE.md`, `GEMINI.md`, or similar instruction files.
- Context loading, retrieval, reference selection, or source-map policy.
- File-backed memory, scratchpads, session summaries, and long-task state.
- Context compression, task handoff, recovery notes, and rollback notes.
- Multi-agent or subagent context isolation.
- Context bloat, stale instruction, or conflicting-rule audits.

Do not use this skill for:

- Ordinary feature implementation or bug fixes.
- Generic skill authoring unless the skill controls agent context or memory.
- Product, business, market, search, or content strategy unless the output is an agent-facing context policy.
- Summarizing sources without an operational context-management goal.

## Core Principles

- Treat context as task state, not storage.
- Keep `AGENTS.md` short and trigger-oriented.
- Put task-specific workflow in `SKILL.md`.
- Put bulky facts, logs, traces, examples, and source excerpts in referenced files.
- Keep active context limited to the goal, constraints, current plan, latest evidence, open risks, and recovery pointers.
- Separate memory that should persist across runs from context needed only for the current turn.
- Never treat generated summaries as source of truth when original sources remain available.

## Workflow

1. Classify the task mode:
   - Context architecture design.
   - Context audit.
   - Skill or `AGENTS.md` design.
   - Long-task memory design.
   - Compression or handoff policy design.
   - Subagent isolation design.
2. Inventory context sources:
   - System, platform, user, repo, and directory instructions.
   - Skill files, references, templates, and source maps.
   - Project docs, source code, logs, traces, screenshots, and generated artifacts.
   - Memory files, scratchpads, session summaries, previous handoffs, and user preferences.
3. Classify each source:
   - Stable rule.
   - Project fact.
   - Volatile task data.
   - Generated summary.
   - Raw evidence.
   - Execution artifact.
   - Sensitive or restricted material.
4. Decide placement:
   - Always-loaded: small, stable, high-priority rules.
   - Skill-loaded: task-specific workflow rules.
   - Reference-loaded: deeper guidance read only when needed.
   - Retrieved: dynamically searched or selected source slices.
   - Scratchpad: temporary execution notes.
   - Session summary: compressed task continuity.
   - Archive: traceable but not loaded by default.
5. Define the context policy:
   - What should Codex read before starting?
   - What should Codex read only after the skill triggers?
   - What should be referenced by path instead of copied?
   - What should be summarized, preserved raw, or excluded from default loading?
   - What must be updated before compaction, handoff, or pause?
6. Add recovery and isolation rules:
   - Preserve goal, constraints, completed work, changed files, decisions, failed attempts, evidence paths, current risks, next safe action, and rollback point.
   - Do not recommend subagents by default; use them only for context isolation, parallel exploration, or large codebase/file exploration.
7. Produce a concrete artifact:
   - Context architecture proposal.
   - Context audit report.
   - `AGENTS.md` trigger block.
   - `SKILL.md` draft or patch.
   - Session-summary template.
   - Context map.
   - Migration or cleanup plan.

## Reference Guide

Read only the reference needed for the current job:

- `references/context-principles.md`: Write, Select, Compress, and Isolate principles.
- `references/context-loading-policy.md`: loading layers, reread rules, and loading budgets.
- `references/compression-policy.md`: safe compression and long-task summary rules.
- `references/memory-vs-context.md`: persistent memory versus active context window separation.
- `references/subagent-isolation-policy.md`: delegation, isolation, and result-merging rules.
- `references/source-map.md`: provenance and deeper pattern cards.

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
- Reject broad always-loaded knowledge that is not needed for the current context-governance task.

## Output Shape

When designing or auditing context systems, include:

- Active context: what must stay visible now.
- External references: file paths, URLs, trace IDs, or source names.
- Memory boundary: what persists beyond this task and why.
- Compression rule: what can be summarized and how to recover it.
- Refresh cadence: when the agent updates plans, summaries, and source reads.
- Subagent rule: what is isolated, shared, and merged.
- Risks: bloat, drift, stale source claims, lost failures, or over-broad memory.
