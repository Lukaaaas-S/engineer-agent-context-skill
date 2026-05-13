# Agent Context Boundary

This skill owns the context architecture around AI agent work: what instructions load, when deeper references are selected, how task state is preserved, and how noisy exploration is isolated.

## This Skill Owns

- Agent-facing context policies.
- `AGENTS.md` trigger rules for context-management work.
- Context-related `SKILL.md` workflows and reference maps.
- File-backed memory, scratchpads, session summaries, and handoff policy.
- Compression, recovery, rollback, and failure-evidence rules.
- Subagent context isolation and result-merging boundaries.

## This Skill Does Not Own

- Ordinary code implementation plans.
- Product, business, market, search, or content strategy.
- Broad AI theory or news summarization.
- External-service operations such as sending, deleting, labeling, archiving, or purchasing.
- Domain facts unless they affect the agent-facing context policy.

When a request crosses into another domain, produce only the agent-facing context requirements and keep domain-specific strategy out of this skill's active context.

## Hard Rules

- Prefer narrow, observable loops over broad autonomous agents when the goal is unclear.
- Gate write, destructive, credential, financial, publishing, and external-side-effect actions.
- Preserve useful failure evidence when it prevents repeated failed paths.
- Keep active context small and move large sources, logs, and examples into files.
- Verification must match risk; if behavior cannot be verified, stop with limits and unresolved risks.
