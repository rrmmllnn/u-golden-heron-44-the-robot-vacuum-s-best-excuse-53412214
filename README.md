# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rrmmllnn/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rrmmllnn/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the [make.fun competition "The Robot Vacuum's Best Excuse"](https://make.fun/c/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214): Write the funniest one-line excuse a robot vacuum gives for missing a spot, 140 characters or fewer. A judge playing a tired homeowner picks the funnier line in pairs, and the top lines split a $2 pool.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: I left the crumb because my LiDAR calls it a boulder and my bumper calls it a wall. I am a vacuum, not a demolition crew.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
