# Subagent Isolation Policy

Use this policy when designing or reviewing Codex subagent workflows.

## Default Stance

Do not spawn subagents by default. Only recommend subagents when the task needs context isolation, parallel exploration, or large codebase/file exploration. Prefer a single main agent for ordinary context design, `AGENTS.md` edits, context-related `SKILL.md` edits, and session-summary work.

## Default Boundary

Give each subagent:

- A concrete task.
- The minimum source paths or artifacts needed.
- Owned files or read-only scope.
- Expected output format.
- Constraints that must not be inferred from hidden context.

Avoid giving a subagent the whole conversation unless the task requires it.

## Isolation Rules

- Split write scopes to avoid conflicting edits.
- Keep secrets, credentials, unrelated personal data, and broad memory out of subagent prompts.
- Pass raw artifacts when validating behavior; avoid leaking expected answers.
- Ask subagents to report changed paths, commands run, findings, risks, and assumptions.
- Treat subagent output as evidence to review, not authority to merge blindly.

## Merge Rules

Before integrating subagent work:

- Reread files the subagent changed.
- Check for conflicts with newer user instructions or local edits.
- Verify assumptions against source files.
- Preserve useful failure evidence in the session summary.
- Keep handoff output concise after merging.

## Long-Running Tasks

For multi-agent or long-running workflows, maintain a visible coordinator state:

- Goal.
- Agent assignments and ownership.
- Completed work.
- Pending work.
- Shared risks.
- Recovery pointers.
- Rollback notes if a subagent changed behavior or data.
