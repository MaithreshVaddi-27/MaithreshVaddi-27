<p align="center"><sub>● SYS_STATUS: NOMINAL // AUTH: ED25519 // 10 SOLO AGENTS // 13 PIPELINES // LOC: HYDERABAD [17.3850° N, 78.4867° E] // LATENCY: 12ms // ⌘K CONSOLE</sub></p>

<p align="center"><img src="./assets/01-hero-whoami.svg" alt="maithresh.sh boot console — Maithresh Vaddi, AI/ML Engineer" width="840"/></p>

<p align="center"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=21&pause=1000&color=38BDF8&center=true&vCenter=true&width=840&lines=%24+whoami+--role+%2F%2F+maithresh.sh;AI%2FML+Engineer+%26+Agentic+Systems+Builder;10+solo+systems+%C2%B7+13+automations+%C2%B7+100%25+offline-capable;If+I+can%27t+defend+it%2C+it+isn%27t+here" alt="Typing intro"/></p>

<p align="center">
  <a href="https://maithreshvaddi-27.github.io/maithresh.sh/"><img src="https://img.shields.io/badge/maithresh.sh-0D1117?style=flat-square&logo=vercel&logoColor=38BDF8" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/maithreshvaddi/"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&logo=linkedin&logoColor=F8FAFC" alt="LinkedIn"></a>
  <a href="mailto:maithreshvaddi16@gmail.com"><img src="https://img.shields.io/badge/Gmail-0D1117?style=flat-square&logo=gmail&logoColor=F8FAFC" alt="Gmail"></a>
  <a href="https://leetcode.com/u/MaithreshV/"><img src="https://img.shields.io/badge/LeetCode-0D1117?style=flat-square&logo=leetcode&logoColor=F8FAFC" alt="LeetCode"></a>
  <a href="https://www.hackerrank.com/profile/maithreshvaddi16"><img src="https://img.shields.io/badge/HackerRank-0D1117?style=flat-square&logo=hackerrank&logoColor=F8FAFC" alt="HackerRank"></a>
</p>

<p align="center"><img src="./assets/12-metrics-strip.svg" alt="$ ./metrics.sh --live — 10 solo systems, 13 automations, 100% offline inference" width="840"/></p>

<img src="./assets/03-about-intro.svg" alt="$ cat about.md — defense pledge" width="840"/>

> No inflated claims — every line here is something I can defend in an interview. Final-year **B.Tech CSE @ KMIT Hyderabad** (CGPA **7.96/10**), building **agentic RAG** outside class: hybrid retrieval, MCP tool orchestration, LangGraph recovery loops. Now hardening **TrustRAG** verification + pushing **CareerOS-Pro** to Docker prod.

<p align="center"><img src="./assets/02-ascii-portrait.svg" alt="TARGET // MAITHRESH_VADDI — whoami --ascii render" width="320"/></p>

<img src="./assets/04-status-snapshot.svg" alt="$ curl stack.local/llm — local inference runtime telemetry" width="840"/>

## [01] Systems · `$ ls projects/ --featured`

#### [TrustRAG — AI Reliability Workbench](https://github.com/MaithreshVaddi-27/TrustRAG) · flagship · `FastAPI · React 18 · Qdrant · LangGraph · ONNX · MCP · Docker`
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
**[PodEase Pro](https://podease-pro.lovable.app)** ![live](https://img.shields.io/badge/status-live-10B981?style=flat-square&labelColor=0D1117) — Lovable → n8n webhook → Gemini script → Murf TTS, idea-to-audio.

## [03] Academic · `$ ls team/ --scope=mine`

- **[CrimeSleuth](https://github.com/MaithreshVaddi-27/CrimeSleuth)** (4) — **trained** 14-class crime-scene classifier (Colab, `.pth`) + YOLO Flask inference → Gemini reports. · **[SignatureSense](https://github.com/MaithreshVaddi-27/SignatureSense)** (4) — **integrated** pre-trained Keras `.h5` verifier + preprocessing/tests.
- KMIT B.Tech CSE 2023–2027 · DSA · OS · DBMS · Networks · SE · Cloud (AWS) · Cyber Security. Extras: F5-TTS Kaggle voice-clone · FoodMunch Bootstrap page. Full detail: [`docs/CV_All.pdf`](./docs/CV_All.pdf)

## Stack · `$ ls stack/ --grouped`

- **llm.sh** — LangChain · LangGraph (self-healing loops, multi-provider routing) · CrewAI · MCP server + client (JSON-RPC 2.0, Composio) · RAG (dense + BM25 + RRF) · cross-encoder rerank · NLI verify · Qdrant · ChromaDB · ONNX · bge-small/base, mpnet · Gemini · NVIDIA NIM · Ollama · llama.cpp · MLX · ReAct/Plan-Execute · memory/checkpointing · LoRA/RLHF. Method: directed AI-orchestrated engineering — architecture owned, implementation delegated.
- **automation.sh** — n8n ×10 · Make.com · Automation Anywhere (RPA) · Webhooks · REST · Telegram Bot API · Groq Whisper · Redis.
- **backend.sh** — Python · Java (OOP) · C++ · JS (ES6) · SQL · FastAPI · Granian · Flask · httpx · Pydantic · SQLAlchemy · Node/Express · MongoDB · MySQL · SQLite · Redis · Pandas/NumPy. 26 LeetCode SQL.
- **cloud.sh** — Docker/Compose · AWS (labs) · Render · Cloudflare Pages · K8s · Jenkins · TF/Keras · sklearn · YOLO · Git · pytest/Vitest/Playwright/k6/Bandit/Trivy. Frontend (supporting): React 19, Framer Motion, Gradio, Bootstrap · Figma.

<p align="center"><img src="./assets/13-stack-marquee.svg" alt="$ ls stack/ --stream — streaming stack marquee" width="840"/></p>

## [04] Credentials · `$ cat certifications.md`

StudyComrade Data Analytics (EDA on Amazon dataset) · Outskill AI Mastermind (assistants/GPTs, Claude Artifacts, generative media, AI-built sites).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/github-snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/github-snake.svg"/>
    <img src="https://raw.githubusercontent.com/MaithreshVaddi-27/MaithreshVaddi-27/output/github-snake.svg" alt="Contribution snake eating the grid" width="840"/>
  </picture>
</p>

<sub>Snake regenerates daily via <code>.github/workflows/snake.yml</code> → <code>output</code> branch. Trigger once manually in Actions after push.</sub>

<img src="./assets/10-closing-statement.svg" alt="$ ./contact.sh --open" width="840"/>

📫 [maithresh.sh](https://maithreshvaddi-27.github.io/maithresh.sh/) · [LinkedIn](https://www.linkedin.com/in/maithreshvaddi/) · <mailto:maithreshvaddi16@gmail.com> — open to AI/ML, GenAI, Agentic AI, Automation internships. Hyderabad / remote.

<img src="./assets/11-session-end.svg" alt="logout — press ESC to close" width="840"/>
