---
name: trading-wiki
description: Maintain the per-ticker LLM Wiki — a compounding markdown knowledge base for stocks. Use when asked to update/read/build a ticker's wiki page, after a holistic analysis, or to recall what we know about a name. Karpathy LLM-Wiki pattern.
---

# Trading Wiki

A compounding, interlinked markdown knowledge base — one page per ticker — that is the
**storage layer for [[holistic-stock-analysis]]**. Instead of re-deriving everything from
raw captures on every query, each analysis is compiled into a durable page that grows over
time. Source of truth lives on disk; the user views/edits it in the dashboard **Trading
Wiki** tab.

- **Root:** `<workspace>/trading-wiki/` (`tickers/<T>.md`, `entities/<name>.md`, `WIKI.md` index)
- **Schema/config:** `<workspace>/trading-wiki/WIKI_SCHEMA.md` — read it; it defines page
  structure, provenance tags, and the maintenance rules. This skill is the *how-to-run*.
- **Engine:** `<workspace>/trading-wiki/scripts/wiki.py` (pure stdlib, deterministic only).

## Division of labor (important)
- **wiki.py** does only the mechanical parts: the `<!--SNAPSHOT-->` facts block, change-log
  line, index, lint. **It never writes narrative.**
- **I (Claude)** write the narrative: Thesis / Fundamentals / Catalysts / Flows / Cross-links
  / Open questions, synthesized from the captures, with provenance tags.
- **The user** edits freely in the dashboard. **User-written sections are authoritative —
  never overwrite them silently.** The Snapshot block is the only machine-owned region.

## Workflow: update a ticker after a holistic analysis
1. Ensure captures exist: `/tmp/holistic_<T>/` (run the holistic gather if not — see
   [[holistic-stock-analysis-skill]]).
2. `python3 <workspace>/trading-wiki/scripts/wiki.py ingest <T>`
   → refreshes the Snapshot from `local.txt` (yfinance), appends a change-log line, and
   prints the list of raw captures to synthesize from.
3. **Read those captures** (finviz/earningshub/quiver/x/aimode `.txt`). Then Edit the page:
   - Update Thesis (don't wipe history — evolve it; note stance/conviction changes).
   - Refresh Fundamentals & trend, append dated Catalysts & events, update Flows & sentiment.
   - Tag every claim `[FACT src]` / `[EST]` / `[USER]`. Never write a number not in a capture.
   - **Cross-check Layer-2 numbers against the Snapshot (Layer-1 anchor).** On conflict,
     trust the anchor and leave a change-log line noting the discrepancy (this is the whole
     point — e.g. AMC: X widget mcap was stale $1.6B vs $2.06B anchor; Quiver news feed was
     polluted with Amcor/AMCR headlines — both flagged, not imported).
   - Add a Change-log line for any thesis change.
4. Preserve the `<!--SNAPSHOT-->`…`<!--/SNAPSHOT-->` block byte-for-byte (ingest owns it).

## Other operations
- `wiki.py new <T>` — create a page from template (no-op if exists).
- `wiki.py query <T>` — print a page; **load it into context before answering about that
  ticker** so you build on prior knowledge instead of starting cold.
- `wiki.py list` — pages + staleness (>30d = stale).
- `wiki.py lint` — stale pages, orphan `[[links]]`, missing sections, TODO/CONFLICT markers.
  Run after edits. Orphan links to not-yet-created pages are fine (forward references).
- `wiki.py index` — rebuild `WIKI.md` (also auto-run when the user saves via the dashboard).

## Dashboard
Trading Wiki tab (`/api/wiki`, `/api/wiki/{T}` GET/PUT in dashboard `main.py`): card list →
page view with rendered markdown + an Edit mode (raw markdown textarea, Save). User edits
land straight in the files I read, so we share one source of truth.

## Recall habit
When the user asks about a ticker we've covered, `wiki.py query <T>` first. The page is the
accumulated thesis — answer from it, then update it if the analysis adds something new.
[[holistic-stock-analysis-skill]] · [[trading-chart-backtest-tools]] · [[forecast-models]]
