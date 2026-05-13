# Context Audit Report

## Scope

[Artifacts reviewed: AGENTS.md, SKILL.md, memory, summaries, subagent prompts, policies.]

## Findings

- Severity: [High/Medium/Low]
- Artifact: `[path]`
- Issue: [context bloat, stale policy, unrecoverable compression, memory leak, isolation gap]
- Evidence: [specific line, section, or behavior]
- Fix: [concrete change]

## Active Context Assessment

[What should stay visible and what should move out.]

## Loading Policy Assessment

[What is loaded too early, too late, or without a source pointer.]

## Compression Assessment

[Whether summaries are restorable and whether lossy drops are explicit.]

## Memory Boundary Assessment

[What belongs in durable memory versus task-local notes.]

## Subagent Isolation Assessment

[Whether delegation scope, write ownership, and handoff outputs are clear.]

## Recovery And Rollback

[Whether a future agent can resume, verify, and undo risky changes.]

## Recommended Patch

[Short patch plan or direct edits to make.]
