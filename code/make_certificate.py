#!/usr/bin/env python3
"""Build a cross-base sector certificate for an artificial boundary.

This reference script uses Machin's formula

  pi = 16 atan(1/5) - 4 atan(1/239)

through mpmath to produce a sector cell

  C = floor(Q^L {10^(H-n) pi}).

It is intended as a compact reproducibility helper for the paper's Experiment 018,
not as a world-record-scale implementation.
"""
from __future__ import annotations

import argparse
import json
import math


def load_mpmath():
    try:
        import mpmath as mp
    except ModuleNotFoundError as exc:
        raise RuntimeError("code/make_certificate.py requires optional dependency: mpmath") from exc
    return mp


def machin_pi(dps: int, mp):
    mp.mp.dps = dps
    return 16 * mp.atan(mp.mpf(1) / 5) - 4 * mp.atan(mp.mpf(1) / 239)


def make_certificate(H: int, n: int, q: int, depth: int, guard: int = 80) -> dict:
    mp = load_mpmath()
    start = H - n
    needed = start + math.ceil(depth * math.log10(q)) + guard + 10
    pi_val = machin_pi(needed + 30, mp)
    s = mp.nstr(pi_val, n=needed + 5).split(".")[1]
    p = math.ceil(depth * math.log10(q)) + guard
    suffix = s[start:start + p]
    cell = (int(suffix) * (q ** depth)) // (10 ** p)
    return {
        "H": H,
        "tail_length": n,
        "phase_start": start,
        "cert_base": q,
        "cert_depth": depth,
        "cert_cell": cell,
        "cert_cell_digits": len(str(cell)),
        "decimal_digits_used_for_cell": p,
        "source": "Machin formula: 16 atan(1/5) - 4 atan(1/239)",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--H", type=int, required=True)
    parser.add_argument("--tail-length", type=int, default=100)
    parser.add_argument("--cert-base", type=int, default=16)
    parser.add_argument("--cert-depth", type=int, required=True)
    parser.add_argument("--guard", type=int, default=80)
    args = parser.parse_args()
    try:
        result = make_certificate(args.H, args.tail_length, args.cert_base, args.cert_depth, args.guard)
    except RuntimeError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
