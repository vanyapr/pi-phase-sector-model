# Pull Request: Add exact proportional sector arithmetic

## Summary

This PR adds an exact integer module for proportional sector arithmetic:

```text
pifs/proportion.py
```

The module implements cross-base sector transforms without floating point arithmetic.

It supports:

- sector intervals;
- overlap ranges;
- containment/certifying ranges;
- exact binary/quaternary conversion;
- decimal zero block certifying cells;
- logarithmic resonance pair helpers;
- the named medium decimal resonance `pi^2456 ≈ 10^1221`.

## Why

`pi-fs locate` needs a strict layer for translating target sectors between grids.

Example:

```text
[0, 4^-1661) subset [0, 10^-1000)
```

Therefore:

```text
floor(4^1661 * {10^M pi}) = 0
    => 1000 decimal zeros at M + 1
```

This is a cross-base certificate, not a heuristic.

## Added files

```text
pifs/proportion.py
docs/proportional-sector-arithmetic.md
tests/test_proportion.py
```

## Key formulas

Overlap:

```text
B_min = floor(A N / M)
B_max = ceil((A + 1) N / M) - 1
```

Containment:

```text
B_min = ceil(A N / M)
B_max = floor((A + 1) N / M) - 1
```

where:

```text
M = Q^L
N = Q2^L2
```

## Tests

Includes tests for:

- exact `(4,L) <-> (2,2L)` mapping;
- `1000` decimal zeros -> quaternary certifying cell depth `1661`;
- small decimal zero block cases;
- brute-force overlap/containment on small grids;
- medium decimal resonance `K=1221, N=2456`.

## Notes

This does not claim to predict first occurrence beyond a finite horizon.
It provides the exact target/certificate transform layer required by `pi-fs locate`.
