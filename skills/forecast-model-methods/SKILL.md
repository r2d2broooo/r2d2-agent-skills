---
name: forecast-model-methods
description: How the live numpy r2d2 uncertainty range, regime context, walk-forward evaluation and evolving band calibration work.
metadata:
  source: shared/local_forecaster.py, shared/forecast_router.py, shared/forecast_backtest.py, shared/forecast_calibrate.py
  status: living-document
---

# How the Local Forecast Models Work

The forecast is **pure numpy, in-process** — no torch, no GPU, no external model
service. r2d2 is the sole active model. Analog, Kronos and TimesFM are retired and
must not appear in a live report.

This doc is the "how" behind the numbers — for interpreting output correctly and for
extending the engine safely. The golden rule: **every accuracy claim comes from the real
model on historically clipped data (`forecast_backtest.py`), never a fabricated or
hypothetical forecast.**

## The range engine

**r2d2 — `local_forecaster.py` (trend rider).** Closed-form, no sampling:
- Log-return drift = a damped blend of a median trailing **trend** (`drift_lookback`) and a
  short **mean-reversion** term (`mr_lookback`, `mr_weight`), plus an optional **TSMOM tilt**
  (`mom_weight`, gated by `regime_ma`) that nudges drift toward the sign of trailing momentum.
- Volatility from **EWMA** of log returns (`vol_span`); the ~1σ cone widens as `sigma·√h`
  (or a borrowed HAR-RV cone if `band_model="har"`).
- `predict(closes, horizon)` → `{path, low, high, mu, sigma}`. Tunables live in
  `data/forecast_params.json`.

## Regime context — `forecast_router.py`

Classifies the current tape with the **Kaufman Efficiency Ratio** (net move ÷ total
path length over `ER_WINDOW=25`). The regime describes the observed price path only;
it must not be used to recover or imply r2d2's retired direction.

`multi_horizon()` runs r2d2 once at the longest horizon and slices calibrated low/high
bands for **5 / 10 / 20 / 30** trading days (the **90d horizon was dropped** because its
evaluation support was too weak). Coverage and sample size must accompany each band when
available. Cross-sectional momentum is separate observed context, never forecast confidence.

## Evolving band calibration — `forecast_calibrate.py` + `forecast_calibration.py`

Raw ~1σ bands can be miscalibrated and the error changes by horizon. The router
therefore scales each horizon's band by a factor **learned from a declared
train/test walk-forward, not guessed**:

- `forecast_calibrate.py` walks every ticker forward (only past data at each cutoff → no
  lookahead), computes the 0.68-quantile of `|realized − mid| / halfband` per horizon, and
  with `--save` writes the factors to `data/forecast_calibration.json`.
- `forecast_router` loads that file at runtime (`forecast_calibration.band_scale()`), so the
  bands **self-correct as history accrues**. A fresh checkout with no file uses built-in
  fallback factors.
- Re-run periodically or after a volatility regime shift. Long-horizon factors are the least
  stable (dispersion is regime-dependent) — another reason the calibration must evolve.

## What the measured record says (be honest about it)

Do not embed a fixed "latest" result in this skill. Read the saved Backtest result for
the exact requested horizon and report:

- non-overlapping sample size and ticker coverage;
- direction hit-rate with its point-level Wilson 95% interval;
- MAPE and improvement versus persistence;
- no-change, always-up and always-down direction baselines;
- the caveat that cross-ticker/date correlation can make the interval too narrow.

The centre path and direction are retired from every live surface. Only calibrated
low/high bounds, exact-horizon coverage, and sample size may leave the engine.

## Division of labor

These models have **zero notion of news, earnings, fundamentals, flows, or setups** — they are
pure price-shape statistics. Everything else (catalysts, valuation, insider/institutional flows,
relative strength as *conviction*) belongs to the holistic-analysis layer that wraps them. The
forecast is one input the analyst modulates, never the verdict.

## Open questions / future work

- Test changes to r2d2 against empirical interval coverage and naive volatility bands on
  the non-overlapping walk-forward harness; directional metrics are archive research only.
- Surface **valuation-percentile** and **insider-cluster** signals as forecast *confidence*
  modulators (live-only; can't be cleanly backtested point-in-time from web captures).
- Periodic **auto-recalibration** (scheduled `forecast_calibrate.py --watchlist --save`).
- Re-tune model params (`forecast_tune.py`) with strict out-of-sample validation before any
  live param change — never overwrite live params on an in-sample fit.
