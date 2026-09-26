<p align="center"><sub>● SYS_STATUS: NOMINAL // AUTH: ED25519 // 10 SOLO AGENTS // 13 PIPELINES // LOC: HYDERABAD [17.3850° N, 78.4867° E] // LATENCY: 12ms // ⌘K CONSOLE</sub></p>

<h1 align="center">Hi, I'm Maithresh Vaddi 👋</h1>
<p align="center"><b>Final-year B.Tech CSE @ KMIT Hyderabad (CGPA 7.96/10)</b> · building <b>agentic RAG</b> that works offline and survives production</p>

<p align="center"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=920&lines=%24+whoami+--role+%2F%2F+maithresh.sh;AI%2FML+Engineer+%26+Agentic+Systems+Builder;10+solo+systems+%C2%B7+13+automations+%C2%B7+100%25+offline-capable;If+I+can%27t+defend+it%2C+it+isn%27t+here" alt="Typing intro" width="100%"/></p>

<p align="center">
  <a href="https://maithreshvaddi-27.github.io/maithresh.sh/"><img src="./assets/05-pill-portfolio.svg" alt="Portfolio — maithresh.sh" height="32"/></a>
  <a href="https://www.linkedin.com/in/maithreshvaddi/"><img src="./assets/06-pill-linkedin.svg" alt="LinkedIn" height="32"/></a>
  <a href="mailto:maithreshvaddi16@gmail.com"><img src="./assets/07-pill-gmail.svg" alt="Gmail" height="32"/></a>
  <a href="https://leetcode.com/u/MaithreshV/"><img src="./assets/08-pill-leetcode.svg" alt="LeetCode" height="32"/></a>
  <a href="https://www.hackerrank.com/profile/maithreshvaddi16"><img src="./assets/09-pill-hackerrank.svg" alt="HackerRank" height="32"/></a>
</p>

<p align="center"><img src="./assets/01-hero-whoami.svg" alt="maithresh.sh boot console — Maithresh Vaddi, AI/ML Engineer" width="100%"/></p>

<p align="center"><img src="./assets/12-metrics-strip.svg" alt="$ ./metrics.sh --live — 10 solo systems, 13 automations, 100% offline inference" width="100%"/></p>

## About · `$ cat about.md`

> No inflated claims — every line here is something I can defend in an interview. Final-year **B.Tech CSE @ KMIT Hyderabad** (CGPA **7.96/10**), building **agentic RAG** outside class: hybrid retrieval, MCP tool orchestration, LangGraph recovery loops. Now hardening **TrustRAG** verification + pushing **CareerOS-Pro** to Docker prod.

<p align="center"><img src="./assets/02-ascii-portrait.svg" alt="TARGET // MAITHRESH_VADDI — whoami --ascii render" width="360"/></p>

<img src="./assets/03-about-intro.svg" alt="$ cat about.md — defense pledge" width="100%"/>
<img src="./assets/04-status-snapshot.svg" alt="$ curl stack.local/llm — local inference runtime telemetry" width="100%"/>

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,fastapi,react,docker,aws,redis,mongodb,mysql,kubernetes,js,ts,nodejs,express,sqlite&theme=dark" alt="Tech stack icons"/>
</p>

<details>
<summary><code>$ ls stack/ --grouped</code> — full stack detail</summary>
<br>

- **llm.sh** — LangChain · LangGraph (self-healing loops, multi-provider routing) · CrewAI · MCP server + client (JSON-RPC 2.0, Composio) · RAG (dense + BM25 + RRF) · cross-encoder rerank · NLI verify · Qdrant · ChromaDB · ONNX · bge-small/base, mpnet · Gemini · NVIDIA NIM · Ollama · llama.cpp · MLX · ReAct/Plan-Execute · memory/checkpointing · LoRA/RLHF. Method: directed AI-orchestrated engineering — architecture owned, implementation delegated.
- **automation.sh** — n8n ×10 · Make.com · Automation Anywhere (RPA) · Webhooks · REST · Telegram Bot API · Groq Whisper · Redis.
- **backend.sh** — Python · Java (OOP) · C++ · JS (ES6) · SQL · FastAPI · Granian · Flask · httpx · Pydantic · SQLAlchemy · Node/Express · MongoDB · MySQL · SQLite · Redis · Pandas/NumPy. 26 LeetCode SQL.
- **cloud.sh** — Docker/Compose · AWS (labs) · Render · Cloudflare Pages · K8s · Jenkins · TF/Keras · sklearn · YOLO · Git · pytest/Vitest/Playwright/k6/Bandit/Trivy. Frontend (supporting): React 19, Framer Motion, Gradio, Bootstrap · Figma.

</details>

<p align="center"><img src="./assets/13-stack-marquee.svg" alt="$ ls stack/ --stream — streaming stack marquee" width="100%"/></p>

## [01] Systems · `$ ls projects/ --featured`

### [TrustRAG — AI Reliability Workbench](https://github.com/MaithreshVaddi-27/TrustRAG) · flagship · `FastAPI · React 18 · Qdrant · LangGraph · ONNX · MCP · Docker`
`route → hybrid retrieve → grounded generate → claim decompose + NLI (one fused call, −62% verify latency) → SHA-256 audit → score vs τ ≥ 0.75 → bounded recover (≤2) → answer / ABSTAIN`
- Offline by default: Ollama/llama.cpp/MLX + ONNX `bge-small` + int8 rerank. No API keys. Optional Gemini/NVIDIA NIM.
- Perf work: KV-cache quant, flash attention, prompt caching, speculative decoding, adaptive top-k. JWT-HS256 + JTI denylist, SSRF-hardened URLs, Prometheus, A/B framework, MCP server.
- 111 pytest + 15 Vitest + 2 Playwright E2E · k6 p95 < 300 ms · Bandit + Trivy CI gates.

| Build | One line |
|---|---|
| [DocuChat](https://github.com/MaithreshVaddi-27/MCP_Agentic_DocuChat) | Agentic PDF-RAG (CLI + Gradio): Gemini/Ollama/llama.cpp, Composio MCP routing, SQLite memory. Killed the 3-agent swarm → single agent: 6.8 s → 1.9 s, −68% tokens. |
| [CareerOS-Pro](https://github.com/MaithreshVaddi-27/CareerOS-Pro) | 5 job APIs + async career-page scraper · deterministic normalize, 2-stage dedup (−74% redundant posts) · LangGraph fallback chain · HEAD+Firecrawl verify · `/agents/health` · Docker. |
| [Resume Crew](https://github.com/MaithreshVaddi-27/Resume_Crew) | CrewAI resume↔JD matcher, evidence-only report (zero invented skills), 8-workflow Gradio + CLI, offline Ollama default, telemetry off. |
| [Game Dev Crew](https://github.com/MaithreshVaddi-27/AI-Game-Dev-Crew) | Designer→Dev→QA pipeline, idea → playable WASM game (pygbag + ngrok). Fixed launcher-overwrite + async-loop freeze. |

> `$ run workbench --select-system` → live pipeline simulators + interview defenses on [maithresh.sh](https://maithreshvaddi-27.github.io/maithresh.sh/).

<details>
<summary><code>$ ls agents/more/</code> — SkillMap · SalaryInsights · Inbox Summarizer · Blog Crew · CourseFinder</summary>
<br>

- [SkillMap](https://github.com/MaithreshVaddi-27/MCP_SkillMap_Agent) — live India job search (Tavily+JSearch), checkpointed follow-ups.
- [SalaryInsights](https://github.com/MaithreshVaddi-27/MCP_SalaryInsights_Agent) — Glassdoor/AmbitionBox/PayScale/Levels.fyi via Firecrawl MCP, sourced answers.
- [Inbox Summarizer](https://github.com/MaithreshVaddi-27/MCP_Email_Inbox_Summarizer) — Gmail URGENT/NEEDS REPLY/FYI triage; drafts only, never sends.
- [Blog Crew](https://github.com/MaithreshVaddi-27/Ai-Blog-Writer-Crew) / [CourseFinder](https://github.com/MaithreshVaddi-27/MCP_CourseFinder_Agent) — topic→edited post; Tavily+YouTube learning paths, grounded only.

</details>

## [02] Automations · `$ ls automation/ --all`

**[Ai-Workflow-Automations](https://github.com/MaithreshVaddi-27/Ai-Workflow-Automations)** — 10 n8n (agentic Shopping Assistant w/ voice + Redis memory · Learning-Path→Docs+Calendar · Internship Applier · Job Tracker · digests) · 2 Make.com (Sheets→Gemini social pipeline · Telegram resume agent) · 1 Automation Anywhere RPA reminder bot (Try-Catch row safety).
**[PodEase Pro](https://podease-pro.lovable.app)** `● LIVE` — Lovable → n8n webhook → Gemini script → Murf TTS, idea-to-audio.

## [03] Academic · `$ ls team/ --scope=mine`

- **[CrimeSleuth](https://github.com/MaithreshVaddi-27/CrimeSleuth)** (4) — **trained** 14-class crime-scene classifier (Colab, `.pth`) + YOLO Flask inference → Gemini reports. · **[SignatureSense](https://github.com/MaithreshVaddi-27/SignatureSense)** (4) — **integrated** pre-trained Keras `.h5` verifier + preprocessing/tests.
- KMIT B.Tech CSE 2023–2027 · DSA · OS · DBMS · Networks · SE · Cloud (AWS) · Cyber Security. Extras: F5-TTS Kaggle voice-clone · FoodMunch Bootstrap page. Full detail: [`docs/CV_All.pdf`](./docs/CV_All.pdf)

## [04] Credentials · `$ cat certifications.md`

StudyComrade Data Analytics (EDA on Amazon dataset) · Outskill AI Mastermind (assistants/GPTs, Claude Artifacts, generative media, AI-built sites).

## 👻 Contribution Arcade · `$ ./play.sh --pacman`

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/pacman-contribution-graph-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/pacman-contribution-graph.svg"/>
    <img src="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/pacman-contribution-graph.svg" alt="Pac-Man eating the contribution grid" width="100%"/>
  </picture>
</p>

<sub>Pac-Man regenerates daily via <code>.github/workflows/pacman.yml</code> → <code>output</code> branch (abozanona/pacman-contribution-graph). Trigger once manually in Actions after push.</sub>

<details>
<summary><code>$ ./play.sh --snake</code> — classic snake variant</summary>
<br>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/github-contribution-grid-snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/github-contribution-grid-snake.svg"/>
    <img src="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/github-contribution-grid-snake.svg" alt="Contribution snake eating the grid" width="100%"/>
  </picture>
</p>

<sub>Snake regenerates daily via <code>.github/workflows/snake.yml</code> → <code>output</code> branch. Trigger once manually in Actions after push.</sub>

</details>

<img src="./assets/10-closing-statement.svg" alt="$ ./contact.sh --open" width="100%"/>

📫 [maithresh.sh](https://maithreshvaddi-27.github.io/maithresh.sh/) · [LinkedIn](https://www.linkedin.com/in/maithreshvaddi/) · [maithreshvaddi16@gmail.com](mailto:maithreshvaddi16@gmail.com) — open to AI/ML, GenAI, Agentic AI, Automation internships. Hyderabad / remote.

<img src="./assets/11-session-end.svg" alt="logout — press ESC to close" width="100%"/>
