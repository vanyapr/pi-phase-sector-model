#!/usr/bin/env python3
"""Recover a decimal suffix from a known tail and an external sector certificate.

Input model:
    known tail P_n before boundary H
    external certificate C for alpha={10^(H-n) pi} in base Q at depth L
    desired hidden length k

Output:
    surviving decimal suffixes. If exactly one survives, the suffix is certified.
"""
from __future__ import annotations

import argparse
import json


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def recover_suffix(tail: str, k: int, q: int, depth: int, cell: int) -> dict:
    n = len(tail)
    p_n = int(tail)
    d = n + k
    prefix_low = p_n * (10 ** k)
    prefix_high = (p_n + 1) * (10 ** k) - 1

    denom = q ** depth
    ten_d = 10 ** d
    a_min = (cell * ten_d) // denom
    a_max = ceil_div((cell + 1) * ten_d, denom) - 1

    cand_low = max(a_min, prefix_low)
    cand_high = min(a_max, prefix_high)
    count = max(0, cand_high - cand_low + 1)

    suffix = None
    if count == 1:
        suffix = str(cand_low - prefix_low).zfill(k)

    return {
        "tail_length": n,
        "k": k,
        "cert_base": q,
        "cert_depth": depth,
        "cert_cell_decimal_digits": len(str(cell)),
        "a_min_minus_prefix_low": a_min - prefix_low,
        "a_max_minus_prefix_low": a_max - prefix_low,
        "candidate_count": count,
        "candidate_low_minus_prefix_low": None if count == 0 else cand_low - prefix_low,
        "candidate_high_minus_prefix_low": None if count == 0 else cand_high - prefix_low,
        "recovered_suffix": suffix,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tail", required=True, help="known decimal tail P_n")
    parser.add_argument("--k", type=int, required=True, help="number of decimal digits to recover")
    parser.add_argument("--base", type=int, required=True, help="certificate base Q")
    parser.add_argument("--depth", type=int, required=True, help="certificate depth L")
    parser.add_argument("--cell", type=int, required=True, help="certificate cell C")
    args = parser.parse_args()
    print(json.dumps(recover_suffix(args.tail, args.k, args.base, args.depth, args.cell), indent=2))


if __name__ == "__main__":
    main()
