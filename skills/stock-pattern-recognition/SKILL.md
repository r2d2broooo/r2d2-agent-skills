---
name: stock-pattern-recognition
description: Use for chart-pattern research, catalyst checklists and data-extraction guidance. r2d2 is the sole active forecaster and has no named-pattern or catalyst awareness.
metadata:
  status: living-document, expanded as new sites/setups are reviewed
  source: screen-recording walkthroughs with the user + qullamaggie.com
---

> ## Chart-reading knowledge — STILL LIVE (reviewed 2026-08-23)
>
> This is chart-pattern vocabulary, and the doctrine uses it: `prompts/docs/trading_doctrine.md` §6
> explicitly asks for higher lows, bull flags, cup-and-handle, consolidation into a breakout and the
> retest after one. Read this for HOW to see structure.
>
> **Execution caveat.** Pattern names are vocabulary for describing a chart, not a checklist to
> satisfy — a clean chart with no textbook name beats a textbook name on a messy chart. The cloud
> bot selects the exact entry, invalidation/stop, target, review point and exit thesis from current
> evidence. Never import the historical ATR, R-multiple, time, position-size or exposure examples
> below as live rules. The only hard loss boundary is no wider than -10%; never average down.

# Stock Pattern Recognition & Research Methodology

This is the growing, curated "skill" for how to read charts, what data to pull from
which site, and which catalysts/setups matter. r2d2 is pure price-history extrapolation with no concept of named chart patterns or catalysts, so it cannot replace this research layer.

## 1. Historical Pattern Examples (Qullamaggie's 3 Timeless Setups)
Source: https://qullamaggie.com/my-3-timeless-setups-that-have-made-me-tens-of-millions/

**Historical examples only — not cloud-bot constraints:**
- The example entries, stops, targets, partial-sale timing and position sizes below explain how a
  pattern can be read. They do not define a live trade.
- For a cloud decision, use the current daily chart and full evidence bundle to choose a bespoke
  allocation and recorded entry/exit plan. There is no position, balance or exposure cap; the
  paper ledger remains finite-cash-accounted.

### Breakout
- Find stocks leading on 1-month / 3-month / 6-month performance.
- Structure: (1) big move higher (30-100%+) over 1-3 months, (2) orderly pullback/
  consolidation with higher lows, tightening range, price surfing the rising 10/20-day
  (sometimes 50-day) MA for 2 weeks-2 months, (3) range-expansion breakout.
- Entry: opening range highs (1/5/60-min candle) or daily-chart breakout.
- Stop: lows of day, never wider than ATR/ADR.
- Manage: sell 1/3-1/2 at day 3-5, move stop to breakeven, trail rest on 10-day
  (beginner) or 20-day MA, exit on first CLOSE below it.
- Visual forms: high tight flags, flat/symmetrical/descending triangles, channels.
  Works on daily/weekly/intraday (1-5 min = "Holy Grail").

### Episodic Pivot (EP)
- Unexpected good news on a (often neglected) stock - mainly earnings/guidance, but
  also regulatory, biotech trial/FDA, macro/political.
- Requirements: gap up 10%+, big volume (multiples of average) in pre-market or first
  5-10 min after open. For earnings EPs: big EPS/revenue growth (mid/high/triple-digit
  %), significant beat vs. estimates. Best when stock hasn't already rallied 3-6 months.
- Entry: opening range highs (1/5/60-min). Stop: lows of day, trail 10/20-day MA once
  clear of initial stop. Can produce multi-month/year moves (e.g. a major chipmaker's
  2016 earnings EP led to a ~doubling over the following 6 months).

### Parabolic Move (reference pattern; not a live short strategy)
- This is historical pattern research only. The live system is long-only; do not recommend a parabolic short.
- "Rubber band" snapback after a stock is overstretched. Riskiest setup.
- Setup: up 50-100%+ in days/weeks (large cap) or 300-1000%+ (small cap), 3-5+
  consecutive up days, often accelerating near the end.
- Entry (short): opening range lows, or wait for first red 5-min candle, or a bounce
  into VWAP that then fails. Stop: highs of day or VWAP reclaim. Target: 10/20-day MA.
- Parabolic LONG variant: after a parabolic short drops 50-60%+ in days, that washed-out
  low can set up a long (entry on opening range highs / first green 5-min candle).
- Historically a smaller payoff than Breakout/EP, but a higher hit rate.
  "Don't be too early."

**Philosophy**: low-risk tight entries on fast movers, aiming for 5-20x+ initial risk;
25-30% win rate can be very profitable if losses are small and winners are large.
Stock/group price action trumps macro view, but macro still matters for sizing/exposure.

## 2. Catalyst Checklist (news/fundamentals layer)
- **Earnings trend**: look at trend/acceleration, not just the latest print - recent
  growth acceleration is a positive catalyst.
- **Big deals/contracts, partnerships, strategic investments, new product launches** -
  all strong catalysts worth flagging.
- **Macro/political events** that could affect the business.
- Analyst rating gauges (e.g. TradingView's "Strong Buy" summary): weak/secondary
  signal - note if positive, don't weight heavily, ignorable when noisy.

## 3. Per-Site Data Extraction

### TradingView
- Chart toolkit: simple moving averages, volume, CVD (cumulative volume delta),
  trendlines, and pattern recognition (bull flags, price compression, mean reversion,
  mean undercuts, breakouts). Use other indicators only if relevant to the setup -
  not a fixed checklist.
- Symbol search: search bar -> Symbols/Ideas/Scripts/People, filter by
  Stocks/Funds/Futures/Forex/Crypto/Indices/Bonds/Economy/Options.

### Finviz
- Homepage: market overview header (major indices/futures), sector heatmap,
  top gainers/losers/news - useful for relative-strength/market context.
- Stock page fundamentals table: P/E, Fwd P/E, PEG, EPS, Sales, margins, insider
  ownership %, short float, etc. - compare against sector/historical norms.
- EPS/Sales growth bar charts (quarterly + annual): trend/acceleration, same approach
  as earnings above.
- Ownership/insider section: insider transactions + institutional ownership chart.
- News section (bottom of stock page): recent headlines - check for catalysts/events.

### Quiver Quantitative
- Has Congress trading, whale/institutional activity, insider trading, institutional
  ownership treemap, patents, government contracts, CNBC personality picks, ETF
  holdings, "Smart Score".
- Per the user: these are **secondary/noisy** - treat as supplementary extra points,
  not primary signals. The core signal stays earnings, price/volume/charts, news, and
  macro events (consistent across all sites). Revisit weighting once core pipeline
  is in place.

### Earnings Hub (retired)
- Retired data source. Do not use it for earnings, news, scores or short-interest claims; use the current market-data and verified news sources instead.

### X (Twitter)
- Cashtag search (`$TICKER`, Top/Latest/People/Media/Lists): real-time breaking
  news, analyst commentary, and price-action threads from finance accounts - a
  faster-moving complement to Finviz/Earnings Hub news sections.
- "What's happening"/Today's News sidebar: trending topics with post-volume - good
  for spotting macro/market-moving events that could affect a sector or the
  broader market.
- Following feed (curated finance accounts, e.g. TweetSpider, Cheddar Flow): chart
  setups/trade ideas and price-action screenshots from trusted sources - same
  pattern-recognition lens as the core setups above.

## 4. Forecast Model Role (r2d2)
- r2d2 is the sole active price-history forecast. It has no pattern, news or catalyst awareness.
- Use it only as corroborating context when its current exact-horizon calibration is available. Its path and band are not a probability or trade trigger; report any disagreement with the structural read.

## 5. Price/Volume Behavior Patterns (empirical, from watchlist study 2026-06-16)

### Volume Dry-Up (VDU) Before Breakouts
During consolidation, daily volume progressively declines to 70-100% of the 20-day average
as weak sellers are exhausted. The subsequent breakout day's volume surge (1.3-2x+) contrasts
sharply. Empirically confirmed: STX vol was 0.81x avg before its +40.8% follow-through move.

### Volume After the Move = Key Diagnostic
- **Vol declining after** (<1.0x avg): healthy continuation — MU +17%, STX +38% followed
- **Vol expanding after** (>1.5x avg): distribution/reversal risk — TER vol 1.5-1.65x after
  breakout, then reversed -10% to -15% over 20 days

### Candle Quality on Breakout Day
Best entries: body >60% of range + close-near-high >70% + rel_vol >1.5x
Example: ACMR 5/26 → 2.1x vol, 68% body, 100% CNH = textbook EP
Dangerous wick: VECO 5/6 → 3.4x vol, 3% body = giant wick = exhaustion top
Climactic top: ALAB 6/11 → body 96%, CNH 99% after +70% run = exhaustion warning

### Breakout Retest
After a genuine breakout, price often returns to test the broken resistance (now support).
Retest entry has better risk/reward if: pullback volume < breakout volume, price holds the
level, a reversal candle forms at support. Failed retest = breakout was false.

## 6. Chart Patterns (from pattern study, 2026-06-16)

### False Breakout Identification
Price breaks above resistance but closes back BELOW it on low/average volume. Key tells:
wick/tail at resistance level, close below the breakout bar's midpoint, no volume surge.
Most breakouts fail — wait for a volume-confirmed CLOSE above resistance.

### Cup and Handle
Bullish continuation: rounded U-shaped cup after a prior uptrend → small flag/handle
(5-15% pullback, declining vol, tight range) → volume-confirmed breakout above cup high.
Target = cup depth added to breakout level.

### Wedge
Rising wedge (bearish) = higher highs + higher lows within converging trendlines, each
high weaker than the last. Falling wedge (bullish) = reverse. Breakout goes OPPOSITE to
wedge slope. Volume contracts within wedge; expands on breakout.

### Head and Shoulders
Left shoulder → head (higher high) → right shoulder (lower high). Neckline breakout = short.
Stronger signal when right shoulder is significantly lower than left. Inverse H&S = bullish.

### Triple Top / Triple Bottom
Three tests of same resistance/support with declining volume each attempt = exhaustion.
Breakout through pullback lows/highs confirms reversal. Often violent when it triggers.

### Triangles
Symmetrical: converging trendlines = coiling. Ascending (flat resistance + rising support) =
bullish bias. Descending (flat support + declining highs) = bearish bias. Volume must contract
during formation; first 2/3 of the triangle provides the most reliable breakouts.

### Parabolic Move Anatomy
Accelerating gains, steepening slope, candles no longer overlap prior day's range. Ends with
volume climax (3-5x avg) on wide-range reversal day. Subsequent decline typically ≥50% of
gains at 2-3x the ascent speed. → Treat as a reversal-risk warning; no live short strategy is authorised.

## Open / To Be Added
- More sites pending walkthrough (candidates seen so far: Gmail - tbc with user).
- Trading strategy fine-tuning session planned (user requested 2026-06-16, scheduled 2026-06-18).
- Once stable, intended to be published externally - keep entries factual, sourced,
  and free of account-specific/private info.
