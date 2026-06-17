#!/usr/bin/env python3
"""Compute a decimal continuation from a known tail and an external sector certificate.

Input data:
  H is only metadata here.
  P_n is the known decimal tail of length n before the boundary.
  C/Q^L is a sector certificate for the local phase {10^(H-n) pi}.

The script performs the proportional intersection:

  [floor(C*10^(n+k)/Q^L), ceil((C+1)*10^(n+k)/Q^L)-1]
  intersect
  [10^k P_n, 10^k(P_n+1)-1]

If one integer A remains, the next k digits are A - 10^k P_n.
"""
from __future__ import annotations

import argparse
import json


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def continue_boundary(tail: str, k: int, q: int, depth: int, cell: int) -> dict:
    n = len(tail)
    p = int(tail)
    cert_den = q ** depth
    decimal_den = 10 ** (n + k)

    a_min = (cell * decimal_den) // cert_den
    a_max = ceil_div((cell + 1) * decimal_den, cert_den) - 1

    prefix_low = (10 ** k) * p
    prefix_high = (10 ** k) * (p + 1) - 1

    low = max(a_min, prefix_low)
    high = min(a_max, prefix_high)
    count = max(0, high - low + 1)

    result = {
        "tail_length": n,
        "k": k,
        "cert_base": q,
        "cert_depth": depth,
        "cert_cell_digits": len(str(cell)),
        "decimal_range": [a_min, a_max],
        "prefix_range": [prefix_low, prefix_high],
        "intersection": [low, high] if count else None,
        "candidate_count": count,
        "next_digits": None,
    }
    if count == 1:
        y = low - prefix_low
        result["next_digits"] = str(y).zfill(k)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tail", required=True, help="known decimal tail before boundary")
    parser.add_argument("--k", type=int, required=True, help="number of decimal digits to recover")
    parser.add_argument("--cert-base", type=int, required=True)
    parser.add_argument("--cert-depth", type=int, required=True)
    parser.add_argument("--cert-cell", type=int, required=True)
    args = parser.parse_args()
    print(json.dumps(continue_boundary(args.tail, args.k, args.cert_base, args.cert_depth, args.cert_cell), indent=2))


if __name__ == "__main__":
    main()
