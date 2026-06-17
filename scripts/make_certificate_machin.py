#!/usr/bin/env python3
"""Build an external sector certificate from Machin's formula.

This reference script is intended for moderate horizons and reproducible
experiments.  For world-record horizons, the same mathematical object should be
computed by optimized binary-splitting / interval-arithmetic implementations.
"""
from __future__ import annotations

import argparse
import json
import math


def machin_pi(dps: int):
    try:
        import mpmath as mp
    except ModuleNotFoundError as exc:
        raise RuntimeError("make_certificate_machin.py requires optional dependency: mpmath") from exc

    mp.mp.dps = dps
    return 16 * mp.atan(mp.mpf(1) / 5) - 4 * mp.atan(mp.mpf(1) / 239)


def certificate_from_machin(h: int, n: int, k: int, q: int, offset: int, guard: int = 80) -> dict:
    start = h - n
    if start < 0:
        raise ValueError("h must be >= n")
    d = n + k
    depth_min = math.ceil(d * math.log(10, q))
    depth = depth_min + offset
    digits_needed = start + math.ceil(depth * math.log10(q)) + guard + 5
    pi_val = machin_pi(digits_needed + 20)
    s = mp.nstr(pi_val, n=digits_needed + 5).split(".")[1]
    s = (s + "0" * digits_needed)[:digits_needed]
    local_digits = math.ceil(depth * math.log10(q)) + guard
    suffix = s[start : start + local_digits]
    cell = (int(suffix) * (q ** depth)) // (10 ** local_digits)
    return {
        "H": h,
        "n": n,
        "k": k,
        "start": start,
        "base": q,
        "depth_min": depth_min,
        "depth": depth,
        "offset": offset,
        "guard": guard,
        "cell": cell,
        "cell_decimal_digits": len(str(cell)),
        "formula": "pi = 16 atan(1/5) - 4 atan(1/239)",
        "digits_needed": digits_needed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--H", type=int, required=True)
    parser.add_argument("--n", type=int, default=100)
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--base", type=int, default=16)
    parser.add_argument("--offset", type=int, default=2)
    parser.add_argument("--guard", type=int, default=80)
    args = parser.parse_args()
    try:
        result = certificate_from_machin(args.H, args.n, args.k, args.base, args.offset, args.guard)
    except RuntimeError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
