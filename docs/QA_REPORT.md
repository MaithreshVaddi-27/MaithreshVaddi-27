# GitHub Profile Redesign — Concept Comparison & QA Report

**Branch:** `monograph-trace` (branched cleanly from `main` at `7ec95d8`; `main` and `cyber-terminal` untouched)  
**Portfolio Reference:** [https://maithresh.pages.dev/](https://maithresh.pages.dev/)  
**Repository Source of Truth:** 18 repositories analyzed from `projects-github/` + live GitHub API (`MaithreshVaddi-27`)  
**Selected Direction:** **Concept 01 (`The Verification Monograph`) + Concept 03 (`Signal & Trace`) Hybrid**, implemented with full **Dark/Light `<picture>` parity**.

---

## 1. Five Concepts Explored

1. **`01-verification-monograph`** — Editorial serif + obsidian (`#0B0D11`) + cobalt (`#60A5FA`) sister artifact to `maithresh.pages.dev`, featuring `SPEC // MV-2027` and `FIG 01` TrustRAG trace.
2. **`02-archival-broadsheet`** — Dual-theme Bell Labs / Swiss broadsheet (`#FAF8F4` paper light / `#0B0D11` obsidian dark) with test-density bar chart and 2-column ledger.
3. **`03-signal-and-trace`** — Distributed-tracing topology canvas connecting `Local Inference Bus → Verification Kernel → Deterministic Pipelines → MCP Fabric` plus a measured-coverage waterfall.
4. **`04-modular-specimen-grid`** — 2×2 GitHub-native Bento SVG tiles (`#161B22` / `#30363D`) + 2×3 flagship cards for 15-second recruiter scanning.
5. **`05-first-principles-minimal`** — Radical restraint with a single dual-theme `M` monogram header SVG and pure GitHub Markdown.

---

## 2. Content Alignment From 18 `projects-github/` Repositories

- **`ApplyOS`:** `96` test files (`~1,041` test cases), `14` providers, `9` gates / `4` dimensions / `5` bands, `13` Bun portal CLIs, `4` offline eval suites, LuaLaTeX CV + `verify_pdf.py --check-ats`.
- **`TrustRAG`:** `86` test files (`~835` test cases across pytest, Vitest, Playwright, k6 `p95 < 300ms`), adaptive `≤3B` vs larger-model prompt tiering, ONNX `bge-small` + `ms-marco` int8, SPO NLI + SHA-256 + MCP JSON-RPC 2.0.
- **`CareerOS-Pro`:** `17` test files (`~218` test functions + `53` scraper/related tests in `STATUS.md`), 6 sources + async company scraper, `url_hash` + `content_hash` dedup, LangGraph `human_review`, Ruff pinned CI.
- **`MCP_Agentic_DocuChat`:** `5` test files (`102` unittest tests), Ollama / llama.cpp / MLX, page-pinned **Sources**, injection-hardened evidence isolation.
- **`Resume_Crew`:** `v1.4.0`, `8` test files (`52` pytest functions), CrewAI `1.15.11`, 9 artifacts, `--check-hardware`, telemetry disabled.
- **`home-credit-lap-voice-agent`:** Retell AI Hindi/English LAP pre-screening up to `₹75L`, 7-rule matrix, 4 hard stops, 7 scenario transcripts.
- **`Ai-Workflow-Automations`:** `10` n8n + `2` Make.com + `1` Automation Anywhere RPA (`13` workflows).
- **MCP CLI Suite, CrewAI & Academic/Media:** `MCP_SkillMap_Agent`, `MCP_SalaryInsights_Agent`, `MCP_CourseFinder_Agent`, `MCP_Email_Inbox_Summarizer`, `AI-Game-Dev-Crew`, `Ai-Blog-Writer-Crew`, `maithresh.sh`, `CrimeSleuth`, `SignatureSense`, `F5-tts-podcast-generator`, `FoodMunch`.

---

## 3. Production Assets (`assets/`) & Verification

- `01-hero-monograph-{dark,light}.svg` — Editorial manifesto + `SPEC // MV-2027` dossier plate
- `02-metrics-ledger-{dark,light}.svg` — 4-column verified proof strip (`13+`, `13`, `880`, `7.96`)
- `03-system-topology-{dark,light}.svg` — `FIG 01` multi-system architecture topology
- `05-measured-deltas-{dark,light}.svg` — `FIG 02` verified test & eval coverage across flagship repos
- `04-fig01-trustrag-trace-{dark,light}.svg` — `FIG 03` TrustRAG 8-stage verification trace (`ANSWER` / `ABSTAIN`)
- `.github/scripts/pacman_recolor.py` — Updated Pac-Man contribution ramp to Monograph Cobalt (`#172554 → #93C5FD` dark, `#BFDBFE → #1E3A8A` light)
- All 10 SVGs XML-validated, `<title>` + `prefers-reduced-motion: reduce` checked, zero external dependencies, visually inspected in Brave across Dark and Light themes.
