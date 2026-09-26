# Ultra-Premium Repo Audit — GitHub Profile README (`maithresh.sh` terminal theme)

Date: 2026-09-26 · Scope: entire working tree (`README.md`, `assets/*.svg`, `.github/workflows/*`, `.github/scripts/*`, `docs/`, `.gitignore`)
Lenses: Senior Product Designer (apple-design + ui-ux-pro-max) · Senior Frontend Developer · Senior Security Engineer · Release/CI Engineer
Method: file reads + `git log/status/diff` + SVG DOM inspection (ids, keyframes, reduced-motion, viewBox) + YAML parse + external-host inventory. No guessing; every finding cites evidence.

---

## 0. Verdict (read first)

| Area | Score | One-line verdict |
|---|---|---|
| Design system / craft | 9/10 | Genuinely premium: one terminal language, one palette, one motion grammar across 8 SVGs. Keep the system, delete the off-theme intruder. |
| Frontend / performance | 6/10 | Local SVGs are lean (~60 KB total) but the Analytics block injects 5 slow third-party renders that break the theme and the load budget. |
| Security / privacy | 8/10 | No secrets, no injection surface. Two supply-chain softenings (unpinned action, broad token) + tracker bloat from Analytics widgets. |
| CI / workflows | 5/10 | **One live data-loss bug:** `snake.yml` wipes `pacman.yml` output on every run. Plus one untracked workflow file. |
| Hygiene / dead code | 7/10 | No real dead code. Two stray `.DS_Store` files on disk (untracked, gitignored) + one phantom `stats.sh` reference. |

**Primary prescription:** remove the `## 📊 GitHub Analytics · $ ./stats.sh --live` block (user-requested), fix the output-branch race, delete stray OS files, commit the orphaned workflow. Everything else is polish, phased below.

---

## 1. Design audit — apple-design lens (precise, ultra-premium detailing)

Reference: `apple-design` §§1–17. Judged against motion, materials, typography, foundations.

### 1.1 What is genuinely excellent (do not touch)

- **Single motion grammar.** `01,03,04,10,11,12` share identical keyframes (`wipe .22s` → `rise .18s` staggered at `.15s` steps, `blink 1.1s step-end`, `glow 2.2s`) with `cubic-bezier(.16,1,.3,1)`. This is apple-design §4 done right: critically-damped-default energy, zero bounce on non-momentum surfaces, interruptible CSS that never locks input. Verified in all six files.
- **Material system.** Every card: `linearGradient #0D1320→#07090E` + `scan` pattern (`fill-opacity 0.028`) + `1px #1E293B` hairline + `rx=12` + traffic-light dots with `gloss` radial highlight. Translucent-chrome thinking (§12) executed as a flat-SVG equivalent; hierarchy reads instantly.
- **Spatial consistency (§7).** Title bar at `y=30`, prompt at `y=58`, traffic lights at `cx=20/36/52, cy=15`, centered chrome title at `x=420`. Enter/exit paths are symmetric (wipe-in only, no exit) so nothing violates the symmetric-paths rule.
- **Narrative wayfinding (§16).** `boot → whoami --ascii → cat about → curl stack → metrics → ls stack --stream → contact → logout` answers *Where am I / Where can I go / How do I get out* at every scroll position. Terminal metaphor is familiar (§16-Familiarity) without being literal kitsch.
- **Reduced motion (§14).** All 8 SVGs gate animation behind `@media (prefers-reduced-motion: reduce)`; `13-stack-marquee.svg` correctly collapses its infinite `slide 26s linear` to `animation:none`. Verified by string inspection. No vestibular traps, no full-viewport loops, no brightness jumps.

### 1.2 Design defects (ranked)

| # | Severity | Finding | Evidence | apple-design rule broken |
|---|---|---|---|---|
| D-1 | **High** | Analytics widgets use `tokyonight`/`tokyo-night` theme — foreign palette inside a `#0D1320/#0C4A6E/#38BDF8` system. Four different vendors, four different typefaces, trophy grid `row=1 column=6` crams 6 trophies into one strip. | `README.md:98-107` — `theme=tokyonight`, `theme=tokyo-night` vs SVG system `#0D1320/#38BDF8` | §16-Craft (nothing is random; every color is a deliberate choice), §6-Simplicity (strip the unnecessary) |
| D-2 | Medium | `## 🛠️ Tech Stack` emoji heading breaks the `$ <cmd>` heading language every other section speaks (`$ cat about.md`, `$ ls projects/`, `$ ./play.sh`). | `README.md:34` vs `:25,53,81,86,109` | §16-Familiarity (things that look the same must behave the same) |
| D-3 | Medium | Section numbering restarts inconsistently: `[01] Systems, [02] Automations, [03] Academic, [04] Credentials`, then unnumbered Analytics + Arcade. | `README.md:53,81,86,91,95,109` | §16-Wayfinding |
| D-4 | Low | All 8 SVGs lack `<title>` — screen readers opening the SVG directly get no accessible name (the `<img alt>` covers README embedding, not direct open). | `grep <title> assets/*.svg` → 0 hits | §16-Flexibility (full range of abilities) |
| D-5 | Low | `02-ascii-portrait.svg` (35,564 chars, 59 text nodes, reveal cascade ≈ 2.5 s+) is the only card with multi-second staged reveal; on slow connections it is the LCP tail. | `assets/02-ascii-portrait.svg` size + `revealW .11s × N` delays | §1-Response (kill latency on the first paint) |

Design decision: D-1 is fixed by the user-requested Analytics removal. D-2/D-3 are intentional-heading polish — recommended, not applied without owner sign-off (see Phase 4, optional). D-4/D-5 are backlog.

---

## 2. Design audit — ui-ux-pro-max lens (delivery checklist)

Applied the skill's pre-delivery checklist to `README.md` + SVG system:

- [x] No emoji-as-icon in UI surfaces (SVG system uses real vector dots/gradients, no emoji glyphs).
- [x] Hover/layout-shift N/A (static README; SVG animations are transform/opacity-only — compositor-friendly per apple-design §11).
- [x] `cursor-pointer` N/A (no clickable cards).
- [x] Transitions 150–300 ms (wipe `.22s`, rise `.18s` — inside the band).
- [x] Keyboard focus N/A (README links are native anchors).
- [x] Alt text on every image — PASS (all 8 local SVGs + all externals carry `alt`).
- [x] Contrast — PASS on SVG system (`#F8FAFC` on `#0D1320` ≈ 15+:1; muted `#94A3B8` on dark ≈ 7+:1). **FAIL inherited from vendors** in Analytics block (tokyonight muted grays on dark) — removed with the block.
- [x] Borders visible in both color schemes — local system uses explicit `#1E293B` hairlines (not `white/10`).
- [~] Responsive: working-tree upgrade `width="840"` → `width="100%"` on all local SVGs is correct and already present (uncommitted). Residual risks: `readme-typing-svg` (fixed 840 internal width, no `width` attr) and `skillicons.dev` (16 icons, one row, wraps unpredictably on narrow viewports) — both external, both stay after Analytics removal. Recommend `width="100%"` wrapper discipline on future adds; not auto-rewritten (external render behavior unverifiable offline).
- [x] `prefers-reduced-motion` respected (all 8 SVGs).
- [x] Floating/sticky overlap N/A.

---

## 3. Frontend / performance audit

| # | Severity | Finding | Evidence |
|---|---|---|---|
| F-1 | **High** | Analytics block = 5 render-blocking third-party image pipelines (`github-readme-stats` ×2, `streak-stats.demolab`, `github-profile-trophy`, `activity-graph`) on every profile view. Slowest, least cacheable, most failure-prone part of the page; each can independently 404/rate-limit and leave a broken-image hole. | `README.md:97-107`; external-host inventory (5 analytics hosts) |
| F-2 | Medium | `skillicons.dev` single-row 16-icon strip has no width constraint; on mobile it overflows or shrinks to illegibility depending on GitHub's renderer. | `README.md:37` — no `width` attr |
| F-3 | Medium | `readme-typing-svg` hardcodes `width=840` with no responsive wrapper; fixed-pixel external render on narrow viewports. | `README.md:10` |
| F-4 | Low | Capsule header (`height=170`) + `<h1>` + sub-status line triple-announce the same identity (image text, heading text, status text). Intentional for SEO/a11y (profile search indexes the `<h1>`, not the image) — **keep**, documented here so nobody "dedups" it later. | `README.md:1-8` |
| F-5 | Low | No `stats.sh` file exists anywhere; the heading `$ ./stats.sh --live` is a phantom reference (narrative metaphor, but this one names a live-data script that doesn't exist). Removal resolves it. | `grep -rn stats.sh` → only `README.md:95` |

Performance note: local assets total ≈ 60 KB SVG (largest single file `02-ascii-portrait.svg` 35 KB). Removing Analytics deletes 0 local bytes but removes the dominant external LCP cost. Post-removal externals: capsule-render ×2, typing-svg, skillicons, komarev views, pacman/snake `raw.githubusercontent` output — a defensible minimum.

---

## 4. Security / privacy audit

| # | Severity | Finding | Evidence |
|---|---|---|---|
| S-1 | Medium | `pacman.yml` pins `abozanona/pacman-contribution-graph@main` — mutable floating ref; upstream force-push = silent behavior change in CI. | `.github/workflows/pacman.yml:17` |
| S-2 | Low | Both workflows request `contents: write` at job level (needed for the `output`-branch push, so legitimate) with no `concurrency` guard — overlapping scheduled + manual dispatches can interleave pushes to the same branch. Fix = `concurrency` group, not permission reduction. | `snake.yml:12-13`, `pacman.yml:12-13` |
| S-3 | Low | Analytics widgets phone home per view (komarev counter, vercel stats, demolab streak, trophy, activity-graph) — per-view IP/user-agent disclosure to 5 third parties + tracking-pixel semantics on a hiring surface. Removal shrinks the disclosure footprint to capsule/typing/skillicons/komarev. | external-host inventory |
| — | Info (clean) | No secrets, tokens, private emails, or internal URLs in tree. `GITHUB_TOKEN` is the auto-provisioned ephemeral token. `snake_metadata.py` is zero-dependency stdlib only (`glob/re/sys/datetime`), no network, no shell-out, no pickle. Contact surface is intentionally public (portfolio, LinkedIn, Gmail, LeetCode, HackerRank). | full-tree grep + `snake_metadata.py:1-69` |

No XSS surface: SVGs are static (no `<script>`, no event-handler attributes, no `foreignObject`); animations are pure CSS keyframes. Markdown links are all `https:`/`mailto:`.

---

## 5. CI / workflows audit — the live bug

| # | Severity | Finding | Evidence |
|---|---|---|---|
| C-1 | **Critical (data loss)** | `snake.yml` pushes `build_dir: dist` to `output` **without** `keep_history: true`, while `pacman.yml` pushes the same branch **with** `keep_history: true`. `crazy-max/ghaction-github-pages` without `keep_history` force-pushes a single-commit history containing only the current `dist` — so every midnight snake run **deletes the pacman SVGs**, and every 01:00 pacman run restores-then-orphans snake history. The two crons (`0 0 * * *`, `0 1 * * *`) guarantee daily mutual clobbering. | `snake.yml:33-39` (no `keep_history`) vs `pacman.yml:25-31` (`keep_history: true`) |
| C-2 | **High** | `.github/workflows/pacman.yml` is **untracked** (`??` in `git status`) — the pacman automation described in `README.md:119` does not exist on the remote and will never run until committed. | `git status --short` → `?? .github/workflows/pacman.yml` |
| C-3 | Medium | No `concurrency` group on either workflow; a slow run overlapping the next cron (or a manual `workflow_dispatch` during a scheduled run) pushes twice to `output`. | both `*.yml` lack `concurrency:` |
| C-4 | Low | `snake.yml` pins `Platane/snk@v3`, `actions/checkout@v4`, `crazy-max/ghaction-github-pages@v4` — major tags, mutable. Acceptable for a profile vanity workflow; full-SHA pinning recommended only if owner wants supply-chain maximalism. | `snake.yml:17,20,34` |
| C-5 | Info | `snake_metadata.py` edge behavior: `ok = all(process(...) for ...)` short-circuits — one malformed SVG skips the rest and exits 1, failing the job loudly. Correct fail-loud behavior for CI; no change. Date math (`SEP 2025 — SEP 2026` style rolling window, `REGEN … · DAILY`) is UTC-dynamic, no hardcoded rot. | `snake_metadata.py:60,64` |

---

## 6. Hygiene / dead-code audit

| # | Finding | Disposition |
|---|---|---|
| H-1 | `/.DS_Store` (10 KB) + `/.github/.DS_Store` (6 KB) exist on disk, untracked, gitignored | **Delete from disk** (Phase 2). Never tracked — `git ls-files \| grep -i ds_store` = empty. |
| H-2 | `## 📊 GitHub Analytics · $ ./stats.sh --live` block (`README.md:95-107`) + phantom `stats.sh` reference | **Remove block** (Phase 1, user-requested). No `stats.sh` file exists; nothing else references it. |
| H-3 | `docs/CV_All.pdf` (95 KB), linked at `README.md:89` | **Keep** — live reference, no duplicate. |
| H-4 | Retired-SVG risk: history shows retired SVGs were dropped in `ecb7d5c`; current `assets/` (8 files) maps 1:1 to live `README.md` references (`01,02,03,04,10,11,12,13`) | **Keep all 8** — zero orphans verified. |
| H-5 | Uncommitted working-tree improvements (capsule header/footer, `<h1>`, komarev views, Tech Stack block, `width 840→100%`, Arcade section) | **Keep** — they are the premium polish; this audit does not revert them. |
| H-6 | `.gitignore` covers OS cruft, IDE, Python, preview renders, logs | **Keep as-is** — correct, no gaps found for this repo shape. |

---

## 7. Phased removal + fix plan (executed in this order)

- [x] **Phase 0 — Audit (this file).** Evidence-backed findings, no code touched.
- [ ] **Phase 1 — Requested removal.** Delete `README.md` Analytics block (heading + 3 `<p>` image groups, `README.md:95-107` + surrounding blank lines). Leave `## 👻 Contribution Arcade` intact. Verify: `grep -rn "stats.sh\|GitHub Analytics" README.md` → empty.
- [ ] **Phase 2 — Disk hygiene.** `rm .DS_Store .github/.DS_Store`. Verify with `git status --short` (no deletions shown — files were never tracked) and `ls`.
- [ ] **Phase 3 — Workflow repair (minimal, behavior-preserving).** `snake.yml`: add `keep_history: true` (stops daily pacman wipe). Both workflows: add `concurrency: group: <snake|pacman>-output / cancel-in-progress: false` (serializes scheduled vs manual runs). No action-version changes (avoid unverifiable SHA churn); S-1/C-4 pinning stays a recommendation. `pacman.yml` itself is kept — commit it separately (owner action; this audit does not commit).
- [ ] **Phase 4 — Re-check (once).** YAML parse both workflows, SVG `viewBox` sanity, `grep` for `stats.sh`, `git diff --stat`, `git status --short`. Report results.
- [ ] **Phase 5 — Optional backlog (NOT applied without sign-off).** D-2 (emoji heading → `$ ls stack/` language), D-3 (renumber sections or drop numbers), D-4 (`<title>` in SVGs), D-5 (portrait reveal budget), S-1/C-4 (SHA-pinning), F-2/F-3 (responsive wrappers on external imgs).

---

## 8. What was deliberately NOT changed

1. Pacman + snake Arcade section, workflows' action versions, and all 8 local SVGs (content/visuals byte-identical except Phase-3 YAML keys).
2. Uncommitted premium polish in the working tree (capsule chrome, `<h1>`, Tech Stack, Arcade, `100%` widths) — preserved.
3. `docs/CV_All.pdf`, `.gitignore`, `snake_metadata.py` — verified clean, untouched.
4. No commits, pushes, or branch operations performed by this audit (owner decides when to commit Phases 1–3).

---

*Skill usage: design judgments rendered through `apple-design` (§§1,4,6,7,11,12,14,16) and `ui-ux-pro-max` (delivery checklist + contrast/type/spacing rules). Security judgments follow least-privilege + supply-chain-minimalism; CI judgments from workflow-file + `git status` evidence, not convention.*

---

# Round 2 — Upstream verification + Image-1 render fixes (2026-09-26)

## R2.1 Upstream source of truth

Fetched `https://github.com/abozanona/pacman-contribution-graph` (201 stars, 86 forks) and diffed our `pacman.yml` against its official "Integrate into Your GitHub Profile" guide:

| Upstream requirement | Our state before | Action taken |
|---|---|---|
| `uses: abozanona/pacman-contribution-graph@main` + `github_user_name` + optional `games` (comma-separated, default `pacman`) + optional `hide_month_labels` | Match (`games: 'pacman'`, no `hide_month_labels` = default `false`) | None — already correct |
| Push `dist` → `output` branch | Match (both workflows now `keep_history: true` after Round-1 C-1 fix) | None |
| Triggers: `schedule cron 0 0 * * *` + `workflow_dispatch` + **`push: branches: [main]`** | **Missing `push`** — graph SVGs 404 for every viewer until the first cron/manual run after push | **Added `push: branches: [main]`** to `pacman.yml` (mirrors upstream exactly) |
| Push action `crazy-max/ghaction-github-pages@v3.1.0` | We use `@v4` (newer) | None — v4 is current; v3.1.0 is the doc's pinned example, not a requirement |
| `<picture>` dark/light `srcset` → `output/[game]-contribution-graph[-dark].svg` | Match (`pacman-contribution-graph.svg` + `-dark.svg`) | None |
| "Run the workflow manually once after push" | Already documented under the Arcade block (`README.md:105,118`) | None |

`games` stays `'pacman'` (single-game = smallest `output` payload; upstream multi-game e.g. `'pacman,breakout'` is listed as optional backlog R2-R1 below).

## R2.2 Image-1 defects — diagnosis → fix

Screenshot evidence (dark GitHub render) showed three live defects at the top of the profile:

| # | Defect in Image 1 | Root cause | Fix applied |
|---|---|---|---|
| I-1 | **Broken header image** — alt text "Maithresh Vaddi header" with broken-image icon | `capsule-render.vercel.app` wave header fails to load (flaky third-party render host; zero informational value — pure decoration duplicating the `<h1>` + hero SVG identity) | **Removed capsule header AND footer divs** (same host, same failure mode). Identity now carried by `<h1>` (search-indexable, screen-reader-safe) + status line + `01-hero-whoami.svg`. −2 external requests. |
| I-2 | **Typing line clipped** — renders "AI/ML Engineer &", drops "Agentic Systems Builder" | `readme-typing-svg` canvas `width=840` leaves no margin for the 38-char line at `size=20`; long line clips at the canvas edge (worst on narrow viewports / camo re-scale) | **Canvas `width=840→920` + `width="100%"` attr** so the render scales into its container instead of clipping. Content lines untouched. |
| I-3 | **Generic monochrome badges** — all-white glyphs on black look stock, LinkedIn mark barely registers | All badges forced `logoColor=F8FAFC` (except Portfolio) — designer-hostile: brand marks lose recognizability | **Brand-color logos on the terminal-black base**: LinkedIn `0A66C2`, Gmail `EA4335`, LeetCode `FFA116`, HackerRank `2EC866`, Portfolio keeps accent `38BDF8`. Same `flat-square` system, now scannable at a glance. Per-link `<a>` wrappers preserved. |

Analytics (`stats.sh --live`) confirmed still absent — `grep` clean (see Re-check). Not reintroduced.

## R2.3 Recommended-changes list (applied vs backlog)

**Applied in Round 2:**
1. Remove capsule-render header + footer (I-1). ✅
2. Typing-SVG canvas hardening 840→920, responsive width (I-2). ✅
3. Brand-color badge logos, unified flat-square system (I-3). ✅
4. `pacman.yml`: add upstream `push: branches: [main]` trigger. ✅
5. Analytics stays deleted. ✅

**Recommended backlog (needs owner sign-off, NOT applied):**
- R2-R1: `games: 'pacman,breakout'` — second arcade game; doubles `output` payload, verify filenames before enabling.
- R2-R2: Pin `abozanona/pacman-contribution-graph@main` to a release SHA (supply-chain maximalism; upstream has no version tags, so this means tracking a commit SHA manually).
- R2-R3: `## 🛠️ Tech Stack` emoji heading → `$ ls stack/` terminal language (design-system consistency D-2).
- R2-R4: Renumber `[01]–[04]` + Arcade into one sequence, or drop numbers (D-3 wayfinding).
- R2-R5: `<title>` inside all 8 SVGs for direct-open screen readers (D-4).
- R2-R6: `02-ascii-portrait.svg` reveal-budget trim — slowest first paint (D-5).
- R2-R7: `skillicons.dev` 16-icon strip responsive wrap audit on mobile widths (F-2 residual).
- R2-R8: After push — manually dispatch both workflows once in Actions, then confirm the four `output` SVGs resolve (pacman ×2, snake ×2) before sharing the profile.

---

# Round 3 — Rounded designer-grade contact pills (2026-09-26)

## R3.1 Web research → chosen free option

Request: softer border-radius (no sharp rectangles) + ultra-premium production-level icons, best free web option. Researched 2026 guides + registries:

- **Chosen: Simple Icons (CC0, 3,400+ brand SVGs, 25k★)** — the same library shields.io itself renders via `logo=`. Verdict from guides: official brand colors + consistent style read as intentional; generic gray reads as copy-pasted.
- Rejected: staying on shields `flat-square` (radius 0 by definition — cannot satisfy the request), `for-the-badge` (still vendored-generic, off-palette), icon-emoji (violates ui-ux-pro-max delivery rules).
- Production move: stop renting shields renders; ship **local pills** built from official Simple Icons paths, themed to the card system. Zero external requests, fully controlled radius, byte-stable.

## R3.2 What was built — `assets/05–09-pill-*.svg`

| File | Label | Glyph source | Glyph color |
|---|---|---|---|
| `05-pill-portfolio.svg` (137px) | maithresh.sh | Simple Icons `vercel` path | `#38BDF8` (portfolio accent) |
| `06-pill-linkedin.svg` (107px) | LinkedIn | Simple Icons `linkedin` path | `#0A66C2` official brand |
| `07-pill-gmail.svg` (84px) | Gmail | Simple Icons `gmail` path | `#EA4335` official brand |
| `08-pill-leetcode.svg` (107px) | LeetCode | Simple Icons `leetcode` path | `#FFA116` official brand |
| `09-pill-hackerrank.svg` (122px) | HackerRank | Simple Icons `hackerrank` path | `#2EC866` official brand |

Shared designer system per pill (matches `01/03/04/10/11/12` card DNA): `h=32, rx=9` (soft-rounded, echoes card `rx=12` at small scale), bg `#0D1117`, `1px #1E293B` hairline, 15px glyph + JetBrains Mono 600 label `#F8FAFC`, `<title>` + `role="img"` for a11y. Widths computed from label length (mono advance 7.55px @12.5px). All 5 XML-validated. Numbering `05–09` fills the asset-sequence gap — no orphans.

Note: `linkedin` is absent from Simple Icons v15 CDN but present in `@latest` — all 5 paths pulled from `cdn.jsdelivr.net/npm/simple-icons@latest` in one consistent set.

## R3.3 README changes

1. Contact row: 5× shields `flat-square` → 5× local pills (`height="32"` uniform row, per-link `<a>` wrappers preserved).
2. Removed komarev `ghpvc` views counter — sharp-cornered, external tracker, off-palette; inconsistent with the new pill row. Revert one-liner if the count is wanted back: re-add `<img src="https://komarev.com/ghpvc/?username=MaithreshVaddi-27&style=flat-square&color=38BDF8" alt="Profile views"/>` inside the row.
3. PodEase `status-live` shields chip → `` `● LIVE` `` terminal text (kills the last sharp third-party badge ref; verified `grep` clean for shields/komarev/capsule/stats hosts).

## R3.4 Re-check (Round 3)

- `grep` banned hosts (`shields.io, komarev, capsule-render, stats.sh, GitHub Analytics, …`) → **CLEAN**.
- 5 pills XML-valid, `rx=9`, `<title>`, correct widths; full asset set now 13 SVGs, all referenced 1:1 in README (05–09 in contact row).
- Workflows untouched since Round-2 verification (still valid, `push` trigger + `keep_history` + `concurrency`).

## R3.5 Recommended-changes list (cumulative)

**Applied (Rounds 1–3):** Analytics block removed · output-branch wipe fixed · `concurrency` guards · capsule header/footer removed · typing canvas hardened · brand-color badges → local rounded pills · komarev removed · PodEase chip de-shieldsed · `.DS_Store` purged · `push` trigger aligned to upstream.
**Backlog (owner sign-off):** R2-R1 breakout game · R2-R2 SHA-pin `@main` · R2-R3/R4 heading language + renumber · R2-R5 SVG `<title>` for the 8 terminal cards · R2-R6 portrait reveal budget · R2-R7 skillicons mobile wrap · R2-R8 manual workflow dispatch + `output`-URL check · **R3-R1:** pill hover states are impossible in static SVG `<img>` — if interactive glow is ever wanted, it must be baked as a second asset + `<picture>` swap (not recommended; keep static).
