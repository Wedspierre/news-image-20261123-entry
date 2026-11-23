# Monday 23 November 2026: 36 stories, 7 regions — COP31 collapses, Ukraine peace push, Nvidia SEC probe

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Wedspierre/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Wedspierre/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One image that sums up the world news of **Monday 23 November 2026**: a newspaper
front page drawn from scratch with Python/PIL — masthead, market ticker, one lead
story, six story cards and 29 one-line briefs across 7 regions.

**Lead:** COP31 collapses in Antalya — nearly 200 nations leave with no climate
deal after the EU rejects a final text that never mentions fossil fuels, the first
COP to fail since Copenhagen in 2009. **Also inside:** the US presses for a
Ukraine–Russia peace deal by early January; Houthis claim a strike on Saudi
Arabia's Rabigh refinery; Nvidia falls 14% as the SEC examines its accounting;
Mexico captures FBI Top Ten fugitive "El Chapo Isidro"; ~50 workers missing after
a candy-factory fire in Java; South Korea's education minister quits over an
AI exam-cheating scandal.

## How it works

- `draw.py` renders `entry.png` (1024×1024, PNG) from fixed text and vector
  shapes — no network, no AI images, fully deterministic.
- `main.ts` (Node 22, stdlib only) validates `entry.png` (PNG magic, ≤ 1 MiB)
  and copies it to `$MAKEFUN_OUTPUT_DIR` (default `/output`), verifying the
  output bytes match.

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Sources

AP, Reuters, AFP, NPR, Financial Times, The Hindu, Indian Express, Chess.com —
every headline verified against reporting of 23 November 2026 (or first reported
that day). Full per-story source list: see `TRANSCRIPT.md`.
