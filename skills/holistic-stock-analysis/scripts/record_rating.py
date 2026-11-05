#!/usr/bin/env python3
"""Record a holistic buy-rating into the prediction track record (grading + training).

Every holistic report ends with a compact rating block (TICKER — Rating / Conviction /
Probability / Forecast / Targets / Key levels). This logs that block under
model='claude-holistic' so it is graded against real price action over time and kept as
training data — separate from, and comparable to, the local @2 model's own record. Same
parser/validator/grader as the local model, so the two are scored identically.

Usage:
  record_rating.py TICKER --file /tmp/holistic_TICKER/rating.txt
  echo "<rating block>" | record_rating.py TICKER
"""

import os as _export_os
import pathlib as _export_pathlib
import argparse
import glob
import sys

TG = str(_export_pathlib.Path(_export_os.environ.get('R2D2_WORKSPACE', str(_export_pathlib.Path(__file__).resolve().parents[3]))) / 'telegram-bots')
sys.path.insert(0, TG)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--file", help="file holding the rating block; omit to read stdin")
    ap.add_argument("--model", default="claude-holistic")
    a = ap.parse_args()
    ticker = a.ticker.upper().strip()

    raw = open(a.file).read() if a.file else sys.stdin.read()
    if not raw.strip():
        print("[record_rating] empty rating text — nothing logged.")
        return

    from shared import predictions
    try:
        entry = predictions.current_price(ticker)
    except Exception:
        entry = None
    charts = sorted(glob.glob(f"/tmp/holistic_{ticker}/chart_*.png"))

    pid = predictions.record_analysis(
        a.model, ticker, source="holistic", analysis_type="holistic",
        timeframes="1wk,1d,1h", entry_price=entry, raw_text=raw, chart_paths=charts,
    )
    p = predictions.parse_analysis(raw)
    print(f"[record_rating] logged #{pid} {a.model} {ticker}: "
          f"{p.get('rating') or '?'} / conv {p.get('conviction') or '?'} / "
          f"prob {p.get('probability')}% / t1 {p.get('target1_price')} / "
          f"inval {p.get('invalidation')} / entry ${entry} / {len(charts)} chart(s)")
    bad = predictions.consistency(p, entry)
    if bad:
        print(f"[record_rating] WARNING — stored as INVALID (excluded from track record): "
              f"{bad}\n  Fix the targets so they sit on the right side of price, then re-run.")


if __name__ == "__main__":
    main()
