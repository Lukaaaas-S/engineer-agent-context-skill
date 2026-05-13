# Agent Skill Boundary

Agent skills own operating systems for AI agents: workflows, context policies, tool boundaries, coding loops, verification loops, and eval-backed agent behavior.

## Agent Owns

- Goal-directed tool loops
- Tool permission and approval boundaries
- Agent state, context, memory, and handoff policy
- Failure modes, recovery paths, and verification gates
- Coding-agent execution loops
- AI behavior eval design when the task is about measuring AI output quality

## Agent Does Not Own

- Product strategy, PRDs, product roadmaps, UX scope, or feature prioritization
- GTM strategy, ICP, positioning, channels, launch motion, outbound, PLG, or sales motion
- SEO, AEO, GEO, citation measurement, schema, or answer-ready content

When a request crosses into Product, GTM, or AEO territory, produce only the agent-facing requirements and call out the appropriate handoff skill.

## Hard Rules

- Prefer narrow, observable loops over broad autonomous agents when the goal is unclear.
- Gate write, destructive, credential, financial, publishing, and external-side-effect actions.
- Preserve useful failure evidence when it prevents repeated failed paths.
- Keep active context small and move large sources, logs, and examples into files.
- Verification must match risk; if behavior cannot be verified, stop with limits and unresolved risks.
