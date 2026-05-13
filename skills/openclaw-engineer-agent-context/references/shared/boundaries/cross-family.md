# Shared Patterns

Shared patterns are reusable decision procedures used by multiple skill families. They prevent Product, GTM, AEO, and Agent skills from redefining the same concepts differently.

## Cross-Family Patterns

| Pattern | Used by | Purpose |
|---|---|---|
| `icp-definition` | GTM, Product | Define and score target customers without turning ICP into a vague persona. |
| `positioning-review` | GTM, Product | Align competitive alternatives, differentiated value, buyer champion, and market category. |
| `value-prop-messaging` | GTM, AEO, Product | Turn product capabilities into buyer-understandable value and message angles. |
| `growth-bottleneck-map` | GTM | Locate the highest-leverage constraint in acquisition, activation, conversion, retention, or sales. |
| `pricing-packaging-check` | GTM, Product | Check whether price, packaging, trial, or plan boundaries block conversion or product adoption. |
| `launch-motion-design` | GTM, AEO | Design a launch or market-entry motion tied to audience, channel, proof, and follow-up. |
| `ai-visibility-measurement` | AEO, GTM | Measure citations, mentions, AI referrals, AIO presence, query-set tracking, and share of answer. |
| `answer-ready-content` | AEO, GTM, Product | Structure approved product facts, value proposition, proof, FAQ, schema, and refresh cadence for answer surfaces. |
| `entity-source-credibility` | AEO, Product, GTM | Check whether an entity has clear facts, external proof, third-party consistency, and verifiable source coverage. |
| `evals-as-prd` | Agent, Product | Convert AI product quality into eval-backed acceptance criteria. |
| `data-task-score` | Agent, Product | Separate data, task, and score when designing AI product quality loops. |
| `failure-mode-map` | Agent, Product | Classify agent or AI workflow failures into actionable categories. |
| `research-to-spec` | Agent, Product | Turn research material into a scoped spec without loading the whole source library. |

## Product-Specific Patterns

| Pattern | Used by | Purpose |
|---|---|---|
| `problem-framing` | Product | Define user, job, context, evidence, and non-goal before solution work. |
| `product-requirements-shaping` | Product | Convert product decisions into testable requirements and acceptance criteria. |
| `feature-prioritization` | Product | Choose product bets and not-now decisions with explicit tradeoffs. |
| `prototype-brief` | Product | Scope a prototype around one learning goal or decision. |
| `product-review-rubric` | Product | Review product artifacts with consistent product-quality criteria. |

## AEO-Specific Patterns

| Pattern | Used by | Purpose |
|---|---|---|
| `ai-visibility-measurement` | AEO | Define repeatable measurement for citations, mentions, answer inclusion, AI referrals, and benchmark cadence. |
| `answer-ready-content` | AEO | Turn approved positioning and proof into content structures that search and answer engines can parse and cite. |
| `entity-source-credibility` | AEO | Audit official and third-party source consistency, verifiability, and trust risks. |

## Rule

Skills should reference shared patterns instead of copying their logic. Product skills may depend on ICP, positioning, value proposition, PMF, pricing, and eval patterns, but should add only Product-specific interpretation. GTM skills keep ownership of channel, launch, outbound, PLG, and sales motions. AEO skills keep ownership of visibility, content structure, source credibility, and measurement; they consume positioning, messaging, and launch decisions rather than redefining them.
