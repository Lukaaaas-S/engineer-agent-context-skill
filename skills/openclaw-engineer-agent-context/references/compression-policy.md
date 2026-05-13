# Compression Policy

Compression should preserve actionability, evidence, and recovery paths. It is not just shortening.

## Preserve Verbatim

- Current user goal and latest correction.
- Non-negotiable constraints.
- Exact commands that reproduce a failure.
- File paths and line numbers for active edits.
- API names, env vars, config keys, and identifiers where small wording changes matter.

## Summarize

- Long logs after keeping the failing command, error class, and relevant excerpt location.
- Exploratory searches after recording which paths were checked.
- Completed plan steps after recording resulting file changes.
- Subagent output after preserving owned scope, changed paths, findings, and unresolved risks.

## Replace With Pointers

- Large source docs: path plus section heading or anchor.
- Generated artifacts: path plus purpose.
- Browser or tool traces: trace path, screenshot path, URL, or run ID.
- External references: URL plus access date when freshness matters.

## Drop Only When Explicitly Safe

- Dead-end hypotheses that do not affect future choices.
- Duplicate observations confirmed by newer evidence.
- Intermediate scratch notes after a durable summary exists.
- Tool output that is reproducible and not needed for diagnosis.

## Session Summary Minimum

Every long-task or compaction summary should include:

- Goal and acceptance criteria.
- Current plan and completed steps.
- Files changed or inspected.
- Commands run and results.
- Failed attempts and why they matter.
- Open risks, blockers, and next action.
- Recovery pointers for logs, traces, screenshots, or source references.
