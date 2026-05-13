# Pattern: Filesystem As Context

## Applicable Situation

Use when a task has more material than should fit in the active context window.

## Inputs

- Source documents
- Generated notes
- Logs or traces
- Current objective

## Default Workflow

1. Store bulky material in files instead of chat context.
2. Keep a small index that says what each file contains and when to read it.
3. Preserve restorable pointers: paths, URLs, source names, or IDs.
4. Load only the file sections needed for the current decision.
5. Summarize what was used and what remains unread.

## Branch Rules

- For source-of-truth documents, cite file paths rather than copying long passages.
- For temporary reasoning, keep a concise working note and delete or archive it when done.
- For ambiguous evidence, reread the source section before making a claim.

## Anti-Patterns

- Pasting entire source documents into the prompt.
- Summarizing away details that may be needed later without a recovery path.
- Creating references that are not linked from the controlling skill.

## Acceptance Criteria

- The agent can find the relevant source again.
- The active context stays focused on the current decision.
- Long references are discoverable without being always loaded.

## Conflict Notes

Some notes favor rich context; Codex skill design favors progressive disclosure. Use the filesystem as the default storage layer and load details on demand.

## Evidence Level

A
