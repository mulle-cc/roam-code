# roam-code Master Backlog v8.0

> Updated: 25 February 2026 (Session 35 — README audit + CI fixes + issue/PR triage)
> Current: 137 commands, 101 MCP tools, 10 resources, 5 prompts, 23 core tools
> Tests: 5080 passing | Competitive score: 84/100 (was 79; +5 from scoring data + dataflow baseline)
> Backlog: **151 items** — 134 shipped, 11 open, 4 killed, 2 someday/maybe
> Research: See [Research Insights](#research-insights-february-2026) at end of document
> Competitors: See [`reports/competitor_tracker.md`](competitor_tracker.md)

---

## Open Items at a Glance (11 remaining)

### v11 Launch (3 items — external actions)
| # | Item | Effort | Epic |
|---|------|--------|------|
| 24 | Add GitHub repo topics | 10m | 4 |
| 29 | Enable GitHub Discussions | 30m | 4 |
| 31 | List on MCP directories + awesome-lists | 2-3h | 5 |

### Distribution & Growth (2 items)
| # | Item | Effort | Epic |
|---|------|--------|------|
| 36 | Partner outreach | ongoing | 5 |
| 37 | Benchmarks on major OSS repos (harness shipped, coverage expansion pending) | 2-3d | 5 |

### README Accuracy (6 items — from dual-agent review, Session 35)
| # | Item | Effort | Epic |
|---|------|--------|------|
| 146 | Remove duplicate `roam schema` entry from command table (listed in both Getting Started and Exploration) | 5m | 4 |
| 147 | Fix project structure: `graph/split.py` and `graph/why.py` don't exist in `graph/`, they are `commands/cmd_split.py` and `commands/cmd_why.py`. Also `rules/` missing `ast_match.py`, `builtin.py`, `dataflow.py`; `analysis/` missing `taint.py`; lang files "17 Tier 1" should be 19 | 15m | 4 |
| 148 | Update stale "29/29" quality benchmark — from when roam had 29 commands. Either re-run benchmarks or remove the Commands column | 30m | 5 |
| 149 | Update stale minimap example output — shows 93 commands, 18 languages, 70 tests vs actual counts | 10m | 4 |
| 150 | Fix stale MCP source code comment in `mcp_server.py` saying "16 tools + meta-tool" — should be "23 core + meta-tool" (24 total) | 5m | 4 |
| 151 | Clean up Roadmap "Next" section — remove internal ticket numbers (#24, #29, etc.) or link them properly; remove process-noise item "#112 recurring hygiene" | 10m | 4 |

---

## Already Done (DO NOT re-add)

- [x] `roam mcp` command with `--transport`, `--list-tools` flags
- [x] MCP tool namespacing with `roam_` prefix (61 tools)
- [x] Lite mode (16 core tools, `ROAM_MCP_LITE=0` for full)
- [x] `fastmcp` optional dependency (`pip install roam-code[mcp]`)
- [x] MCP tests (50 functions, 395 lines)
- [x] Structured MCP error handling
- [x] CI workflow YAML `--json` flag fix
- [x] `PRAGMA mmap_size=268435456` (256MB memory-mapped I/O) in connection.py (#11)
- [x] Size guard on `propagation_cost()` — BFS sampling for graphs >500 nodes (#12)
- [x] O(N) → O(changed) incremental edge rebuild via `source_file_id` provenance tracking (#13)
- [x] FTS5/BM25 semantic search with `porter unicode61` tokenizer + camelCase preprocessing (#14)
- [x] DB Sprint: 7 new indexes, 1 redundant removed, UPSERT pattern, batch size 500 (#15)
- [x] In-process MCP via CliRunner — eliminates subprocess overhead per tool call (#1)
- [x] MCP tool presets: core/review/refactor/debug/architecture/full via `ROAM_MCP_PRESET` env var (#3)
- [x] All 61 MCP tool descriptions shortened to <60 tokens each (#5)
- [x] `roam_expand_toolset` meta-tool — lists presets and their tools (#6)
- [x] Compound MCP operations: `roam_explore`, `roam_prepare_change`, `roam_review_change`, `roam_diagnose_issue` — each replaces 2-4 tool calls (#2)
- [x] Structured return schemas (`output_schema`) on all MCP tools — compound + core get custom schemas, rest get envelope default (#4)
- [x] Standardized exit codes: 0=success, 1=error, 2=usage, 3=index missing, 5=gate failure (#19)
- [x] Fixed command count inconsistency — actual count is 96, all references updated (#25)
- [x] Progress indicators during `roam init`/`roam index` with `--quiet` flag, stderr output (#30)
- [x] `defer_loading` annotations on non-core MCP tools — 21 always-loaded, 45 deferred (#66)
- [x] GitHub Action: composite action, SARIF upload, sticky PR comments, quality gates, SQLite caching (#20)
- [x] Idempotent sticky PR comment updater with duplicate cleanup (single marker-managed comment) (#23)
- [x] CHANGELOG.md — v1.0.0 through v11.0.0, Keep a Changelog format (#27)
- [x] CONTRIBUTING.md + bug report/feature request YAML templates + PR template (#28)
- [x] Competitive positioning table in README — category-based comparison (#76)
- [x] Deterministic output guarantee — `sort_keys=True`, timestamps→`_meta`, sorted graphs, seeded sampling (#90)
- [x] `roam syntax-check` — tree-sitter ERROR node detection for multi-agent Judge pattern, 26 languages (#92)
- [x] `roam agent-export` — auto-generate agent context bundles (`AGENTS.md` + provider-specific files like `CLAUDE.md`, `.cursorrules`) from index, `--write` flag (#65, #68)
- [x] `--budget N` Phase 1 shipped — smart JSON truncation on 4 commands + 4 MCP compounds (#9)
- [x] `roam vibe-check` — 8-pattern AI rot detection, composite 0-100 score, `--threshold` gate (#57)
- [x] PageRank-weighted truncation — importance-sorted budget truncation, `omitted_low_importance_nodes` metadata (#91)
- [x] `--mermaid` output flag on `roam layers`, `roam clusters`, `roam tour` with `mermaid.py` helper (#82)
- [x] `roam codeowners` — CODEOWNERS parser, coverage analysis, drift detection, PageRank-ranked unowned (#38)
- [x] `roam ai-readiness` — 7-dimension AI agent effectiveness score, 0-100 composite, recommendations (#84)
- [x] `roam drift` — time-decayed blame ownership drift detection, reuses CODEOWNERS parser (#39)
- [x] `roam dashboard` — unified single-screen codebase status: health + hotspots + risks + AI rot (#80)
- [x] `roam secrets` — 24-pattern secret scanning, masking, SARIF output, `--fail-on-found` gate (#44)
- [x] `roam simulate-departure` — knowledge loss simulation with time-decayed blame + CODEOWNERS + PageRank (#40)
- [x] `roam suggest-reviewers` — multi-signal reviewer scoring: ownership, CODEOWNERS, recency, breadth (#41)
- [x] `roam verify` — 5-category pre-commit consistency check with threshold gating (#85)
- [x] `roam api-changes` — 8-category API change detection across 3 severity levels (#42)
- [x] `roam onboard` — 7-section structured onboarding guide with reading order (#83)
- [x] `roam test-gaps` — BFS reverse-edge walk to find untested changed symbols (#43)
- [x] `roam ai-ratio` — 5-signal AI code estimation (Gini, bursts, patterns, comments, temporal) (#86)
- [x] `roam duplicates` — Union-Find clustered semantic duplicate detection via AST similarity (#87)
- [x] `roam partition` — multi-agent partition manifest with conflict scores, test coverage, complexity (#88)
- [x] `roam affected` — monorepo impact analysis with DIRECT/TRANSITIVE classification (#89)
- [x] `roam semantic-diff` — structural change summary: symbols added/removed/modified via tree-sitter (#77)
- [x] `roam trends` — historical metric snapshots with sparkline output in metric_snapshots table (#81)
- [x] `roam algo` precision profiles (`balanced`/`strict`/`aggressive`) + detector precision metadata (#101)
- [x] `roam algo` runtime-aware impact scoring + evidence paths + framework-aware explicit N+1 packs (#102)
- [x] `roam algo --sarif` with stable fingerprints (`primaryLocationLineHash`), codeFlows, and fix templates (#103)
- [x] CI SARIF launch hardening: per-command SARIF export set, configurable upload category, and pre-upload run/result/size guardrails with truncation warnings (#105)
- [x] Conversation-aware context ranking in `roam context` + MCP compounds with `--session-hint` and `--recent-symbol`, score/rank output, and test coverage (#94)
- [x] PyPI discoverability: keywords (graph-analysis, code-intelligence, mcp-server, tree-sitter, architecture), Documentation URL, expanded classifiers in pyproject.toml (#111)
- [x] Duplicate CI workflow consolidation — ci.yml deleted, roam-ci.yml enhanced with lint job, roam.yml converted to template (#110)
- [x] Bare `except` clause audit — zero bare except: found in codebase, already clean (#18)
- [x] Remediation steps in error messages — added to `ensure_index`, `open_db`, and 15+ commands (#50)
- [x] Symbol not found with fuzzy suggestions — FTS5 fuzzy lookup added to `resolve.py`, wired to 4 commands (#51)
- [x] `.pre-commit-hooks.yaml` — 5 hooks: secrets, syntax-check, verify, health, vibe-check (#21)
- [x] Batch MCP operations: `roam_batch_search` (10 queries) and `roam_batch_get` (50 symbols) in single MCP call with shared DB connection (#7)
- [x] `--budget N` Phase 2: extended to all list-producing commands (13 more commands), completing universal budget support (#9)
- [x] Universal progressive disclosure: `--detail` flag for full output, compact summary by default — applied to `health`, `hotspots`, `dead`, `deps`, `layers`, `clusters` (#10)
- [x] Git hook auto-indexing: `roam hooks install/uninstall/status` with append-mode markers for post-merge/post-checkout/post-rewrite (#61)
- [x] `roam dev-profile` — developer behavioral profiling: commit time patterns, Gini scatter, burst detection, session analysis, risk scoring (#78)
- [x] Install verification: `roam --check` eager flag for quick first-run validation of tree-sitter grammars, SQLite, and git availability (#115)
- [x] `roam watch` — poll-based file watcher with debouncing for always-on agent sessions (#60)
- [x] `roam search --explain` — BM25 score breakdown with field match highlights (#55)
- [x] `roam supply-chain` — dependency risk dashboard: 7 package formats, pin coverage scoring (#79)
- [x] `roam check-rules` — structural rule engine with 10 built-in rules, `.roam-rules.yml` config (#93)
- [x] `roam spectral` — Fiedler vector bisection, spectral gap metric, `--compare` vs Louvain (#73)
- [x] Bottom-up context propagation through call graph for `roam context` ranking (#72)
- [x] **Session 6:** MCP structured errors with `isError`/`retryable`/`suggested_action` (#116), `structuredContent` spec conformance (#117), 5 MCP Prompts (#118), response metadata `_meta` enrichment (#119), `roam smells` 15-detector code smell catalog (#120), `roam health --gate` quality gate enforcement (#122), `roam mcp-setup` config generator for 6 platforms (#130)
- [x] **Session 7:** `roam verify-imports` import hallucination firewall (#125), `roam vulns` vulnerability scanning CLI (#131), `roam secrets` upgraded with entropy + env-var + remediation (#133), `roam metrics` unified vital signs (#137), composite difficulty scoring for partitions (#128), quality rule profiles with inheritance (#138), MCP resources expanded 2→10 (#129)
- [x] **Session 9:** AST pattern matching with `$WILDCARD` metavariables via `ast_match` rules + `$METAVAR` captures, plus `check-rules` custom-rule integration (#121)
- [x] **Session 10:** Community rule pack shipped with 169 YAML rules under `rules/community/`, recursive rule loading, and style requirement checks (`name_regex`, `max_params`, `max_symbol_lines`, `max_file_lines`) for `symbol_match` custom rules (#136)
- [x] **Session 11:** Documentation quality uplift: new docs site pages for getting started tutorial, command reference with examples, and architecture diagram (`docs/site/getting-started.html`, `docs/site/command-reference.html`, `docs/site/architecture.html`), wired into site nav and covered by docs quality tests (#132)
- [x] **Session 12:** `roam trends --cohort-by-author` shipped with AI-vs-human cohort risk trajectories, degradation velocity, percentile comparison, and sparkline output (#139)
- [x] **Session 13:** `roam hotspots --security` shipped with dangerous-API detection + entry-point reachability scoring (#135), and `roam algo` runtime ranking v2 now uses OTel DB semantic attributes (`db.system`/operation/type) to reduce noisy runtime weighting (#104)
- [x] **Session 14:** global `--agent` CLI mode shipped (compact JSON + 500-token default budget) (#124), plus alpine-based Docker packaging (`Dockerfile`, `.dockerignore`, docs/tests) (#22)
- [x] **Session 15:** Per-symbol SNA vector shipped in `graph_metrics` (`closeness`/`eigenvector`/`clustering_coefficient`) with composite `debt_score` (#70), and `roam metrics` now computes comprehension difficulty from fan-out + information scatter + working set size (#71)
- [x] **Session 16:** Kotlin/Swift Tier-1 language upgrades shipped with dedicated extractors, registry routing, and focused extraction tests (#63, #64)
- [x] **Session 17:** Plugin/extension discovery shipped for CLI commands, algo detectors, and language extractors via entry-point/env-module registration with focused tests (#114)
- [x] **Session 18:** Coverage report ingestion shipped via `coverage-gaps --import-report` (LCOV/Cobertura/coverage.py JSON), persisted per-file/per-symbol coverage metrics, and integrated into `health`, `metrics`, and `test-gaps` outputs/scoring (#134)
- [x] **Session 19:** Clean Python library API shipped via `roam.api` (`run_json`, `RoamClient`, and structured `RoamAPIError`) for in-process embedding in agent frameworks (#69)
- [x] **Session 20:** `roam guard <symbol>` shipped as a compact sub-agent preflight bundle (definition/signature, 1-hop callers/callees, test coverage hints, breaking-risk score, and layer-violation signals) (#123)
- [x] **Session 21:** Multi-agent coordination v2 shipped via `roam agent-plan --agents N` (dependency-ordered task graph + merge sequencing + Claude Agent Teams payload) and `roam agent-context --agent-id N` (per-worker write scope, read-only deps, and interface contracts) (#126, #127)
- [x] **Session 22:** MCP async indexing shipped with `roam_init` + `roam_reindex` task-required handlers and force-reindex elicitation flow for non-blocking agent indexing/recovery (#8, #67)
- [x] **Session 23:** Daemon + webhook bridge shipped by extending `roam watch` with authenticated local HTTP triggers (`POST /roam/reindex` + `GET /health`), webhook-only mode, and webhook-force refresh policy for warm CI/index refresh flows (#95)
- [x] **Session 24:** Hybrid semantic retrieval shipped by fusing FTS5/BM25 and TF-IDF vector rankings with Reciprocal Rank Fusion in `roam search-semantic`, including index-time TF-IDF persistence and deterministic scoring (#54)
- [x] **Session 25:** Pre-indexed framework/library packs shipped in semantic retrieval (Django/Flask/FastAPI/React/Express/SQLAlchemy/pytest/stdlib), enriching cold-start framework intent matching in `roam search-semantic` (#96)
- [x] **Session 26:** Refactoring ROI estimation shipped in `roam debt --roi`, estimating developer-hours saved per quarter/year with confidence bands from complexity, churn, and coupling signals (#144)
- [x] **Session 27:** `roam docs-coverage` shipped with exported-symbol doc coverage, stale-doc drift detection, PageRank-ranked missing-doc hotlist, and threshold gating; MCP tool `roam_docs_coverage` added (#143)
- [x] **Session 28:** Refactoring intelligence shipped via `roam suggest-refactoring` (ranked proactive recommendations using complexity/coupling/churn/smells/coverage/debt) and `roam plan-refactor <symbol>` (ordered refactor plan with risk, blast radius, test gaps, layer checks, and simulation preview), plus MCP tools `roam_suggest_refactoring` and `roam_plan_refactor` (#140, #141)
- [x] **Session 29:** Basic intra-procedural dataflow baseline shipped via new `dataflow_match` rule type (dead assignments, unused parameters, source-to-sink in-function heuristics), wired into `check-rules` custom rules and surfaced in `roam dead` summary as unused-assignment signal (#142)
- [x] **Session 30:** Integration tutorials shipped for Claude Code, Cursor, Gemini CLI, Codex CLI, and Amp via new docs page (`docs/site/integration-tutorials.html`), wired into docs-site navigation with quality tests for cross-page linkage and platform coverage (#33)
- [x] **Session 31:** Benchmark publish artifact shipped via `reports/09_agent_efficiency_benchmarks.md` plus reproducible `benchmarks/agent-eval/results/summary.{json,md}` aggregation tooling, and community rule pack expanded to 554 YAML rules (602 total rules including builtin/smells/algo) via generated language-scoped style rules (#34, #145)
- [x] **Session 32:** Agent performance benchmark evidence upgraded with direct `codex` `cpp-calculator` `vanilla` vs `roam-cli` delta publication (+20 health, -40 dead symbols, +25 AQS), and Search v2 completed with optional local ONNX semantic backend (`symbol_embeddings`, `search-semantic --backend`, config/env controls, optional `roam-code[semantic]`) (#35, #56)
- [x] **Session 33:** Continuous Architecture Guardian shipped via `roam watch --guardian` snapshots + JSONL compliance artifacts, `roam report guardian` preset (snapshot/gates/trend/drift bundle), and scheduled CI workflow artifact publishing (`.github/workflows/architecture-guardian.yml`) (#58)
- [x] **Session 34:** Terminal demo GIF shipped in README with deterministic generator pipeline (`dev/generate_terminal_demo_gif.py`, `docs/assets/roam-terminal-demo.gif`) (#26), and OSS benchmark expansion got a reproducible harness/manifest/artifact lane (`benchmarks/oss-eval/*`) for #37 progress tracking.

---

## v11.0.0 Release Scope (Phase 0 + Phase 1)

The items marked **[v11]** below ship together as a single release.
Goal: fix MCP crisis + close CI gap + launch to the world.

**URGENCY UPDATE (Feb 2026 research — CORRECTED DATA):** The MCP space is larger and more competitive than v4 estimated.
Official MCP Registry: 518 servers (grew from 90 in 1 month). PulseMCP: 8,610+ servers. Total ecosystem: 17,000+.
**41% of MCP servers lack authentication** (Feb 2026 security audit) — our "100% local, zero API keys" is now a security differentiator.
SonarQube MCP has **34+ tools** (not ~10 as previously estimated), ~391 stars. CKB published counts are currently inconsistent (**76/80+ vs 90+/92**) and should be tracked as a range.
Serena MCP currently documents **40 tools** and ~20.5k stars. CodeGraphMCPServer has **Louvain community detection** (only other MCP server with graph algorithms).
roam-code is invisible on all directories. **MCP directory listings (#31) must ship in Phase 0.**

**What v11 achieves (shipped):**
- MCP token overhead: 36K → <3K tokens (core preset) — **92% reduction**
- Agent tool calls: 60-70% fewer (compound operations)
- MCP speed: 10-100x faster (in-process calls)
- Search: 5-10s → <10ms (FTS5/BM25) — **1000x faster**
- Incremental indexing: O(N) → O(changed) — correctness fix
- GitHub Action: SARIF + PR comments + quality gates
- 101 MCP tools + 10 resources + 5 prompts + 23 core preset
- 136 canonical CLI commands across 14 epics
- **v11 remaining:** 3 external actions (#24 topics, #29 Discussions, #31 MCP listings)

**v7 FINDING — Documentation crisis had blocked all of the above (now resolved):**
The actual product was ~40% bigger than what public docs previously showed. This is now reconciled across README and CHANGELOG (`#106`, `#107`, `#108`, `#109`, `#112`): README matches 136 canonical CLI commands (+1 alias = 137 invokable), MCP inventory is 101 tools + 10 resources + 5 prompts, [Unreleased] carries all shipped items with backlog IDs, README has a v11 launch narrative section, and roadmap state is aligned.

---

## Epic 1: MCP v2 Overhaul

> WHY: Agents with 50+ tools achieve 60% task success; with 5-7 tools = 92%.
> Our 61 tools at ~36K tokens is actively hurting agent performance.
> CKB's advantage is presets + compounds, not tool count.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 1 | **[v11]** Replace subprocess MCP with in-process Python calls | 3d | YES | — | **DONE** |
| 2 | **[v11]** Compound MCP operations: `roam_explore`, `roam_prepare_change`, `roam_review_change`, `roam_diagnose_issue` | 3-4d | YES | #1 | **DONE** |
| 3 | **[v11]** MCP tool presets: core (16), review (27), refactor (26), debug (27), architecture (29), full | 2-3d | YES | #1 | **DONE** |
| 4 | **[v11]** Structured return schemas on all MCP tool descriptions | 1-2d | YES | #3 | **DONE** |
| 5 | **[v11]** Shorten all tool descriptions to <60 tokens each | 1d | YES | #3 | **DONE** |
| 6 | **[v11]** `roam_expand_toolset` meta-tool for dynamic mid-session preset switching | 2-3d | YES | #3 | **DONE** |
| 7 | Batch MCP operations: `batchSearch` (10 queries), `batchGet` (50 symbols) — agents make 10+ sequential calls; batching = 10x fewer round trips | 2-3d | no | #1 | **DONE** |
| 8 | MCP Resources/Prompts + async Tasks + Elicitation support (2025-11-25 revision) — agents need non-blocking indexing | 2-3d | no | #1 | **DONE** |
| 9 | Universal `--budget N` token-cap flag on all commands (Phase 1 shipped on 4 commands + 4 compounds; Phase 2 full rollout pending) | 2d | no | — | **DONE** |
| 10 | Universal progressive disclosure (summary + `--detail` flag) — agents get summary first, drill into detail only when needed, saving context window tokens | 2-3d | no | — | **DONE** |
| 66 | **[QUICK WIN]** Ensure `defer_loading: true` on all non-core MCP tools (Claude Code Tool Search compat) | 0.5d | no | — | **DONE** |
| 67 | MCP Tasks support for `roam init`/`roam reindex` — async indexing with poll-for-completion; agents shouldn't block on 30s indexing | 2-3d | no | #1 | **DONE** |
| 68 | Agent-oriented codebase summary export — auto-generate a multi-agent context bundle (`AGENTS.md` + provider-specific files) from roam analysis | 2-3d | no | — | **DONE** |
| 69 | Clean Python library API for code-execution-with-MCP — expose core as importable functions; agent frameworks can embed roam directly | 5d | no | — | **DONE** |
| 90 | **Deterministic output guarantee** — ensure all MCP JSON output uses sorted keys, topological edge ordering, no timestamps, stable iteration order. Critical for LLM **prompt caching** (Anthropic/OpenAI rely on exact prefix matching; non-deterministic output breaks cache on every turn, costing users 10x in tokens) | 1-2d | no | — | **DONE** |
| 91 | **PageRank-weighted truncation** for `--budget N` (#9) — when token budget is hit, drop lowest-PageRank nodes first, append `"truncated": true, "omitted_low_importance_nodes": N` metadata so agents know they got the most important data and can drill down | 1-2d | no | #9 | **DONE** |
| 94 | Conversation-aware PageRank personalization for context delivery (`--budget`, MCP compounds, and `roam context`) using task/session signals to rank relevant nodes first; agents need context ranked by current task | 2-3d | no | #9, #91 | **DONE** |
| 97 | Smart agent profile targeting for `roam agent-export` — generate best-fit outputs per client capability (generic `AGENTS.md` fallback + provider-specific variants such as `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, editor rule files) | 2-4d | no | #68 | **DONE** |
| 98 | Add **Streamable HTTP** transport support (`/mcp` endpoint model), including protocol-version header handling, optional session IDs, localhost/origin hardening, and protected-resource metadata compatibility; keep `stdio` as default and legacy SSE fallback | 3-5d | no | #1 | **SHIPPED (BASELINE)** |
| 99 | Expand MCP tool metadata from `deferLoading`-only to full annotation strategy (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`, `title`) plus `ToolExecution.taskSupport` on long-running tools | 2-3d | no | #4, #67 | **DONE** |
| 100 | MCP client compatibility profile + conformance tests (Copilot tools-only constraints, AGENTS precedence behavior, CLAUDE/GEMINI/CODEX file handling, Gemini config schema behavior, remote-auth capability matrix) | 2-4d | no | #68, #97 | **DONE** |

**Epic outcome:** Token overhead drops from ~36K to ~3K. Agent success rate jumps from ~60% to ~92%.

**New context (Feb 2026 — ENRICHED):** MCP spec added Tasks primitive, output schemas (we're ahead — 97.1% of MCP tools lack schemas per arXiv:2602.14878), and MCP Apps for interactive UI. Claude Code Tool Search (#66) achieves 85% context reduction via `defer_loading`. Anthropic's code-execution-with-MCP (#69) achieves 98.7% token reduction. Context engineering is now a formal discipline (Martin Fowler); `--budget N` (#9) is increasingly important.

**MCP-Atlas benchmark (Feb 2026):** Best model achieves only **62.3% on multi-tool tasks** — validates our compound operations approach (#2 done). Fewer tool calls = higher success rate. This is our strongest data point for the preset + compound architecture.

**Tool Smells paper (arXiv:2602.14878):** 97.1% of MCP tools have description smells. Shorter targeted descriptions outperform verbose ones. Our <60 token descriptions (#5 done) put us in the top 2.9%. CKB's preset architecture still validates preset-driven MCP design, but published counts now conflict by page (docs show 14 core with 76/80+ full-preset references vs other CKB pages claiming 90+/92).

**Prompt caching blind spot (v6 strategic insight):** Anthropic and OpenAI both rely on exact prefix matching for prompt context caching in 2026. If roam's MCP output includes timestamps, non-deterministic key ordering, or randomly ordered graph edges, it breaks the cache every turn — costing users massive token waste. #90 (deterministic output) is a high-impact, low-effort item that enables us to market: *"roam's deterministic output is optimized for LLM context caching, saving 90% on token costs."*

**Priority adjustments:** #9 elevated — agents need budget-aware context. #90 elevated — prompt caching is the hidden cost multiplier. #91 ensures smart truncation when budget is hit. #66 is zero-risk, high-impact quick win. #68 addresses the #1 developer pain (finding information) and every agent's first action (reading project docs).

---

## Epic 2: Performance Foundations

> WHY: Incremental indexer has O(N) correctness bug. Search is 1000x slower than it should be.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 11 | **[v11]** `PRAGMA mmap_size = 268435456` in connection.py | 1h | YES | — | **DONE** |
| 12 | **[v11]** Size guard on `propagation_cost()` in cycles.py (>500 nodes) | 1h | YES | — | **DONE** |
| 13 | **[v11]** Fix incremental edge rebuild: store per-file ref index, O(N) → O(changed) | 2-3d | YES | — | **DONE** |
| 14 | **[v11]** Replace TF-IDF with SQLite FTS5/BM25 (zero new deps) | 1-2d | YES | — | **DONE** |
| 15 | DB Sprint: add 5 missing indexes, remove 1 redundant, UPSERT pattern, batch size 500+ | 1d | no | — | **DONE** |
| 16 | Fix cycle detection to use SCC data instead of 2-cycle self-join | 3-5h | no | — | **DONE** |
| 17 | Consolidate duplicated EXTENSION_MAP + schema definitions | 2h | no | — | **DONE** |
| 18 | Replace bare `except` clauses with logged exception handling | 1h | no | — | **DONE (already clean)** |
| 70 | Per-symbol SNA metric vector (degree, betweenness, closeness, eigenvector, clustering coefficient) + composite debt score | 5d | no | — | **DONE** |
| 71 | Comprehension difficulty metrics: fan-out, information scatter (distinct files in N-hop closure), working set size | 5d | no | — | **DONE** |
| 72 | Bottom-up context propagation through call graph for `roam context` — propagate callee signatures upward; agents get richer context automatically | 5d | no | — | **DONE** |
| 73 | Spectral bisection (Fiedler vector) module decomposition as alternative to Louvain | 3-5d | no | — | **DONE** |

**Epic outcome:** Everything feels instant. Correctness bugs fixed. Graph analysis reaches academic state-of-the-art.

**New context (Feb 2026):** PLOS ONE study proved SNA metrics combined with traditional TD metrics achieve 87% recall / 152% F1 for debt detection — roam already computes PageRank; adding full centrality suite is low-hanging fruit (#70). Neuroscience research shows SonarSource cognitive complexity is a poor proxy for actual developer difficulty; fan-out + scatter are better predictors (#71). Code-Craft paper demonstrated 82% retrieval improvement via bottom-up call graph summarization (#72). Spectral methods provide mathematically optimal graph bisection (#73).

---

## Epic 3: CI/CD Integration

> WHY: #1 competitive gap. Every SAST tool (CodeQL, SonarQube, Semgrep, CodeScene) has CI.
> Composite action = no Docker overhead, sub-60s PR analysis, zero API keys.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 19 | **[v11]** Standardized exit codes for error categories | 4-8h | YES | — | **DONE** |
| 20 | **[v11]** GitHub Action: composite action, SARIF upload, sticky PR comment, quality gate, SQLite cache | 2-3d | YES | #19 | **DONE** |
| 21 | `.pre-commit-hooks.yaml` for pre-commit framework | 1d | no | — | **DONE** |
| 22 | Docker image (alpine-based) | 1d | no | — | **DONE** |
| 23 | Idempotent sticky PR comment updater (single marker-managed comment + duplicate cleanup) | 3d | no | #20 | **DONE** |
| 74 | Trend-aware fitness functions: alert on velocity toward violation, not just threshold breach | 3-5d | no | #20 | **DONE** |
| 75 | `--changed-only` incremental CI mode: only analyze changed files + dependents on PR | 1-2d | no | #20 | **DONE** |
| 95 | Daemon + webhook bridge for precomputed index refresh (post-merge/post-push), so CI checks reuse warmed analysis state | 3-5d | no | #20, #75 | **DONE** |
| 105 | SARIF launch hardening: per-command SARIF export + configurable upload `category` + pre-upload guardrails for GitHub SARIF limits (size/result caps) | 0.5-1d | no | #20 | **DONE** |

**Epic outcome:** roam-code runs in CI on every PR. SARIF results in GitHub Code Scanning.

**New context (Feb 2026):** CI integration is now absolute table stakes — every major competitor (CodeQL, SonarQube, Semgrep, CodeScene) has it. #19-#20 must ship. Trend-aware gates (#74) detect "complexity growing 5%/phase" before thresholds break. Incremental mode (#75) enables sub-60s PR analysis on large repos.

---

## Epic 4: Launch Readiness

> WHY: Must ship before external launch/distribution. A maintained-looking repo gets 3-5x more stars.
> 34.2% of developers cite docs as #1 trust signal.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 24 | **[v11]** Add GitHub repo topics (cli, static-analysis, mcp, etc.) | 10m | YES | — | |
| 25 | **[v11]** ~~Fix command count inconsistency (94 vs 95)~~ | 10m | YES | — | **DONE** |
| 26 | **[v11]** Terminal demo GIF for README | 4-8h | YES | — | **DONE** |
| 27 | **[v11]** CHANGELOG.md (v11 + retroactive v10.x) | 2-4h | YES | — | **DONE** |
| 28 | **[v11]** CONTRIBUTING.md + issue/PR templates | 4-8h | YES | — | **DONE** |
| 29 | **[v11]** Enable GitHub Discussions | 30m | YES | — | |
| 30 | **[v11]** Progress indicator during `roam init` / `roam index` | 2-4h | YES | — | **DONE** |
| 76 | **[v11]** Competitive positioning page / comparison table in README (vs Augment, Claude Context, CodeGraphContext, CodeScene MCP) | 0.5d | YES | — | **DONE** |
| 106 | **[v11] [RELEASE BLOCKER]** README accuracy overhaul — update command count (~120), MCP tool count (90), add 19+ missing commands to command tables, update MCP section with v11 story (presets, compounds, schemas, 92% reduction), fix ASCII diagram ("94 Commands" → actual), update comparison table numbers | 4-8h | YES | — | **DONE** |
| 107 | **[v11] [RELEASE BLOCKER]** CHANGELOG [Unreleased] completeness — add all 20+ items shipped in Sessions 2-5 (vibe-check, ai-readiness, secrets, codeowners, drift, dashboard, duplicates, partition, affected, semantic-diff, trends, etc.) | 2-4h | YES | — | **DONE** |
| 108 | **[v11] [RELEASE BLOCKER]** Command count reconciliation — verify actual count from `_COMMANDS` dict in cli.py (explore found ~116 vs documented 96), update everywhere: cli.py, README, CLAUDE.md, llms-install.md, launch copy | 1-2h | YES | — | **DONE** |
| 109 | **[v11]** v11 narrative section in README — add "What's New in v11" section covering MCP v2, performance, compound operations, presets, CI integration. This is the story new users and agents need to see | 2-4h | YES | #106 | **DONE** |

**Epic outcome:** Repo looks maintained, professional, ready for public attention. **Public docs match reality.**

**New context (v7 gap analysis finding — CRITICAL):** The product had grown ~40% beyond public docs. That documentation parity gap is now closed (`#106` + `#107` + `#108` + `#109` + `#112`): README command/MCP surfaces are aligned, CHANGELOG [Unreleased] reflects shipped scope with backlog IDs, README includes a clear v11 story section, and roadmap state is refreshed. **Public launch now depends mainly on external launch tasks.**

**Previous context (Feb 2026 — CORRECTED):** Claude Context (Zilliz) has 5,400+ stars with 4 tools. Augment claims "70% agent improvement" but has only 1 MCP tool. CodeGraphContext has 19 tools, 775 stars, requires external graph DB. **New entrants:** CodePrism (18 tools, Rust-based), CodeGraphMCPServer (14 tools, **has Louvain** — only other MCP server with graph algorithms), code-graph-mcp (9 tools, claims PageRank). A clear comparison table showing roam's actual MCP tools, commands, 26 languages, zero cloud dependency, and zero API keys is essential for conversion. The "100% local" message is a critical security differentiator: **41% of MCP servers lack authentication** (Feb 2026 audit).

---

## Epic 5: Distribution and Adoption

> WHY: Focus on durable delivery outcomes: discoverability, integrations, and measurable proof.
> MCP directory listings + integration tutorials + benchmarks compound over time.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 31 | **[v11] [URGENT]** List on MCP directories: Official MCP Registry, Smithery, mcp.so, PulseMCP, mcpserverfinder.com, Glama.ai + submit PRs to 4 awesome-mcp-servers GitHub lists + GitHub Copilot MCP Registry | 2h | YES | Epic 1, #106 | |
| 32 | Community launch thread(s), channel-agnostic and optional (explicitly not required for v11 closeout) | 1-2h + optional engagement | no | Epic 4, #106-#109 | **DEFERRED (strategy: deliverables-first, no single-channel dependency)** |
| 33 | Integration tutorials for Claude Code, Cursor, Gemini CLI, Codex CLI, Amp (Sourcegraph) — end-to-end setup + workflow guides, not just MCP config snippets. This is how Context7 got 44k stars. | 2-3d | no | Epic 1 | **DONE** |
| 34 | Blog post: agent efficiency benchmarks (token savings) | 2-3d | no | Epic 1 | **DONE** |
| 35 | Agent performance benchmark: measure task completion rate with/without roam MCP (counter Augment's "70% improvement" claim). `benchmarks/agent-eval/` framework exists — run it, publish numbers | 3-5d | no | — | **DONE** |
| 36 | Partner outreach to Claude Code, Codex CLI, Gemini CLI teams | ongoing | no | Epic 1 | |
| 37 | Benchmarks on major OSS repos (Linux kernel, React, Django, CPython, FastAPI) | 2-3d | no | — | **IN PROGRESS (harness + local snapshot artifacts)** |

**Epic outcome:** roam-code visible on discovery channels, with conversion driven by tutorials and benchmark evidence.

**Channel-Agnostic Launch Playbook (optional, post-deliverables):**
- Publish one concise launch note after `#24/#29/#31` are complete (`#26` already shipped).
- Use the same core narrative across channels: deterministic local analysis, structural intelligence, and agent workflow impact.
- Include one concrete artifact per post: demo GIF, benchmark chart, or CI/SARIF screenshot.
- Prioritize response quality over channel count in the first engagement window.
- Treat social/community channels as amplification, not release gating.

**Key messaging themes (validated by research — ENRICHED):**
1. "100% local, zero API keys, no code leaves your machine" — NOW STRONGER: 41% of MCP servers lack auth, 43% have injection flaws
2. "AI agents read files. roam-code understands architecture." — deterministic vs probabilistic
3. "Your codebase is 42% AI-generated. Do you know how much of it is rotting?" — CodeRabbit: 1.7x more issues in AI code
4. "Lost Cody Free? roam-code gives you code intelligence for free, forever." — Sourcegraph pivot opportunity
5. "Best AI model achieves 62.3% on multi-tool MCP tasks. Our compound operations cut tool calls 60-70%." — MCP-Atlas data

---

## Epic 6: Ownership & Team Intelligence

> WHY: No CLI tool fuses CODEOWNERS with git blame. CKB + CodeScene own this space.
> roam-code has the graph data to do it better — 100% locally.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 38 | CODEOWNERS parser + `roam codeowners` command (coverage, top owners, unowned files) | 3-4d | no | — | **DONE** |
| 39 | Ownership drift detection: `roam drift` (declared vs actual from time-decayed blame) | 2-3d | no | #38 | **DONE** |
| 40 | Knowledge loss simulation: `roam simulate-departure` (what breaks if dev X leaves?) | 3-4d | no | #38 | **DONE** |
| 41 | Reviewer suggestion: `roam suggest-reviewers` (multi-signal scoring) | 2-3d | no | #38, #39 | **DONE** |

**Epic outcome:** CodeScene-level team intelligence, 100% local, zero cost.

**New context (Feb 2026):** CKB already ships CODEOWNERS + ownership drift + reviewer suggestions — validating all 4 items in this epic. CKB has 59 stars and Go-only incremental indexing (12 languages). roam can do this better with 26 languages and graph-backed scoring. Serena has ownership-like features via LSP but no CODEOWNERS parsing. **Epic 6 is now validated by market evidence — elevate priority.**

---

## Epic 7: Change Intelligence

> WHY: Breaking API detection = CKB exclusive we can beat with AST diff.
> Test gap analysis extends our existing test convention detection.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 42 | Breaking API change detection: compare symbol signatures pre/post commit | 3-5d | no | — | **DONE** |
| 43 | Test gap analysis: map changed symbols to missing test coverage | 2-3d | no | — | **DONE** |
| 44 | Secret scanning (regex patterns for API keys, tokens, passwords) | 3-4d | no | — | **DONE** |
| 77 | `roam semantic-diff` — structural change summary: symbols added/removed/modified, changed call edges, signature changes, new imports | 3-5d | no | — | **DONE** |
| 78 | Developer behavioral profiling for pr-risk: commit time patterns, change scatter (Gini), burst detection | 3-5d | no | — | **DONE** |
| 79 | `roam supply-chain` — dependency risk dashboard: direct vs transitive depth, vuln reachability, maintenance status, transfer signals | 3-5d | no | — | **DONE** |

**Epic outcome:** PR review gets breaking change alerts + test gap warnings + secret leak detection + semantic diffs + supply chain risk.

**New context (Feb 2026 — ENRICHED):** PR volume up 29% YoY due to AI coding. GitHub considering "kill switch" for AI-slop PRs. Code review is the quality bottleneck. **CodeRabbit (2M+ repos): AI-generated code has 1.7x more issues and 3x readability problems** — validates every item in this epic. CKB already has `compareAPI` for breaking API change detection (#42) — validates the feature. Semantic diff (#77) is what the industry is moving toward — Greptile and Qodo 2.0 both offer structural change analysis. CKB has 26-pattern secret scanning (#44). MSR 2025 validated developer behavioral features for JIT defect prediction (#78). npm supply chain attacks and EU CRA compliance make supply chain analysis (#79) increasingly important.

---

## Epic 8: Agent Error Recovery & Guidance — ALL DONE

> WHY (REFRAMED — agents-only pivot): Agents waste tool calls on bad inputs and can't self-recover from errors.
> Actionable error messages, next-step guidance, and self-diagnostic capability reduce wasted round trips.
> Human CLI polish items (#46, #47, #49, #53) killed — agents use MCP tools, never see `--help`.
> **STATUS: All 5 items (#45, #48, #50, #51, #52) are now DONE. Full agent error recovery chain shipped.**

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 45 | Next-step suggestions in key command output — agents get actionable "what to investigate next" after each result, reducing planning burden | 4-8h | no | — | **DONE** |
| 48 | `roam doctor` setup diagnostics — agents self-diagnose why roam isn't working (missing deps, stale index, broken config, tree-sitter grammar availability). First-run success rate multiplier | 4-8h | no | — | **DONE** |
| 50 | Remediation steps in error messages — agents need "run `roam index` first" not just "index missing" to self-recover. Currently agents get raw errors with no guidance | 4-8h | no | — | **DONE** |
| 51 | Consistent "symbol not found" with fuzzy suggestions — agents make approximate symbol name guesses; FTS5 makes this trivial to implement. Without this, agents waste 2-3 retries on typos | 4-8h | no | #14 | **DONE** |
| 52 | `roam reset`/`roam clean` for index management — agents need recovery path from corrupted/stale indexes | 2-4h | no | — | **DONE** |
| 80 | `roam dashboard` — unified single-screen codebase status: health + hotspots + debt + bus-factor + recent churn | 2-3d | no | — | **DONE** |
| 81 | `roam trends` — historical metric snapshots with sparkline output, stored in local SQLite | 3-5d | no | — | **DONE** |
| 82 | `--mermaid` output flag on architecture commands (`roam layers`, `roam tour`, `roam graph`) | 1-2d | no | — | **DONE** |
| 83 | `roam onboard` — structured new-developer guide: architecture overview, key entry points, critical paths, suggested first-read files | 2-3d | no | — | **DONE** |

**Epic outcome:** Agents self-recover from errors and get guided next steps, reducing wasted MCP tool calls.

**v7 gap analysis finding (now resolved):** This entire epic represented the #1 reason agents fail on first use with roam. All 5 items (#45, #48, #50, #51, #52) are now DONE. Agents now get remediation hints on error, fuzzy symbol suggestions, `roam doctor` diagnostics, actionable next-step guidance, and `roam reset`/`roam clean` for index recovery.

**Killed from this epic (agents-only pivot):** #46 fuzzy command matching (agents use exact MCP tool names), #47 usage examples in --help (agents use MCP descriptions), #49 "5 core commands" --help framing (agents use presets), #53 Windows PATH detection (MCP is in-process, PATH irrelevant).

---

## Epic 9: Search v2

> WHY: squirrelsoft has BM25+ONNX hybrid. After FTS5 ships in v11, upgrade path is clear.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 54 | Hybrid BM25 + vector search with Reciprocal Rank Fusion | 5-10d | no | #14 | **DONE** |
| 55 | Search score explanation (`--explain` flag) | 2-3d | no | #14 | **DONE** |
| 56 | Local ONNX Runtime embedding model (optional dependency) | 10d | no | #54 | **DONE** |
| 96 | Pre-indexed framework/library packs (popular stdlib + framework symbols) to improve cold-start retrieval and onboarding quality | 3-5d | no | #14 | **DONE** |

**Epic outcome:** Best-in-class local code search. Beats squirrelsoft at their own game.

---

## Epic 10: AI Debt & Architecture Guardian

> WHY: 75% of companies face moderate-to-severe tech debt in 2026, largely from AI code.
> The "10x feature": shift from snapshot tool to continuous infrastructure layer.
> **MARKET VALIDATION (Feb 2026 — ENRICHED WITH SPECIFIC DATA):**
> GitClear (211M lines): AI code duplication up 4x, refactoring collapsed from 25% to <10%.
> SonarSource: 42% of committed code is AI-generated, 96% of devs don't trust it.
> **CodeRabbit (2M+ repos): AI code has 1.7x more issues, 3x more readability problems.**
> Ox Security ($60M Series B): 10 anti-patterns with specific prevalence: hardcoded credentials 70-80%, lack of input validation 80-90%, improper error handling 80-90%, insecure HTTP 45-55%, SQL injection 25-35%, path traversal 20-30%, insecure deserialization 15-25%, command injection 30-40%, SSRF 15-25%, JWT misuse 35-45%. **5 of 10 detectable by roam today.**
> Stack Overflow: "AI can 10x devs...in creating tech debt."
> **This is the hottest topic in developer tools. CodeScene, TurinTech Artemis, Codacy AI Risk Hub, OX VibeSec all competing.**

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 57 | **`roam vibe-check`** — expanded Vibe Code Auditor with 8-pattern taxonomy and composite AI rot score (see detection table below). **STRATEGIC: This is the Trojan Horse / viral growth engine. A single readable markdown report showing "8 hallucinated imports, 42 empty try/catch blocks, 18 semantic clones" is high-share launch content. Transitions roam from agent-tool to governance-tool for humans managing AI agents.** | 5-7d | no | — | **DONE (ELEVATED THEME)** |
| 58 | Continuous Architecture Guardian: daemon/Action monitoring trends, drift detection, compliance-ready reports, Tier 3 trend analysis | 10-15d | no | #20, #81 | **DONE** |
| 84 | AI Readiness Score: 0-100 estimating AI agent effectiveness on this codebase (dead code noise, naming consistency, module coupling, test signals) | 2-3d | no | #57 | **DONE** |
| 85 | `roam verify` — pre-commit AI code consistency check: naming conventions, import patterns, error handling, duplicate logic detection | 3-5d | no | #57 | **DONE** |
| 86 | AI Code Ratio Estimation — statistical estimate of AI-generated code % via commit patterns (change concentration Gini, conditional density, comment density) | 1-2d | no | — | **DONE** |
| 87 | Semantic duplicate detector — AST similarity for functionally equivalent code with divergent edge-case handling (not textual clones) | 2-3d | no | — | **DONE** |
| 93 | Structural rule packs with optional autofix templates (ast-grep-style relational matching on top of `.roam/rules`) for policy-driven smell/security/style detection; agents need automated policy enforcement | 4-6d | no | — | **DONE** |
| 101 | `roam algo` precision governance: detector-level precision metadata + profile controls (`balanced`/`strict`/`aggressive`) to trade recall vs precision explicitly | 1-2d | no | #57 | **DONE** |
| 102 | `roam algo` richer reasoning layer: runtime-aware impact scoring, semantic evidence paths, and framework-aware explicit N+1 detector packs with guard hints | 2-3d | no | #57, #20 | **DONE** |
| 103 | `roam algo --sarif`: algorithm findings exported with stable fingerprints, path-style `codeFlows`, and SARIF `fixes` payload | 1-2d | no | #20, #102 | **DONE** |
| 104 | Runtime ranking v2 for `roam algo`: fold OpenTelemetry DB semantic attributes (operation/type/system) into impact scoring to reduce noisy trace weighting | 2-4d | no | #102, #103 | **DONE** |

**#57 Detection Taxonomy (8 patterns):**

| Pattern | Prevalence | Detection Method | Existing Infrastructure |
|---------|-----------|-----------------|------------------------|
| Dead exports / orphaned symbols | High | Graph fan-in = 0 | `roam dead` (done) |
| Short-term churn (revised within 14 days) | 7.9% of AI code | Git log temporal analysis | `git_stats.py` (extend) |
| Empty error handlers | 70-80% | Tree-sitter catch-block query | `parser.py` (add query) |
| Abandoned stubs (TODO/pass/empty bodies) | High | Tree-sitter body analysis | `parser.py` (add query) |
| Hallucinated imports (unresolvable) | 27.8% of AI suggestions | Cross-ref imports vs file index | `symbols.py` + `relations.py` |
| Error handling inconsistency | 80-90% | Error pattern classification + variance | `effects.py` (extend) |
| Comment density anomaly | 90-100% | Comment-to-code ratio outliers | New (simple) |
| Copy-paste ratio exceeding refactoring | 12.3% and rising | AST similarity + git move detection | `indexer.py` + `git_stats.py` |

**Epic outcome:** roam-code becomes "the codebase X-ray that catches what AI coding misses." The Vibe Code Auditor is the hero feature for launch narratives and blog content.

**Competitive landscape for this epic (UPDATED):**
- **CodeScene:** Markets "AI-Ready Code" whitepaper + Code Health for AI. MCP server (14 tools). Git forensics overlap.
- **TurinTech Artemis:** "Evolutionary AI platform for AI-driven tech debt." Intel partnership. Dev preview Dec 2025.
- **Codacy AI Risk Hub:** Governance dashboard, risk scoring, policy enforcement. Enterprise SaaS. Has MCP integration.
- **OX VibeSec ($60M Series B):** Prevents vulns at AI generation time. 10 anti-patterns with prevalence data. Security-first.
- **Qodo 2.1:** Continuous learning rules for AI code review. "Rule-based learning" approach.
- **DeepWiki (Cognition/Devin):** AI-generated wiki/docs/Mermaid for repos. Indirect competitor for comprehension.
- **roam-code advantage:** 100% local, zero cost, deterministic (not AI-analyzing-AI), 26 languages, graph algorithms none of them have. Only tool that can detect architectural anti-patterns (cycles, coupling, complexity) created by AI code, not just security flaws.

---

## Epic 11: Platform Expansion

> WHY: These expand roam's reach as agent infrastructure.
> #59 (docs site) and #62 (VS Code extension) moved to Someday/Maybe — agents use MCP, not docs sites or IDE extensions.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 60 | File watcher mode (`roam watch`) with debouncing — keeps index fresh for always-on agent sessions | 2-3d | no | — | **DONE** |
| 61 | Git hook auto-indexing (post-merge, post-checkout, post-rewrite) — zero-friction index freshness | 1-2d | no | — | **DONE** |
| 63 | Kotlin upgrade to Tier 1 | 3d | no | — | **DONE** |
| 64 | Swift upgrade to Tier 1 | 3d | no | — | **DONE** |
| 65 | Auto-generate generic agent context docs from roam index (`AGENTS.md` + provider-specific exports) | 2-3d | no | — | **DONE** |

**Epic outcome:** roam-code available in more contexts: file watch, git hooks, more languages.

---

## Epic 12: Multi-Agent Orchestration

> WHY: Multi-agent coding is THE dominant trend of 2026.
> Claude Agent Teams, Codex multi-agent, VS Code multi-agent orchestration — all production reality.
> Agents need module boundaries, conflict detection, and work estimation that roam already computes.
> **roam-code should be the "operating system" for multi-agent coding.**

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 88 | Multi-agent partition manifest — extend `roam orchestrate` with conflict probability scores, test coverage per partition, estimated complexity, suggested agent roles | 3-5d | no | — | **DONE** |
| 89 | `roam affected` — given a git diff, identify which packages/workspaces are affected and need rebuilding/retesting (monorepo impact analysis) | 3-5d | no | — | **DONE** |
| 92 | **`roam_check_syntax_integrity`** — tree-sitter syntax validation MCP tool for multi-agent Judge pattern. AI Worker agents write syntax-broken code constantly; tree-sitter is fault-tolerant and can detect `ERROR` nodes in the AST. A Judge agent uses this to instantly verify if a Worker corrupted a file, without needing a full compiler/interpreter. Expose as both CLI (`roam syntax-check`) and MCP tool. | 1-2d | no | — | **DONE** |

**Epic outcome:** roam-code becomes the coordination layer for multi-agent coding workflows.

**New context (Feb 2026 — ENRICHED with agent platform data):** Anthropic's 2026 Agentic Coding Trends Report identifies multi-agent orchestration as a defining trend. Standard pattern: Planner + Worker + Judge with git worktree isolation. VS Code v1.110 (Feb 2026) shipped multi-agent support. Cognition acquired Windsurf for $250M (Devin + IDE integration).

**Agent platform specifics that validate this epic:**
- **Claude Code** (68.3k stars, 4% of GitHub commits): Agent Teams use parallel workers. No persistent index, no call graph, no blast radius — all things roam provides.
- **Codex CLI** (~61.4k stars): **#1 recognized limitation is no codebase indexing** (per GitHub issues). roam directly fills this gap.
- **Gemini CLI** (~95.3k stars): **#1 feature request is persistent codebase indexing**. Uses LLM-driven "Codebase Investigator" — non-deterministic, expensive.
- roam-code's `orchestrate` command is uniquely positioned but output needs structuring for direct consumption by Claude Agent Teams / Codex SDK.

---

## Epic 13: Infrastructure Quality & First-Run Experience

> WHY (v7 gap analysis): Codebase has grown 40% beyond documentation. Duplicate CI workflows,
> stale PyPI metadata, missing install verification, no plugin discovery. These are the cracks
> that erode trust on first contact. `#106/#107/#108/#109/#112` closed the launch documentation parity gap.

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 110 | Duplicate CI workflow consolidation — ci.yml and roam-ci.yml serve overlapping purposes, confusing contributors. Merge into single workflow or clearly separate (test vs analysis) | 1-2h | no | — | **DONE** |
| 111 | PyPI discoverability enhancement — add keywords (graph-analysis, code-intelligence, mcp-server, tree-sitter, architecture), Documentation URL, expand classifiers (Topic::Software Development::Libraries) | 30m | no | — | **DONE** |
| 112 | README Roadmap section refresh — mark completed items as `[x]` (many still `[ ]`), add v11 features, remove stale items. Currently contradicts CHANGELOG | 1h | no | #106 | **DONE** |
| 113 | `roam endpoints` — list all detected REST/GraphQL/gRPC endpoints with handlers. REST bridge exists (`bridge_rest_api.py`) but no CLI surface. Atlassian: "finding services/APIs" is #1 friction point | 2-3d | no | — | **DONE** |
| 114 | Plugin/extension discovery mechanism — enable community to add commands, detectors, language extractors without forking. Architecture supports it (LanguageExtractor, LanguageBridge) but no discovery/registration for external plugins | 3-5d | no | — | **DONE** |
| 115 | Install verification — `roam doctor` (#48) covers diagnostics, but also need first-run validation that confirms tree-sitter grammars load, SQLite works, git is available. Could be part of #48 or standalone `roam --check` | 2-4h | no | #48 | **DONE** |

**Epic outcome:** Infrastructure matches product quality. First-run experience inspires confidence. Contributors find a clean, consistent project.

**v7 gap analysis findings that created this epic:**
- Explore agent found ~116 commands registered but all docs say 96
- 86 MCP tools exist but README says 61, MEMORY.md says 65
- ci.yml and roam-ci.yml appear to be duplicates
- PyPI has no keywords, no Documentation URL
- README Roadmap has done items marked `[ ]` and missing v11 features
- No way for community to contribute commands or language extractors without forking
- No install verification beyond `roam --version`

---

## Epic 14: Agent-Ready Polish (Research-Derived, Feb 2026)

> WHY: 5 deep research reports (MCP readiness, agent workflows, error recovery, multi-agent, competitor features) identified 15 high-impact items that complete the product.
> Source: `reports/research_*.md` and `reports/strategic_moat_analysis.md`
> These items address the remaining 30% of the agent interface layer and 50% of the polish layer.

### MCP Protocol Compliance

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 116 | **MCP error conformance:** return `isError: true` on tool failures + `retryable` boolean + `suggested_action` field. Agents currently parse text to detect errors; spec provides this flag | 2-4h | no | — | DONE |
| 117 | **`structuredContent` spec conformance:** roam declares `outputSchema` on all tools but doesn't return `structuredContent` field required by 2025-06-18 MCP spec. Non-conformant until fixed | 1d | no | #4 | DONE |
| 118 | **MCP Prompts (5-8 workflow prompts):** expose `/roam-onboard`, `/roam-review`, `/roam-debug`, `/roam-refactor`, `/roam-health-check` as MCP prompt primitives. Claude Code and VS Code render as slash commands. CodeGraphMCPServer has 6 prompts, we have 0 | 1d | no | — | DONE |
| 119 | **Response metadata enrichment:** add `response_tokens`, `latency_ms`, `cacheable`, `cache_ttl_s` to `_meta` on all tool responses. Agents need this to manage context budget and enable prompt caching (45-80% cost reduction) | 2-4h | no | — | DONE |

### Agent Workflow Features

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 120 | **Code smell catalog (15+ detectors):** Brain Method, Deep Nesting, Long Parameter Lists, Feature Envy, Large Class, Shotgun Surgery, Primitive Obsession, Low Cohesion, DRY Violations, Data Clumps. Per-file code health score 1-10. CodeScene has 25+, we have only cognitive complexity — this is our biggest depth gap | 3-5d | no | — | DONE |
| 121 | **AST pattern matching with `$WILDCARD` metavariables:** structural search/lint on existing tree-sitter ASTs. Integrated into `.roam/rules` YAML engine (`ast_match` type) with `$METAVAR` capture output and `check-rules` custom-rule evaluation support. `roam pattern <expr> [--lang py]` command remains optional follow-up. | 3-5d | no | #93 | **DONE** |
| 122 | **Quality gate enforcement (`roam health --gate`):** configurable pass/fail thresholds in `.roam-gates.yml`. Exit code 5 on failure. Default: health >= 60, complexity < 50. SonarQube's #1 CI feature — table stakes | 0.5d | no | — | DONE |
| 123 | **`roam guard <symbol>` sub-agent preflight:** minimal ~2K token context bundle for Claude Code sub-agents (which can't use MCP — CLI only). Symbol definition + 1-hop callers/callees + test files + risk score + layer violations | 2d | no | — | **DONE** |
| 124 | **`--agent` CLI output mode:** strip decorative text, minimal key:value, <500 tokens for most commands. Critical because Claude Code sub-agents invoke CLI via Bash, not MCP | 2d | no | — | **DONE** |
| 125 | **`roam verify-imports <file>` hallucination firewall:** validate all import/require statements against indexed symbol table. Flag unresolvable imports. Suggest corrections via fuzzy matching. 27.8% of AI suggestions are hallucinated (research data) | 1-2d | no | #51 | **DONE** |

### Multi-Agent Coordination v2

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 126 | **Agent task graph decomposition (`roam agent-plan --agents N`):** decompose `orchestrate` partitions into dependency-ordered tasks with merge sequencing. Output format compatible with Claude Agent Teams | 2-3d | no | #88 | **DONE** |
| 127 | **Per-agent context generation (`roam agent-context --agent-id N`):** generate per-worker instructions with assigned files, interface contracts, read-only dependencies. For Claude Agent Teams / Codex multi-agent | 1d | no | #126 | **DONE** |
| 128 | **Composite difficulty scoring for partitions:** combine complexity(0.3) + coupling(0.25) + churn(0.25) + size(0.2) into per-task work estimate. Research: doubling task duration quadruples failure rate | 1d | no | #88 | **DONE** |

### Discovery & Onboarding

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 129 | **Expand MCP Resources to 8-10:** add `roam://architecture`, `roam://hotspots`, `roam://tech-stack`, `roam://dead-code`, `roam://recent-changes` beyond existing health/summary. Resources auto-populate Claude context | 1d | no | — | **DONE** |
| 130 | **`roam mcp setup <platform>` config generator:** output platform-specific MCP config for Claude Code, Cursor, Windsurf, VS Code, Gemini CLI, Codex CLI. Single highest-friction point for new users | 1d | no | — | DONE |

### Scoring & Competitive Fairness

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 131 | **`roam vulns` — vulnerability scanning integration:** wrap `pip audit`/`npm audit`/`trivy`/OSV API to scan dependencies for known CVEs. Infrastructure exists (`vuln_store.py` ingestion, `vuln_reach.py` reachability). Need CLI command that invokes scanners, parses output, stores advisories, reports reachable vulns. `--sarif` output. Flips `vuln_scanning` criterion (+3pts) | 1-2d | no | — | **DONE** |
| 132 | **Documentation quality improvement:** getting-started tutorial, command reference with examples, architecture diagram. Existing docs site (`docs/site/`) + CLAUDE.md + llms-install.md. Target: match SonarQube/CodeQL documentation depth. Flips `documentation_quality` 1→2 (+1pt) | 1-2d | no | — | **DONE** |
| 133 | **`roam secrets` semantic + remediation upgrade:** (a) test-file/fixture/docs suppression — skip findings in `test_*`, `*_test.*`, `fixtures/`, `docs/` paths, (b) env-var assignment detection — suppress when value comes from `os.environ`/`process.env`/`config.get()`, (c) Shannon entropy detector — flag high-entropy strings (>4.5 bits/char) in assignment contexts even without matching a known regex pattern, (d) per-finding remediation — specific fix suggestion per pattern type (e.g., AWS key → "Use `os.environ['AWS_ACCESS_KEY_ID']` or AWS Secrets Manager", DB connection string → "Use connection pool with env-var DSN"). Upgrades `secret_detection` from "regex" to "remediation" (+2pts). Reduces false positives and provides actionable fixes — SonarQube's full secret workflow | 1d | no | #44 (DONE) | **DONE** |

### Competitive Parity Features (SonarQube / CodeScene / Semgrep gap closure)

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 134 | **Coverage report ingestion (`coverage-gaps --import-report <file>`):** parse lcov.info / Cobertura XML / coverage.py JSON, map file:line ranges to symbols in `symbols` table, store `coverage_pct` per file/symbol. Cross-reference with graph: "this high-complexity, high-centrality symbol has 0% coverage" as compound risk signal. Integrates into `health` scoring and enriches `test-gaps` with actual vs predicted data. SonarQube's `search_files_by_coverage` / `get_file_coverage_details` equivalent | 2-3d | no | — | **DONE** |
| 135 | **Security hotspot classification (`roam hotspots --security`):** detect calls to dangerous APIs across languages — `eval`, `exec`, `os.system`, `subprocess.run`, `sql.execute`, `pickle.loads`, `dangerouslySetInnerHTML`, `innerHTML`, `crypto.createCipher` (weak), `child_process.exec`, `yaml.load` (unsafe). ~50-100 patterns across Python/JS/Go/Java/Ruby. Cross-reference with entry point reachability from call graph. Not bugs — review checkpoints. SonarQube's `search_security_hotspots` equivalent. Distinct from `roam secrets` (credentials) and `roam adversarial` (attack surface) | 2-3d | no | — | **DONE** |
| 136 | **Community rule pack targeting 100+ rules:** combine existing 10 builtin rules + 23 algo detectors + #120 code smell detectors (25+) + new security/style rules to break the 100-rule threshold. Security rules: no-eval, no-exec, SQL injection patterns, XSS patterns, insecure deserialization, SSRF patterns. Style rules: max function length, max file length, max parameters, naming conventions. Ship as `rules/` directory with YAML definitions consumable by `check-rules` engine. Flips `rule_count` from 0/3 to 1/3 (+1pt). Semgrep has 3,500+, SonarQube has 6,500+ — 100 is the minimum credible number | 3-5d | no | #93 (DONE), #120, #121 | **DONE** |
| 137 | **Unified `roam metrics <file\|symbol>` command:** consolidate all per-file/per-symbol metrics into single structured output — complexity, fan-in, fan-out, PageRank, churn, co-change count, coverage %, smell count, test file count, layer depth, dead code risk, AI ratio estimate. All data already exists in SQLite. SonarQube's `get_component_measures` equivalent. Enables agents to get a complete "vital signs" snapshot in one call without composing 5+ commands | 1-2d | no | — | **DONE** |
| 138 | **Quality rule profiles with inheritance:** named profiles (e.g., `strict-security`, `ai-code-review`, `legacy-maintenance`) that bundle specific rule sets with configured thresholds. Profile inheritance via `extends:` keyword in `.roam-rules.yml`. Ship 3-5 built-in profiles. SonarQube's Quality Profile management equivalent. Enables per-project rule customization without maintaining separate YAML files | 1-2d | no | #93 (DONE) | **DONE** |
| 139 | **Trend cohort analysis (`roam trends --cohort-by-author`):** compare metric trajectories of AI-authored vs human-authored code using git blame attribution + `ai-ratio` signals. Slope/velocity of degradation per cohort, percentile ranking across codebase, time-series visualization via sparklines. CodeScene's behavioral trend analysis gap. Data already in `metric_snapshots` + blame tables — pure SQL + Python aggregation | 2-3d | no | #81 (DONE), #86 (DONE) | **DONE** |

**Epic outcome:** MCP spec conformance, 15+ code smell detectors, AST pattern matching, quality gates, agent-optimized output modes, multi-agent task decomposition, vulnerability scanning, documentation parity, coverage integration, security hotspots, 100+ rules, unified metrics, quality profiles, trend cohorts. Closes all architecturally-feasible competitive gaps.

**Research basis:** MCP-Atlas benchmark (62.3% multi-tool success), Tool Smells paper (97.1% smell rate), ContextBench bitter lesson, Cursor production data (hierarchy > equal-status agents), CodeScene 25+ code smell catalog, ast-grep structural matching, SonarQube quality gates. See `reports/research_*.md` for full evidence.

---

## Epic 15: Competitive Gap Closure (NEW — Feb 24 Competitive Analysis)

> WHY: CKB v8.1.0 shipped `findCycles`, `suggestRefactorings`, `planRefactor` — directly copying our feature categories.
> SonarQube MCP shipped 7 new tools in v1.10.0 (Feb 17). grepai shipped 9 releases in Feb with 1.3k stars.
> We have all the underlying data (debt scores, complexity, coupling, churn, coverage) but lack the compound
> recommendation/planning commands that competitors are now shipping. These items close every architecturally-feasible
> competitive gap — leaving no moat on the table.
>
> **Scoring impact:** #142 moved `dataflow_taint` to `intra` (+1 point). #145 raised rule depth above 500 rules but does not change scoring tier until 1000+.
> **Trigger:** Feb 24, 2026 competitive deep-dive (16 competitors, 200+ sources, fresh web verification).

### Proactive Refactoring Intelligence (CKB parity)

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 140 | **`roam suggest-refactoring`** — proactive refactoring recommendation engine. Combine debt score (#70), cognitive complexity, coupling (fan-in/fan-out), churn velocity, smell count, and coverage gaps into a ranked actionable list. Output: top-N symbols needing refactoring with reason, estimated effort (S/M/L), and suggested action (extract, simplify, split, decouple). CKB v8.1.0 shipped `suggestRefactorings` on Feb 1 — we have all the signals in SQLite, just need composition + ranking. MCP tool: `roam_suggest_refactoring`. JSON envelope with `verdict` | 2-3d | no | #70 (DONE), #71 (DONE), #120 (DONE) | **DONE** |
| 141 | **`roam plan-refactor <symbol>`** — compound refactoring plan for a specific symbol. Combines: `simulate move` impact prediction, blast radius (callers/callees), test gap analysis, layer violation check, risk score, and produces an ordered step-by-step refactoring plan with pre/post metrics. CKB v8.1.0 shipped `planRefactor` combining risk + impact + test gaps + ordered steps. Our `simulate`, `impact`, `test-gaps`, `guard` already compute each piece — this command composes them. MCP tool: `roam_plan_refactor` | 2-3d | no | #123 (DONE) | **DONE** |

### Static Analysis Depth (Scoring Gap Closure)

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 142 | **Basic intra-procedural dataflow analysis** — detect dead assignments (variable assigned but never read in same function), unused parameters, and simple source-to-sink patterns (user input → dangerous API in same function body) via tree-sitter AST walking. NOT a full dataflow engine — a pragmatic subset using def-use chain analysis within function scope. Moves `dataflow_taint` scoring criterion from "none" (0/4) to "intra" (1/4) = **+1 competitive point**. SonarQube and CodeQL have full dataflow; this gives us a credible entry in the category. Integrates into `check-rules` as `dataflow_match` rule type and enriches `dead` command with unused-assignment findings | 5-7d | no | #121 (DONE) | **DONE** |

### Documentation Intelligence (CKB parity)

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 143 | **`roam docs-coverage`** — docstring/comment coverage analysis + staleness detection. Tree-sitter extracts docstrings/comments for all 26 languages; cross-reference with `symbols` table to compute: (a) % of public symbols with docstrings, (b) stale docs where symbol signature changed after last docstring edit (via git blame), (c) missing-docs hotlist ranked by PageRank (most-imported undocumented symbols first). CKB has `docs stale` and `docs coverage`; we can do it better with graph-weighted prioritization. MCP tool: `roam_docs_coverage`. `--threshold N` gate support | 2-3d | no | — | **DONE** |

### Debt Quantification (CodeScene parity)

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 144 | **Refactoring ROI estimation in `roam debt`** — add `--roi` flag that estimates developer-hours saved from fixing top debt items. Formula: `savings = complexity_reduction * touch_frequency * avg_review_overhead`. Uses churn data (how often the file is modified), complexity metrics (how much simpler it would be), and coupling data (how many files are co-changed). Outputs "fixing X saves ~Y hours/quarter" with confidence band. CodeScene's "refactoring business case" is a premium feature — we make it free. Extends existing `roam debt` command, no new CLI entry needed | 1-2d | no | #70 (DONE) | **DONE** |

### Rule Pack Depth (Semgrep/SonarQube parity)

| # | Item | Effort | v11? | Depends On | Status |
|---|------|--------|------|------------|--------|
| 145 | **Expand rule packs to 500+ rules targeting 1000+** — add language-specific security rules for Go (30+), Java (50+), Ruby (30+), PHP (30+), C# (30+), TypeScript (40+), Rust (20+). Add performance rules (N+1 detection patterns, excessive allocation, blocking I/O in async). Add accessibility rules (missing alt text, missing ARIA). Add API design rules (inconsistent naming, missing versioning). Current count: 602 rules (554 community + 10 builtin + 15 smells + 23 algo). Target hit: 500+ minimum. At 1000+ rules, `rule_count` scoring moves from tier 1 (1/3) to tier 2 (2/3) = **+1 competitive point**. Semgrep has 3,500+, SonarQube has 6,500+ — 1000 remains the next depth milestone | 3-5d | no | #136 (DONE) | **DONE** |

**Epic outcome:** CKB parity on refactoring intelligence is shipped (`#140`, `#141`), CodeScene parity on ROI quantification is shipped (`#144`), basic dataflow baseline is shipped (`#142`, +1 scoring point), and rule-pack depth is now above 500 (`#145` done). Next tier lift requires crossing 1000+ rules.

**Scoring data fixes applied in prior sessions (no code needed):**
- `structural_pattern_matching`: `False` → `True` (+3 pts) — #121 AST patterns + #136 rule-pack foundation shipped
- `rule_count`: `20` → `602` (+1 pt, tier unchanged until 1000+) — 554 community + 10 builtin + 15 smells + 23 algo
- `documentation_quality`: `1` → `2` (+1 pt) — #132 docs site with tutorials, command ref, architecture already shipped

**Competitive intelligence that triggered this epic:**
- CKB v8.1.0 (Feb 1): `findCycles`, `suggestRefactorings`, `planRefactor`, `prepareChange (extract)` — directly tracking our features
- SonarQube MCP v1.10.0 (Feb 17): 7 new tools (duplications, coverage, security hotspots), token optimization
- grepai: 9 releases in Feb, 1.3k stars, Reciprocal Rank Fusion, semantic search growing fast
- CodeGraphMCPServer: dormant since Dec 2025 — no longer a threat
- Context7: 46.7k stars proves demand for framework knowledge packs (validates #96)

---

## Someday/Maybe (park, revisit quarterly)

These were evaluated and deliberately deferred. Not killed — just not now.
Items marked **↑ SIGNAL STRENGTHENING** have new research evidence and should be re-evaluated next quarter.

| Item | Why Deferred | Feb 2026 Research Update |
|------|-------------|--------------------------|
| SBOM generation (CycloneDX/SPDX) | Enterprise feature; not core value; large multi-phase effort | **↑ SIGNAL STRENGTHENING** — EU CRA Sep 2026 deadline, CISA 2025 SBOM standards. SonarQube 2026.1 added SCA/SBOM. Enriched SBOM with reachability status is a differentiator no other tool offers. Consider promoting next quarter. |
| Taint/data flow analysis | CodeQL/Semgrep years ahead; large multi-phase effort for inferior result | Unchanged |
| Multi-repo federation | Enterprise need; CKB owns this; massive scope | Unchanged |
| ~~Near-duplicate code detector~~ | ~~SonarQube does it better; not differentiator~~ | **PROMOTED** to Epic 10 #87 as *semantic* duplicate detector. AI code produces functionally-equivalent clones with divergent edge cases that SonarQube's textual detection misses. FSE 2025 paper validates. |
| ADR intelligence | Niche; no user demand signal | **↑ SIGNAL STRENGTHENING** — AWS, Google, Microsoft, Backstage all publishing ADR guidance. Growing adoption. Keep parked but note. |
| ~~Monorepo analysis (Nx/Turborepo/Bazel)~~ | ~~Wait for user demand~~ | **PROMOTED** to Epic 12 #89 as `roam affected`. Strong market signal: DPE Summit, AI context window problem at scale, CI optimization demand. |
| Web UI for graph exploration | High effort, low ROI vs CLI/MCP | Unchanged. MCP Apps (2025-11-25 revision) could enable interactive visualizations rendered inline in Claude/ChatGPT — revisit when MCP Apps adoption grows. |
| Agent session management | Serena has memories; agents handle this themselves | AiDex MCP server has session persistence concept (notes + task backlog across sessions). Interesting but agents are evolving fast. Keep parked. |
| Cost-of-change in dollars | CodeScene premium feature; hard to get right | Unchanged |
| Developer congestion metrics | Interesting but niche | Unchanged |
| Doc-symbol linking | CKB feature; no user asked for it | Unchanged |
| rustworkx replacement | Premature; NetworkX fine up to 50k nodes | Unchanged. Leiden algorithm (#73 in Someday section of Epic 2) is a lighter alternative to explore first. |
| Named snapshot save/diff | Niche; fingerprinting already exists | Unchanged |
| Color output with NO_COLOR support | Polish; low impact | Unchanged |
| Compact JSON for pipes | Edge case | Unchanged |
| All language additions (Zig, Dart, Elixir, Scala, Gleam, Lua, R, Mojo) | Demand-driven; community can contribute | Unchanged |
| All framework extractors (React, Django, Spring, Rails, Terraform) | Same — wait for demand | Unchanged |
| All CI platforms beyond GitHub (GitLab, Azure, Bitbucket, CircleCI, Jenkins, Helm) | GitHub first; expand on demand | Unchanged |
| JetBrains plugin | After VS Code proves the model | Unchanged |
| SLSA provenance + Sigstore | Enterprise hardening; later | Unchanged |
| Feature flag dead code detection | Common flags (LaunchDarkly, Unleash, custom `isFeatureEnabled()`) create conditionally-dead code standard linters miss | **NEW** — added from developer pain points research. 2-3d effort. Low priority. |
| ~~`roam endpoints` — list all detected REST/GraphQL/gRPC endpoints with handlers~~ | ~~REST bridge exists but no CLI surface.~~ | **PROMOTED** to Epic 13 #113. Atlassian: "finding services/APIs" is #1 friction point. Leverages existing `bridge_rest_api.py`. |
| A2A Agent Card for roam-code | Google Agent2Agent protocol (v0.3, Linux Foundation). Complementary to MCP (agent-to-agent vs agent-to-tool). | **NEW** — Wait for A2A adoption to reach critical mass. |
| `roam compliance` — audit-ready report mapped to CRA/PCI DSS | Depends on SBOM generation. Enterprise need growing. | **NEW** — 2-3d on top of SBOM. |
| #59 Dedicated docs site (Starlight/MkDocs) | Agents read AGENTS.md and MCP tool descriptions, not docs sites. Human adoption artifact only. | **MOVED from Epic 11** — agents-only pivot. Revisit if human-facing marketing becomes priority. |
| #62 VS Code extension (LSP-based) | Agents in VS Code use MCP tools, not LSP extensions. IDE features (hover, go-to-def) are human-only. | **MOVED from Epic 11** — agents-only pivot. Revisit if agent-IDE integration model changes. |

---

## Killed Items (47+ permanently removed)

Evaluated across 7 reports. Grouped by reason:

**Wrong layer / not our job (6):**
- AI hallucinated-reference detector — agents handle this themselves
- AI-generated code pattern detector — replaced by Vibe Code Auditor (#57)
- Rollback guidance for agents — agents have their own undo
- Agent session management — agents manage their own sessions
- Interactive `roam init` — unnecessary ceremony; `roam init` should just work
- Command namespace consolidation — too disruptive for 0 user complaints

**Not a product feature (7):**
- Counter-messaging for context windows — strategy doc, not code
- Recruit maintainers — outcome of growth, not a backlog item
- Multiple positioning content pieces — do one well, not five
- Air-gapped landing page — niche; no signal
- Evaluate CLI rename from `roam` — disruption > benefit
- Video content creation — text-first community; video later
- Product Hunt launch — after channel-agnostic launch messaging is validated

**Premature / too early (5):**
- Web playground/hosted demo — no demand; massive effort
- Rust/Go binary distribution — Python + pipx is fine
- Shared fitness functions community hub — no community yet
- Salesforce/Apex case studies — too niche
- VFP legacy case studies — too niche

**Low-value polish (5):**
- Color output with NO_COLOR — minimal impact
- Compact JSON for pipes — edge case
- Document alias commands — nobody asked
- Subcommand consistency — internal housekeeping
- Validate empty command arguments — defensive; low impact

**Agents-only pivot (4) — killed Feb 2026:**
- #46 Fuzzy command matching with typo suggestions — agents use MCP tools with exact names, never type CLI commands
- #47 Usage examples in every command help text — agents use MCP tool descriptions, not `--help`
- #49 "5 core commands" framing in `--help` — agents use MCP presets, never see `--help`
- #53 Windows PATH issue auto-detection — MCP is in-process via CliRunner, PATH is irrelevant

**Absorbed into someday/maybe bundles (24+):**
- 8 language additions (Zig, Dart, Elixir, Scala, Gleam, Lua, R, Mojo) — demand-driven
- 5 framework extractors (React, Django, Spring, Rails, Terraform) — demand-driven
- 6 CI platforms (GitLab, Azure, Bitbucket, CircleCI, Jenkins, Helm) — GitHub first
- JetBrains plugin — after VS Code
- Multi-repo federation — enterprise; CKB territory
- SLSA provenance — enterprise hardening
- Parallelize file processing — premature optimization
- `schema_meta` table — over-engineering for now

---

## Summary Stats (Live Snapshot — 24 Feb 2026, Session 34 — demo GIF + OSS benchmark harness)

| Metric | Value | Notes |
|--------|-------|-------|
| Numbered backlog items | **145** | IDs `#1-#145` (6 added in competitive gap analysis) |
| Shipped items | **134** | Sessions 1-34 (counted from epic tables) |
| Killed items | **4** | `#46`, `#47`, `#49`, `#53` (agents-only pivot) |
| Moved to Someday/Maybe | **2** | `#59`, `#62` |
| **Open items** | **5** | See [Open Items at a Glance](#open-items-at-a-glance-5-remaining) |
| Deferred | **1** | `#32` (community launch, non-blocking) |
| v11 remaining | **3** | `#24`, `#29`, `#31` (external actions) |
| Competitive score | **84/100** | Was 79; +4 from stale scoring data fixes plus +1 from `dataflow_taint=intra` (#142). `rule_count` is now 602 (#145) but still in 100-999 tier. |
| CLI commands | **136 canonical** | +1 legacy alias `math` = 137 invokable |
| MCP tools | **101** | 23 in core preset |
| MCP resources | **10** | Up from 2 in v11.0.0 |
| MCP prompts | **5** | onboard, review, debug, refactor, health-check |
| Test files | **~130** | 4889 tests, all green |
| Completed epics | **9** | Epic 2, 6, 7, 8, 9, 10, 11, 12, 13 fully done |

### Shipped by session
| Session | Items | Key deliverables |
|---------|-------|------------------|
| 1-2 | Epic 1 (#1-#6), Epic 2 (#11-#15) | MCP v2, Performance foundations |
| 3 | #19-#30, #38-#44, #57, #65-#68, #76-#77, #80-#92, #97-#103 | CI/CD, Ownership, Change intel, AI debt, Multi-agent |
| 4 | #7, #9-#10, #45, #48, #50-#52, #61, #78, #105, #110-#115 | Progressive disclosure, Batch MCP, Error recovery, Endpoints |
| 5 | #55, #60, #72-#73, #79, #93 | Watch, Search explain, Spectral, Supply-chain, Check-rules |
| 6 | #116-#120, #122, #130 | MCP protocol compliance, Smells, Quality gates, MCP-setup |
| 7 | #125, #128-#129, #131, #133, #137-#138 | Verify-imports, Vulns, Metrics, Difficulty scoring, Profiles, MCP resources |
| 9 | #121 | AST pattern matching + custom-rule integration in check-rules |
| 10 | #136 | Community rule pack (169 YAML rules) + recursive loader + style requirement checks |
| 11 | #132 | Docs quality uplift: getting-started tutorial, command reference, architecture diagram |
| 12 | #139 | Trends cohort mode: AI vs human quality trajectory analysis with velocity + sparkline |
| 13 | #104, #135 | Runtime ranking v2 for `algo` (OTel DB semantics) + `hotspots --security` security hotspot classification |
| 14 | #22, #124 | Alpine-based Docker image packaging + global `--agent` compact CLI mode |
| 15 | #70, #71 | SNA metric vector + composite debt score, plus comprehension difficulty metrics in `roam metrics` |
| 16 | #63, #64 | Kotlin + Swift promoted to Tier 1 via dedicated extractors and parser-quality tests |
| 17 | #114 | Plugin/extension discovery for commands, detectors, and language extractors |
| 18 | #134 | Coverage report ingestion (LCOV/Cobertura/coverage.py JSON) + integration into `health`, `metrics`, and `test-gaps` |
| 19 | #69 | Clean Python embedding API (`roam.api`) with in-process JSON command execution client |
| 20 | #123 | `roam guard <symbol>` compact sub-agent preflight bundle with risk/layer/test context |
| 21 | #126, #127 | Multi-agent v2: `agent-plan` task graph decomposition + `agent-context` per-worker context bundles |
| 22 | #8, #67 | MCP Tasks+Elicitation completion: `roam_init` + `roam_reindex` async task-mode indexing with force confirmation |
| 23 | #95 | Daemon + webhook bridge: `roam watch` now supports authenticated webhook-triggered reindex and webhook-only daemon mode |
| 24 | #54 | Hybrid semantic search v2: fused BM25 lexical ranking + TF-IDF vector ranking (RRF) with deterministic score blending |
| 25 | #96 | Pre-indexed framework/library semantic packs: cold-start retrieval for common stack intents (Django/Flask/FastAPI/React/Express/SQLAlchemy/pytest/stdlib) |
| 26 | #144 | `roam debt --roi`: refactoring ROI estimate (developer-hours saved per quarter/year) with confidence bands |
| 27 | #143 | `roam docs-coverage`: exported-symbol docs coverage + stale-doc drift + PageRank missing-doc hotlist with threshold gate |
| 28 | #140, #141 | `roam suggest-refactoring` + `roam plan-refactor`: proactive recommendations and ordered per-symbol refactor planning with MCP parity |
| 29 | #142 | Basic intra-procedural dataflow baseline: `dataflow_match` rule type + `roam dead` unused-assignment signal |
| 30 | #33 | Integration tutorials page for Claude/Cursor/Gemini/Codex/Amp with docs-site nav wiring and docs quality test coverage |
| 31 | #34, #145 | Benchmark publish artifact + 500+ community rule-pack expansion (602 total rules including builtin/smells/algo) |
| 32 | #35, #56 | Comparative benchmark slice published (`codex` `cpp-calculator` `vanilla` vs `roam-cli`) + optional local ONNX semantic backend in Search v2 |
| 33 | #58 | Continuous Architecture Guardian: `watch --guardian` snapshots, `report guardian` preset, and scheduled CI artifact workflow |
| 34 | #26 (+ #37 progress) | Terminal demo GIF shipped in README with deterministic generator; OSS benchmark harness + manifest + latest local snapshot artifacts published |

### Product surface (current)
| What | Count | Source of truth |
|------|-------|-----------------|
| CLI commands (canonical) | 136 | `_COMMANDS` dict in `cli.py` |
| CLI commands (invokable) | 137 | +1 legacy alias `math` → `algo` |
| MCP tools | 101 | `@_tool(` decorators in `mcp_server.py` |
| MCP resources | 10 | `@mcp.resource(` in `mcp_server.py` |
| MCP prompts | 5 | `@mcp.prompt(` in `mcp_server.py` |
| Core preset tools | 23 | 16 original + 4 compounds + 2 batch + expand_toolset |
| Languages (Tier 1) | 26 | `registry.py` |
| Test files | ~130 | `tests/test_*.py` |

---

## Smart Execution Layer (De-Generalized Backlog)

To keep this backlog execution-grade (not idea-grade), every active item should be judged with binary acceptance criteria.

### 1) Backlog Quality Rules (apply to all new/edited items)

- Must define `done_when` in one sentence with measurable output.
- Must define at least one `verification_artifact` (PR link, screenshot, benchmark JSON, or command output path).
- Must define one `non_goal` to prevent scope creep.
- Must avoid subjective language (`better`, `smarter`, `magical`, `state-of-the-art`) unless paired with a metric.
- Must include explicit dependency IDs when blocked by another item.

### 2) Concrete Acceptance Criteria for Remaining v11 Items (+ Deferred `#32`)

| Item | done_when (binary) | verification_artifact | non_goal |
|------|--------------------|-----------------------|----------|
| `#106` README overhaul (**DONE**) | All command tables include every registered CLI command; MCP tool count and list match mcp_server.py; ASCII diagram shows correct count; comparison table uses real numbers | `README.md` + `tests/test_readme_surface_consistency.py` + `tests/test_surface_counts.py` | Rewriting README prose or restructuring sections |
| `#107` CHANGELOG completeness (**DONE**) | [Unreleased] section lists every item shipped since v11.0.0 with correct backlog IDs | `CHANGELOG.md` + `tests/test_changelog_unreleased.py` | Retroactive changelog for pre-v11 items |
| `#108` Command count (**DONE**) | Verified count from `_COMMANDS` dict documented; all references (cli.py, README, CLAUDE.md, llms-install.md, launch copy) now use the verified number and explicitly document alias handling | `src/roam/surface_counts.py` + `tests/test_surface_counts.py` + updated copy in docs | Counting aliases or hidden commands as separate |
| `#109` v11 narrative (**DONE**) | README has a "What's New" section covering MCP v2 (92% token reduction, compounds, presets), performance (1000x search, O(changed)), and CI integration | `README.md` + `tests/test_readme_surface_consistency.py::test_readme_has_v11_narrative_section` | Marketing copy or blog-style prose |
| `#24` Repo topics | Repo has at least 10 relevant topics set and visible publicly | GitHub repo settings screenshot + list in release notes | SEO/blog optimization beyond topic tags |
| `#26` Demo GIF (**DONE**) | README includes one GIF showing `index -> context -> verify` flow in <=30s | `docs/assets/roam-terminal-demo.gif` + README "Terminal demo" section + `tests/test_demo_gif_asset.py` | Full video/course production |
| `#29` Discussions | Discussions enabled with at least 3 categories (`Q&A`, `Ideas`, `Showcase`) | Discussion categories screenshot | Community moderation automation |
| `#31` MCP listings | roam is submitted/listed on target MCP directories + awesome lists from item text, and each entry has `last_verified` date (Registry is preview/reset-prone) | Tracking checklist with live URLs + submission/listing dates + last-verified column | Paid promotion campaigns |
| `#32` Community launch note (DEFERRED) | One channel-agnostic launch note is published post-v11 with a linked proof artifact (GIF/benchmark), but this item does not block v11 | Link to post + linked artifact | Multi-channel campaign requirement |

### 3) Concrete Acceptance Criteria for Next Post-v11 Phase

| Item | done_when (binary) | verification_artifact | non_goal |
|------|--------------------|-----------------------|----------|
| `#23` Inline PR comments (**DONE**) | CI job now posts/updates one sticky marker-managed PR comment idempotently and cleans up duplicate sticky comments | `.github/scripts/pr-comment.js` + `tests/test_pr_comment_script.py` | Rich threaded reviewer bot |
| `#69` Python API (**DONE**) | Stable importable module API documented with examples and tests | `src/roam/api.py` + `tests/test_library_api.py` | Full SDK for all languages |
| `#74` Trend-aware gates | Gate can fail/pass on trend slope, not only static threshold | Fixture snapshots + gate test cases | Predictive ML forecasting |
| `#75` Changed-only mode | CI runtime improves on representative repo while preserving result parity | Before/after timing + parity report | Full monorepo build orchestration |
| `#105` SARIF hardening (**DONE**) | Action now exports per-command SARIF set, merges with run/result/size guardrails, uses configurable category, and warns when truncation occurs | `action.yml` + `.github/scripts/sarif_guard.py` + `tests/test_ci_sarif_guard.py` | Replacing GitHub code scanning with custom UI |
| `#93` Rule packs/autofix | Ships baseline relational rule pack and optional autofix templates | Rule pack files + rule tests | Full ast-grep compatibility layer |
| `#94` Personalized ranking (**DONE**) | Context ranking now uses task/session signals in `roam context` + MCP wrappers and emits deterministic `score`/`rank` fields | `tests/test_commands_workflow.py` + `tests/test_mcp_server.py` passing runs | User profiling or telemetry collection |
| `#95` Daemon/webhooks (**DONE**) | Merge/push trigger refresh path updates analysis cache without full reindex | `tests/test_watch.py` webhook bridge tests + `roam watch --webhook-*` help/output | Always-on background service on all OSes |
| `#96` Pre-index packs | At least 3 framework/library packs ship with opt-in enablement | Pack definitions + retrieval benchmark | Exhaustive package ecosystem coverage |
| `#97` Smart export targeting | `agent-export` supports canonical `AGENTS.md` baseline + provider-specific overlays selected by profile | CLI help/docs + snapshot tests per profile | Maintaining vendor-specific proprietary formats beyond public docs |
| `#98` Streamable HTTP transport | `roam mcp --transport streamable-http` passes protocol smoke tests and client interop checks | MCP transport integration tests + demo transcript | Replacing `stdio` as default transport |
| `#99` MCP metadata completeness | Tool catalog ships policy annotations + `taskSupport` for long jobs with backward compatibility | `--list-tools` JSON snapshot + compatibility tests | Manual per-session tool curation |
| `#100` Client conformance suite | Automated checks validate tools-only fallback, AGENTS precedence, provider file loading behavior, and remote-auth capability reporting per client profile | Client-profile matrix test output | Supporting every niche MCP client variant |
| `#50` Error remediation (**DONE**) | All error messages include actionable next step (e.g., "run `roam index` first") | Before/after error message screenshots | Rewriting all error handling |
| `#51` Symbol-not-found suggestions (**DONE**) | Missing symbol triggers FTS5 fuzzy search, shows top 3 candidates | Test case with misspelled symbol | Full autocomplete/completion engine |
| `#48` `roam doctor` (**DONE**) | Checks Python version, tree-sitter, git, index freshness, disk space; outputs PASS/FAIL per check | `roam doctor` output on clean + broken install | Full system health monitoring |
| `#110` CI consolidation (**DONE**) | Single workflow or clearly separated test vs analysis workflows | Workflow file diff | Rewriting entire CI pipeline |
| `#111` PyPI keywords (**DONE**) | pyproject.toml has keywords list, Documentation URL, expanded classifiers | `pyproject.toml` diff | PyPI marketing optimization |
| `#112` README Roadmap (**DONE**) | All completed items marked `[x]`, v11 features listed, stale items removed | `README.md` + `tests/test_readme_surface_consistency.py::test_readme_roadmap_refreshed_for_v11_state` | Full roadmap strategy document |
| `#113` `roam endpoints` (**DONE**) | CLI command lists REST/GraphQL/gRPC endpoints with handler function + file:line | Command output on test project with endpoints | Full API documentation generation |

### 4) Generality Fixes Applied in This Pass

- Removed single-vendor framing around `CLAUDE.md`; shifted to canonical `AGENTS.md` + provider overlays (`#65`, `#68`, `#97`).
- Converted summary metrics from stale historical text to live snapshot values.
- Converted v11 execution plan to remaining-only work with explicit IDs.
- Added competitor/protocol-derived items with concrete scope (`#93-#100`) instead of broad “study/adopt” notes.
- Converted execution wording to phase-based sequencing instead of calendar-window planning.

---

## Quick-Win Chains (compound impact)

### Chain A0: Documentation Crisis (P-CRITICAL, 1-2 days) — NEW v7
```
#108✓ command count reconciliation (1-2h) → #106✓ README accuracy overhaul (4-8h)
→ #107✓ CHANGELOG completeness (2-4h) → #109✓ v11 narrative (2-4h)
→ #112✓ README Roadmap refresh (1h)
```
**Result:** Public docs match reality. 40% product undersell eliminated. External users now see the real product. **MUST complete before #31 MCP directory submissions and any optional community launch note (`#32`).**

### Chain A: Launch Prep Phase (P0, now mostly external)
```
#26✓ GIF (Session 34) + #24 topics (10m) + #29 Discussions (30m) → #31 MCP listings
```
**Result:** Core launch asset (demo GIF) is shipped; remaining launch closeout is external platform execution.

### Chain B: DB Speed Phase (P-completed, 0.5 day) — DONE
```
#11 mmap (1h) → #12 propagation guard (1h) → #15 indexes + UPSERT + batch (4h)
+ #13 O(changed) incremental fix + #14 FTS5/BM25
```
**Result:** Everything feels snappier; pairs with FTS5. **Shipped in commit 8cdad19.**

### Chain C: Discoverability Blitz (P0, 6h10m) — URGENT
```
#24 topics (10m) → #31 MCP directories + awesome-lists (2h) → #76 comparison table (4h)
```
**Result:** 10+ discovery channels; competitive positioning; free organic traffic.

### Chain D: MCP Token Emergency (historical bundle) — DONE
```
#5 shorten descriptions (3h) → #3 presets (after #1) → #6 expand_toolset (3h)
+ #1 in-process → #2 compound ops → #4 schemas
```
**Result:** 36K tokens → <3K immediately. **Shipped in commits 0148c5f + 485c22d.**

### Chain E: Agent Error Recovery MVP — ALL DONE
```
#50✓ remediation in errors → #51✓ symbol-not-found suggestions → #48✓ roam doctor
→ #45✓ next-step suggestions → #52✓ roam reset/clean
```
**Full chain shipped.** Agents self-recover from errors, get guided next steps, and can diagnose/reset their own index state.

### Chain F: MCP Agent Compat Phase (P2, 1 day) — NEW
```
#66 defer_loading (0.5d) → #68 agent summary export (2-3d) → #9 budget flag (2d)
```
**Result:** roam-code works optimally with Claude Code Tool Search, generates AGENTS.md automatically, and supports token-budget-aware context retrieval. Zero-to-hero for agent integration.

### Chain G: Vibe Code Auditor MVP (P3, medium block) — NEW
```
#57 vibe-check 8-pattern detection (5-7d) → #84 AI Readiness Score (2-3d) → #85 verify command (3-5d)
```
**Result:** Hero feature for blog content and broader launch narratives. Addresses the hottest topic in dev tools.

### Chain I: Agent Optimization Phase (P2, 3 days) — NEW v6
```
#90 deterministic output (1-2d) → #91 PageRank truncation (1-2d) → #9 budget flag (2d)
```
**Result:** roam output is 100% prompt-cache-friendly, agents get smart truncation at budget limits. Marketable: "optimized for LLM context caching."

### Chain J: Multi-Agent Judge Phase (P2, 2 days) — NEW v6
```
#92 syntax integrity (1-2d) → #88 partition manifest (3-5d)
```
**Result:** roam becomes the Judge layer for multi-agent coding. Worker agents write code, roam validates syntax + blast radius.

### Chain H: Graph Intelligence Upgrade (P4, deep R&D block) — NEW
```
#70 SNA metrics (5d) → #71 comprehension difficulty (5d) → #72 bottom-up context propagation (5d)  **DONE (Session 15)**
```
**Result:** State-of-the-art graph analysis validated by academic research. Unique differentiator no competitor can match.

---

## Critical Path Dependencies

```
Epic 1 (MCP v2):      #1✓ → #2✓ → #3✓ → #4✓,#5✓,#6✓ → #66✓ defer_loading → #31 (MCP listings)
Epic 3 (CI/CD):       #19✓ → #20✓ → #75✓ → #74✓ → #23✓
Epic 4 (Launch):      #108✓ cmd count → #106✓ README → #107✓ CHANGELOG → #109✓ v11 narrative
                      + #24,#29 parallel → #112✓ roadmap refresh → #26✓ GIF → #31
Epic 5 (Growth):      Epic 4 + #106-#109 → #35✓ (+ optional #32 post-v11) → #37
Epic 6 (Ownership):   #38✓ → #39✓ → #40✓,#41✓ — ALL DONE
Epic 8 (Error Recov): #50✓ remediation → #51✓ symbol-not-found → #48✓ doctor → #45✓ next-step → #52✓ reset — ALL DONE
Epic 9 (Search v2):   #14✓ → #54✓ + #96✓ → #56✓
Epic 10 (AI Debt):    #57✓ → #84✓,#85✓,#87✓ → #58
Epic 12 (Multi-Agent): #92✓ → #88✓; #89✓ standalone — ALL DONE
Epic 13 (Infra):      #110,#111 parallel (quick) → #114 (later)
```

**v11 remaining execution plan:**
```
COMPLETED PHASES:
  Phase -1 (documentation crisis): ALL DONE (#106-#109, #112)
  Phase 0.5 (agent retention): ALL DONE (#50, #51, #52)
  Phase 0 partial: #110✓ CI consolidation, #111✓ PyPI discoverability
  Phase 2 partial: #7✓ batch MCP, #10✓ progressive disclosure, #21✓ pre-commit,
                   #45✓ next-steps, #48✓ doctor

REMAINING — v11 closeout (3 items, external actions):
  #24 GitHub topics (10m) + #29 Discussions (30m)
  #31 MCP directories + awesome-lists (2-3h) — submit ASAP

POST-v11 priorities:
  #33 integration tutorials (2-3d) — DONE (Session 30)
  #34 benchmark blog post (2-3d) — DONE (Session 31)
  #35 agent performance benchmark (3-5d) — DONE (Session 32)
  #56 ONNX semantic backend (10d) — DONE (Session 32)
  #37 OSS-repo benchmark expansion (2-3d) — next competitive-evidence step
```
v11 closes when #24 + #29 + #31 ship. `#26` is done; `#32` remains explicitly post-v11 and non-blocking.

---

## Positioning

**Current:** "Instant codebase comprehension for AI coding agents"

**Recommended:** "The codebase X-ray that catches what AI coding misses"

**Alternative (agent-focused):** "The computation layer AI agents cannot replicate by reading files"

**Vibe Code Auditor launch line:** "Your codebase is 42% AI-generated. Do you know how much of it is rotting?"

**Security differentiator:** "100% local, zero API keys, no code leaves your machine"

**Zero-Trust MCP (v6 strategic insight):** Frame roam as a **Zero-Trust MCP server**. Because roam only does static AST extraction and SQLite querying, it is immune to prompt-injection-to-RCE attacks that plague LLM-integrated bash/python execution tools. 41% of MCP servers lack auth, 43% have injection flaws — roam is architecturally immune. Use in README, docs, and launch messaging: *"Zero-Trust MCP: static analysis only, no code execution, no network calls, immune to prompt injection."*

> Full competitive analysis: [`reports/competitor_tracker.md`](competitor_tracker.md)
> Per-competitor files: `reports/competitors/`

---

## Competitor Feature Triage (Canonical Decision Layer)

The full competitor feature inventory is maintained in `reports/competitor_tracker.md`.
This section converts that inventory into product decisions: what we already have, what must ship before v11 unless impossible, and what we explicitly avoid.

### A) Features We Already Have (Shipped)

| Capability | Competitor Signal | roam Status |
|-----------|-------------------|-------------|
| MCP presets + toolset expansion | CKB preset model, Serena scoped workflows | **DONE** (`#2`, `#3`, `#6`) |
| Deterministic output for cache-friendly agent context | Emerging best practice for MCP tool reliability | **DONE** (`#90`) |
| Budget-aware truncation with importance ordering | Needed for agent context limits | **SHIPPED PARTIAL + DONE** (`#9`, `#91`) |
| CODEOWNERS + ownership drift + reviewer suggestions | CKB/Serena leadership area | **DONE** (`#38-#41`) |
| Secret scanning in local pipeline | CKB/SAST parity requirement | **DONE** (`#44`) |
| Structural change intelligence (API/test/semantic diff) | CKB + AI review tool trend | **DONE** (`#42`, `#43`, `#77`) |
| Multi-agent partition + affected + syntax judge checks | Multi-agent coding trend | **DONE** (`#88`, `#89`, `#92`) |
| Mermaid architecture outputs | Windsurf/DeepWiki-style visualization demand | **DONE** (`#82`) |
| Multi-agent context export bundle (not vendor-locked) | Agent workflows rely on repo guidance files | **DONE** (`#65`, `#68`) |
| Conversation-aware context ranking | Aider-style repo-map personalization for long sessions | **DONE** (`#94`) |

### B) Features We Must Implement Before v11 (Unless Blocked/Impossible)

| New ID | Feature | Why It Matters | Source Pattern |
|--------|---------|----------------|----------------|
| `#93` | Structural rule packs + optional autofix templates on `.roam/rules` | Brings ast-grep-like relational policy power into roam workflows | ast-grep rule system |
| `#95` | Daemon/webhook bridge for precomputed index refresh (**DONE**) | Keeps CI/PR analysis warm and faster | CodeMCP + Sonar operational patterns |
| `#96` | Pre-indexed framework/library packs | Better cold-start retrieval and onboarding quality | CodeGraph/Context-packing tools |
| `#97` | Smart client-aware context export targeting | Makes agent-export adaptive beyond single-vendor files by centering `AGENTS.md` + overlays | Multi-agent platform compatibility gap |
| `#98` | Streamable HTTP transport support with hardened defaults | Aligns with current MCP transport direction and client interoperability | MCP transport spec updates |
| `#99` | Full MCP tool annotation + `taskSupport` metadata | Improves planner behavior and safe tool usage across clients | MCP schema + annotation semantics |
| `#100` | Client compatibility profile + conformance tests | Prevents silent breakage across Copilot/Claude/Codex/Gemini/VS Code differences | GitHub Copilot + Gemini + VS Code docs |

### C) Features We Should Not Integrate (By Design)

| Feature Pattern | Decision | Rationale |
|----------------|----------|-----------|
| Cloud-required code analysis with mandatory API keys | **Do not integrate in core** | Conflicts with local-first, zero-key security positioning |
| MCP tools that execute arbitrary shell/python by default | **Do not integrate in core** | Breaks Zero-Trust MCP claim and raises prompt-injection blast radius |
| Black-box AI auto-fixers as primary analysis mode | **Do not integrate as default** | Reduces determinism/reproducibility; better as optional bridge, not core |
| SaaS-only multi-tenant governance dashboards | **Do not integrate now** | Product scope drift from CLI/MCP intelligence engine |
| Full CodeQL-class taint/data-flow parity | **Do not target near-term** | High complexity; complementary ecosystem already strong (CodeQL/Semgrep) |

### D) Primary Source Re-Validation (Web + Local, 22 Feb 2026)

| Source | What It Validates |
|--------|-------------------|
| https://modelcontextprotocol.io/specification/2025-11-25 | Current MCP revision baseline |
| https://modelcontextprotocol.io/specification/2025-11-25/basic/transports | Streamable HTTP transport direction, SSE legacy, origin validation expectations |
| https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization | OAuth 2.1, protected-resource metadata, and resource indicators for remote servers |
| https://modelcontextprotocol.io/specification/2025-11-25/changelog | New protocol primitives (`elicitation`, utility tools, resource links) |
| https://modelcontextprotocol.io/specification/2025-11-25/schema | `ToolExecution.taskSupport`, tool annotations, and metadata schema fields |
| https://modelcontextprotocol.io/legacy/concepts/tools | MCP tool annotation semantics (`readOnlyHint`, `destructiveHint`, etc.) |
| https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp | Copilot coding agent MCP constraints (tools-only, auth limitations) |
| https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions | Multi-file repository instruction support (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) |
| https://code.visualstudio.com/updates/v1_104#_custom-instructions-and-reusable-prompt-files | VS Code support for `AGENTS.md` custom instructions and reusable prompt files |
| https://docs.anthropic.com/en/docs/claude-code/memory | Claude Code hierarchical `CLAUDE.md` loading + imports |
| https://openai.com/index/introducing-codex/ | Codex `AGENTS.md` support signal in agent workflow docs |
| https://agents.md/ | Open format signal for cross-agent instruction interoperability |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/configuration.md | Gemini context file hierarchy and configurable instruction filename behavior |
| https://github.com/google/A2A | A2A protocol maturity signal and ecosystem trajectory |
| https://github.com/SonarSource/sonarqube-mcp-server | SonarQube MCP tool surface and server-centric operating model |
| https://docs.codeknowledge.dev/mcp/getting-started/mcp-integration | CKB preset counts by current version (v7.4 docs snapshot) |
| https://docs.codeknowledge.dev/news/token-economics-of-mcp-toolsets | CKB preset-size publication showing 80+ full preset and 14 core references |
| https://docs.codeknowledge.dev/mcp/getting-started/mcp-tools-reference | CKB tool catalog references and count inconsistency signal |
| https://www.codeknowledge.dev/pricing | CKB marketing claim of 90+ tools (cross-check against docs) |
| https://oraios.github.io/serena/docs/mcp_guide/available_tools/ | Serena documented tool list count and category coverage |
| https://semgrep.dev/docs/semgrep-mcp | Semgrep MCP server capability status (beta) |
| https://semgrep.dev/docs/semgrep-mcp#supported-transports-and-client-compatibility | Semgrep transport/auth compatibility details (stdio, SSE, Streamable HTTP) |
| https://ast-grep.github.io/guide/rule-config/relational-rule.html | Relational structural matching worth porting into roam rule packs |
| https://raw.githubusercontent.com/Aider-AI/aider/main/aider/repomap.py | PageRank personalization mechanics for context ranking |
| https://repomix.com/guide/mcp-server | Context-packaging workflow expectations in MCP ecosystems |
| https://github.com/yamadashy/repomix | Repomix current MCP tool surface (README) |
| https://mcp.so/server/codescene-mcp-server/codescene-io | CodeScene MCP listing signal (tool count + stars) |
| https://registry.modelcontextprotocol.io/ | MCP ecosystem registry as distribution baseline |

### E) Fresh Web-Validated Gap Findings (Feb 2026)

| Finding | Evidence | Backlog Mapping |
|---------|----------|-----------------|
| MCP current revision is now 2025-11-25 (not 2025-06-18), so transport/auth assumptions must be updated | MCP spec index + changelog | `#98`, `#100` |
| MCP transport direction includes Streamable HTTP with explicit security checks (origin validation) and SSE legacy context | MCP transport docs | `#98` |
| MCP authorization model requires OAuth 2.1 patterns, protected-resource metadata, and resource indicators for remote flows | MCP authorization docs | `#98`, `#100` |
| MCP schema exposes `ToolExecution.taskSupport` and richer annotation fields used by planners | MCP 2025-11-25 schema | `#99` |
| Copilot coding agent MCP support is currently tools-only and excludes prompts/resources, with auth constraints on remote MCP | GitHub Copilot MCP docs | `#100` |
| GitHub custom instruction files now explicitly support `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` with precedence behavior | GitHub instruction docs | `#97`, `#100` |
| VS Code explicitly supports `AGENTS.md`, reinforcing canonical-generic export strategy with provider overlays when documented per client | VS Code release notes | `#97`, `#100` |
| Claude Code loads `CLAUDE.md` hierarchically and supports imports, favoring layered export generation | Anthropic memory docs | `#97`, `#100` |
| Gemini CLI supports hierarchical context file loading and configurable context filename, plus strict schema handling | Gemini CLI config docs | `#97`, `#100` |
| CKB competitor benchmark counts are internally inconsistent (docs now show 76/14 and 80+/14 references vs other pages: 90+/92), so matrix values should be tracked as ranges with version pinning | CKB docs + pricing | `#100` |
| Serena currently documents 40 tools; prior "~45" assumptions should be normalized to docs-backed values | Serena tools docs | `#100` |
| Repomix MCP server now documents 7 tools; prior `6` in matrix is stale | Repomix README | `#97`, `#100` |
| Semgrep now documents MCP Server beta; matrix classification should be `Server (beta)` not client-only | Semgrep MCP docs | `#100` |
| Semgrep explicitly documents stdio/SSE/Streamable HTTP transport and authentication paths, reinforcing remote-transport compatibility work | Semgrep transport compatibility docs | `#98`, `#100` |
| A2A protocol (v0.3.0) is maturing and should be tracked for future interoperability | A2A GitHub repo | Someday/Maybe `A2A Agent Card` |

---

## Research Insights (February 2026)

> Full agent transcripts available in task output files. Key findings summarized below.
> Sources: 16 Opus agents (6 landscape + 4 deep-dive + 6 final research), 200+ web sources

**Top signals across all 16 research agents:**
1. **MCP directory listings URGENT** — Official Registry 518 servers (90→518 in 1 month); PulseMCP 8,610+; competitors listed, we're not (6/6 → 16/16)
2. **Vibe Code Auditor is the zeitgeist** — GitClear 211M lines, SonarSource 42% AI code, OX 10 anti-patterns, CodeRabbit 1.7x more issues (5/6 → 14/16)
3. **"100% local" is now a security differentiator** — **41% of MCP servers lack authentication** (Feb 2026 audit); 43% have injection flaws (5/6 → 12/16)
4. **Multi-agent orchestration is THE 2026 trend** — Claude Agent Teams, Codex multi-agent, VS Code multi-agent (Feb 2026) (4/6 → 10/16)
5. **Historical trend tracking is missing** — DX Core 4 replacing DORA; CTOs want trends (4/6 → 8/16)
6. **Academic validation of graph approach** — SNA metrics: 87% recall for debt detection (3/6 → 6/16)
7. **NEW: Agent platform gap is our biggest opportunity** — Codex CLI #1 limitation is no indexing; Gemini CLI #1 request is persistent indexing; Claude Code has no call graph (6/16)
8. **NEW: Compound operations validated by data** — MCP-Atlas: best model only 62.3% on multi-tool tasks; fewer calls = higher success (6/16)

**Key academic papers driving backlog items:**

| Paper | Finding | Backlog Item |
|-------|---------|-------------|
| PLOS ONE — TD via Complex Software Networks | SNA + TD = 87% recall | #70 |
| Code-Craft (arXiv:2504.08975) | 82% retrieval improvement via call graph propagation | #72 |
| Frontiers Neuroscience — Code Complexity | Fan-out + scatter > cyclomatic for actual difficulty | #71 |
| GitClear 2025 — 211M lines | AI duplication 4x, refactoring collapsed | #57 expansion |
| arXiv:2602.14878 — MCP Tool Smells | 97.1% of tools have smells; roam ahead (top 2.9%) | Validates #5 |
| arXiv:2511.04453 — Community launch impact | Avg +289 stars in 7 days for one major tech-community launch post | Context for optional `#32` |
| MCP-Atlas benchmark (Feb 2026) | Best model 62.3% on multi-tool tasks | Validates #2 (compounds) |
| Overthinking Loops (agent research) | Agents lose 47% efficiency on long reasoning chains | Validates #9 (budget) |
| CodeRabbit 2M+ repo study | AI code 1.7x more issues, 3x readability problems | Validates Epic 10 |
| FSE 2025 — Semantic Clone Detection | AI produces functionally-equivalent clones with divergent edge cases | Validates #87 |

---

## Deep Review Notes (Independent Audit - 22 Feb 2026)

This section is a direct review of backlog quality and execution fitness.
It focuses on internal consistency, release readiness, and decision clarity.

### 1) Integrity Findings and Cleanup Status

| Finding | Impact | Cleanup Applied | Status |
|--------|--------|-----------------|--------|
| Status drift between "Already Done" and epic tables | False remaining-work signal | Normalized status fields across epic tables | **Resolved in v6.2** |
| `#9` ambiguity (done vs elevated) | Scope confusion | Reframed as `SHIPPED (PARTIAL)` with explicit phase notes | **Resolved in v6.2** |
| v11 remaining count mismatch | Release tracking errors | Recomputed live snapshot from normalized rows (now 3 remaining after `#26` shipped and `#32` moved post-v11) | **Resolved in v6.2 + refreshed Session 34** |
| Completed count stale | Misleading velocity signal | Replaced with live snapshot metrics block | **Resolved in v6.2** |
| Launch-copy command-count drift | Public messaging inconsistency | Updated launch copy to `136 canonical CLI commands` (`137` invokable names with legacy alias) | **Resolved** |
| Quick-win chain estimate drift | Schedule reliability drops | Corrected durations + clarified historical bundles | **Resolved in v6.2** |
| Execution tracks included shipped work | Planning rework overhead | Replaced with v11 remaining-only execution plan | **Resolved in v6.2** |

### 2) Strategic risks observed

| Risk | Why it matters | Mitigation |
|------|----------------|------------|
| **Documentation crisis (v7 — CRITICAL)** | Command/MCP/CHANGELOG parity, v11 narrative, and roadmap hygiene are now fixed (`#106` + `#107` + `#108` + `#109` + `#112`) | **Resolved** |
| **Agent first-run failure (v7 — RESOLVED)** | Epic 8 ALL DONE. Agents get error hints, fuzzy suggestions, doctor diagnostics, next-step guidance, reset/clean | All 5 items (#45, #48, #50, #51, #52) shipped |
| **Command count confusion (v7 — HIGH)** | cli.py registered ~116 names while docs said 96. Needed explicit alias/canonical methodology | **Resolved by `#108`**: now documented as `136 canonical + 1 legacy alias = 137 invokable names` in code + docs + tests |
| Launch scope mixes product, marketing, and research tasks in one board | Hard to tell what blocks release vs what is growth follow-up | Split into `Release-Critical`, `Post-Launch Growth`, and `R&D` boards |
| External tasks lack explicit "blocking" status | #24, #29, #31 depend on GitHub/community actions and can stall quietly (`#32` is now deferred/non-blocking) | Add `BLOCKED_EXTERNAL` status and owner/date fields |
| Too many active narratives at once | Zero-Trust MCP, Vibe Auditor, Multi-Agent OS, Search v2 all compete for attention | Pick one primary launch message and one secondary proof point |
| Research-stat freshness risk | Competitive/security numbers can decay quickly | Add `last_verified` date for each numeric claim; re-validate at each phase gate |
| **Competitive evidence still sparse (v7)** | Benchmark publication exists and includes first direct with/without slice (`codex` `cpp-calculator` `vanilla` vs `roam-cli`), but matrix coverage is still partial (16/60) | Continue #37 expansion on major OSS repos and fill additional roam-cli/roam-mcp rows |
| **Pre-commit distribution (v7 — RESOLVED)** | pre-commit hooks shipped (#21). 5 hooks: secrets, syntax-check, verify, health, vibe-check | **DONE** |
| SARIF uploads can silently replace or truncate findings | Fixed upload category collisions and SARIF size/result limits can hide or drop alerts | #105 shipped; verify in production CI runs |

### 3) Recommended execution order from current state

**Completed:** Documentation crisis (Phase -1), agent retention MVP (Phase 0.5), CI consolidation, PyPI, batch MCP, progressive disclosure, pre-commit hooks, doctor, next-steps — ALL DONE.

**Next actions:**
1. **v11 closeout (external):** `#24` topics (10m) + `#29` Discussions (30m) + `#31` MCP directories (2-3h)
2. **Competitive score uplift (remaining):** core uplift items `#132` (+1pt) and `#136` (+1pt) are now shipped.
3. **Code intelligence:** maintain and iterate on shipped coverage ingestion signals in `health`, `metrics`, and `test-gaps`
4. **Distribution:** maintain shipped tutorial+blog+benchmark artifacts (`#33`, `#34`, `#35` done), then complete `#37` OSS repo expansion (harness is in place).
5. **Long-horizon:** optional `#32` launch note and expanded comparative benchmark matrix coverage.

### 4) Governance upgrades to keep this backlog healthy

- Add canonical statuses: `TODO`, `IN_PROGRESS`, `BLOCKED_EXTERNAL`, `SHIPPED_PARTIAL`, `SHIPPED`, `DEFERRED`.
- Add metadata columns: `Owner`, `Last Updated`, `Last Verified`, `Evidence` (PR/commit/link).
- Auto-generate summary metrics from table rows instead of manual text.
- Add one phase-gate "backlog integrity pass" as a recurring task.

### 5) Suggested release gate definition (v11)

v11 is **~97% complete**. Remaining 3 items are external actions:

| Gate | Status |
|------|--------|
| Documentation accuracy (#106-#109, #112) | **DONE** |
| v11 narrative in README (#109) | **DONE** |
| Roadmap hygiene (#112) | **DONE** |
| CONTRIBUTING + CHANGELOG (#27, #28) | **DONE** |
| Agent error recovery (Epic 8) | **ALL DONE** |
| GitHub topics (#24) | **TODO** (10m) |
| GitHub Discussions (#29) | **TODO** (30m) |
| Demo GIF (#26) | **DONE** (Session 34) |
| MCP directory listings (#31) | **TODO** (2-3h) |
| Community launch note (#32) | **DEFERRED** (non-blocking) |

### 6) Additional pre-launch hardening checks

1. ~~Confirm SARIF uploads use unique categories~~ → **DONE** (#105 shipped)
2. For MCP Registry entries in `#31`, add re-verification reminder (registry preview resets)
3. ~~Verify ci.yml vs roam-ci.yml~~ → **DONE** (#110 shipped, ci.yml removed)
4. ~~Verify pyproject.toml keywords~~ → **DONE** (#111 shipped)
5. ~~Verify agent error messages~~ → **DONE** (#50 shipped, Epic 8 ALL DONE)
6. Expand benchmark matrix depth on external OSS repos and additional roam-mcp rows (#37 — open)

---

*Source: 14 reports in reports/archive/ (01-14)*
*Competitor data: reports/competitor_tracker.md + 24 files in reports/competitors/*
*Competitive score: 84/100 (nearest: SonarQube 63, CodeQL 49) — see memory/competitive-scoring.md*
*Research: 16 Opus agents, 200+ web sources, Feb 2026*
*Backlog v8.0: 145 items, 134 shipped, 5 open. 136 canonical CLI commands, 101 MCP tools, ~130 test files, 4889 tests.*
