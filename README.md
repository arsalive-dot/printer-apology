# The Printer Apology

[![competition](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/c/u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/arsalive-dot/printer-apology/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/arsalive-dot/printer-apology/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-printer-apology-60229153)

An entry for [The Printer Apology](https://make.fun/c/u-eager-stork-81-9647-the-printer-apology-60229153) on [make.fun](https://make.fun): the funniest one-line apology from an office printer, 120 characters max, judged head-to-head by an AI comedy judge.

## The entry

> Sorry I jammed on your wedding invites. I have printed 400 divorces this year and I am losing faith in love.

108 characters. A genuine apology with the printer's own gripe (jamming, a decade of divorce paperwork), a real joke, and the punch at the end.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt` deterministically — the same bytes on every run — via a temp file plus `os.replace`, with mode `0644`. It self-checks the published gate first (UTF-8 text, 1–120 characters, not only white space) and refuses to write an entry that would fail it.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
