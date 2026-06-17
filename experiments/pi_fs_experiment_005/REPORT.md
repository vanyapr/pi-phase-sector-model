# pi-fs experiment 005: finite matrix-sector locate MVP

## Goal

Build and test the "boring but strict" locate engine:

```text
target -> sector transform -> sparse finite index lookup -> certificate -> resonance coordinates
```

This experiment uses the mixed layer:

```text
B = 10, Q = 4
```

That means the phase orbit is decimal:

```text
u_M = {10^M pi}
```

but the certification/index grid is quaternary:

```text
a_M = floor(4^Lmax u_M)
```

This is the layer needed to certify decimal targets such as zero blocks using quaternary cells.

## Index parameters

```json
{
  "H_decimal_positions": 500000,
  "Lmax4": 16,
  "N4_cells_total": 4294967296,
  "occupied_cells": 499975,
  "occupancy_fraction": 0.00011640950106084347,
  "decimal_guard_digits_P": 34,
  "build_seconds": 0.7973825931549072,
  "source": "generated decimal pi digits with mpmath",
  "gen_seconds": 2.983380079269409,
  "first_80_decimal_digits": "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
}
```

## Locate query results

| label      | kind              |   pattern |   D |   A_decimal |   contained_cells | contained_range        |   intersect_cells | intersect_range        |   boundary_cells |   direct_first_M |   direct_first_position |   direct_count_in_H |   contained_locate_M |   contained_locate_position |   contained_occupied_cells_in_range |   contained_cell_returned | contained_verified_direct   |   intersect_locate_M |   intersect_locate_position |   intersect_occupied_cells_in_range |   intersect_cell_returned | intersect_verified_direct   | finite_index_matches_direct_first   |   contained_q1221 |   contained_r1221 |   intersect_q1221 |   intersect_r1221 |
|:-----------|:------------------|----------:|----:|------------:|------------------:|:-----------------------|------------------:|:-----------------------|-----------------:|-----------------:|------------------------:|--------------------:|---------------------:|----------------------------:|------------------------------------:|--------------------------:|:----------------------------|---------------------:|----------------------------:|------------------------------------:|--------------------------:|:----------------------------|:------------------------------------|------------------:|------------------:|------------------:|------------------:|
| zero_1     | zero_block        |         0 |   1 |           0 |         429496729 | 0..429496728           |         429496730 | 0..429496729           |                1 |               31 |                      32 |               49915 |                   31 |                          32 |                               49911 |               1.23875e+08 | True                        |                   31 |                          32 |                               49911 |               1.23875e+08 | True                        | True                                |                 0 |                31 |                 0 |                31 |
| zero_2     | zero_block        |        00 |   2 |           0 |          42949672 | 0..42949671            |          42949673 | 0..42949672            |                1 |              306 |                     307 |                5003 |                  306 |                         307 |                                5002 |               2.83739e+07 | True                        |                  306 |                         307 |                                5002 |               2.83739e+07 | True                        | True                                |                 0 |               306 |                 0 |               306 |
| zero_3     | zero_block        |       000 |   3 |           0 |           4294967 | 0..4294966             |           4294968 | 0..4294967             |                1 |              600 |                     601 |                 483 |                  600 |                         601 |                                 483 |               2.44009e+06 | True                        |                  600 |                         601 |                                 483 |               2.44009e+06 | True                        | True                                |                 0 |               600 |                 0 |               600 |
| zero_4     | zero_block        |      0000 |   4 |           0 |            429496 | 0..429495              |            429497 | 0..429496              |                1 |            13389 |                   13390 |                  50 |                13389 |                       13390 |                                  50 |          389618           | True                        |                13389 |                       13390 |                                  50 |          389618           | True                        | True                                |                10 |              1179 |                10 |              1179 |
| zero_5     | zero_block        |     00000 |   5 |           0 |             42949 | 0..42948               |             42950 | 0..42949               |                1 |            17533 |                   17534 |                   3 |                17533 |                       17534 |                                   3 |            4575           | True                        |                17533 |                       17534 |                                   3 |            4575           | True                        | True                                |                14 |               439 |                14 |               439 |
| zero_6     | zero_block        |    000000 |   6 |           0 |              4294 | 0..4293                |              4295 | 0..4294                |                1 |               -1 |                      -1 |                   0 |                   -1 |                          -1 |                                   0 |             nan           | False                       |                   -1 |                          -1 |                                   0 |             nan           | False                       | True                                |               nan |               nan |               nan |               nan |
| zero_7     | zero_block        |   0000000 |   7 |           0 |               429 | 0..428                 |               430 | 0..429                 |                1 |               -1 |                      -1 |                   0 |                   -1 |                          -1 |                                   0 |             nan           | False                       |                   -1 |                          -1 |                                   0 |             nan           | False                       | True                                |               nan |               nan |               nan |               nan |
| zero_8     | zero_block        |  00000000 |   8 |           0 |                42 | 0..41                  |                43 | 0..42                  |                1 |               -1 |                      -1 |                   0 |                   -1 |                          -1 |                                   0 |             nan           | False                       |                   -1 |                          -1 |                                   0 |             nan           | False                       | True                                |               nan |               nan |               nan |               nan |
| pat_1      | arbitrary_decimal |         1 |   1 |           1 |         429496729 | 429496730..858993458   |         429496731 | 429496729..858993459   |                2 |                0 |                       1 |               49984 |                    0 |                           1 |                               49980 |               6.08136e+08 | True                        |                    0 |                           1 |                               49980 |               6.08136e+08 | True                        | True                                |                 0 |                 0 |                 0 |                 0 |
| pat_14     | arbitrary_decimal |        14 |   2 |          14 |          42949672 | 601295422..644245093   |          42949674 | 601295421..644245094   |                2 |                0 |                       1 |                4963 |                    0 |                           1 |                                4962 |               6.08136e+08 | True                        |                    0 |                           1 |                                4962 |               6.08136e+08 | True                        | True                                |                 0 |                 0 |                 0 |                 0 |
| pat_141    | arbitrary_decimal |       141 |   3 |         141 |           4294967 | 605590389..609885355   |           4294969 | 605590388..609885356   |                2 |                0 |                       1 |                 493 |                    0 |                           1 |                                 492 |               6.08136e+08 | True                        |                    0 |                           1 |                                 492 |               6.08136e+08 | True                        | True                                |                 0 |                 0 |                 0 |                 0 |
| pat_314    | arbitrary_decimal |       314 |   3 |         314 |           4294967 | 1348619731..1352914697 |           4294969 | 1348619730..1352914698 |                2 |             2119 |                    2120 |                 497 |                 2119 |                        2120 |                                 497 |               1.3499e+09  | True                        |                 2119 |                        2120 |                                 497 |               1.3499e+09  | True                        | True                                |                 1 |               898 |                 1 |               898 |
| pat_159    | arbitrary_decimal |       159 |   3 |         159 |           4294966 | 682899801..687194766   |           4294968 | 682899800..687194767   |                2 |                2 |                       3 |                 510 |                    2 |                           3 |                                 510 |               6.8404e+08  | True                        |                    2 |                           3 |                                 510 |               6.8404e+08  | True                        | True                                |                 0 |                 2 |                 0 |                 2 |
| pat_2718   | arbitrary_decimal |      2718 |   4 |        2718 |            429495 | 1167372112..1167801606 |            429497 | 1167372111..1167801607 |                2 |            11705 |                   11706 |                  51 |                11705 |                       11706 |                                  51 |               1.16774e+09 | True                        |                11705 |                       11706 |                                  51 |               1.16774e+09 | True                        | True                                |                 9 |               716 |                 9 |               716 |
| pat_9999   | arbitrary_decimal |      9999 |   4 |        9999 |            429496 | 4294537800..4294967295 |            429497 | 4294537799..4294967295 |                1 |              761 |                     762 |                  58 |                  761 |                         762 |                                  58 |               4.29497e+09 | True                        |                  761 |                         762 |                                  58 |               4.29497e+09 | True                        | True                                |                 0 |               761 |                 0 |               761 |
| pat_12345  | arbitrary_decimal |     12345 |   5 |       12345 |             42949 | 530213713..530256661   |             42951 | 530213712..530256662   |                2 |            49701 |                   49702 |                   4 |                49701 |                       49702 |                                   4 |               5.30252e+08 | True                        |                49701 |                       49702 |                                   4 |               5.30252e+08 | True                        | True                                |                40 |               861 |                40 |               861 |
| pat_314159 | arbitrary_decimal |    314159 |   6 |      314159 |              4294 | 1349302631..1349306924 |              4296 | 1349302630..1349306925 |                2 |           176450 |                  176451 |                   1 |               176450 |                      176451 |                                   1 |               1.34931e+09 | True                        |               176450 |                      176451 |                                   1 |               1.34931e+09 | True                        | True                                |               144 |               626 |               144 |               626 |
| pat_000001 | arbitrary_decimal |    000001 |   6 |           1 |              4294 | 4295..8588             |              4296 | 4294..8589             |                2 |            17533 |                   17534 |                   1 |                17533 |                       17534 |                                   1 |            4575           | True                        |                17533 |                       17534 |                                   1 |            4575           | True                        | True                                |                14 |               439 |                14 |               439 |
| pat_987654 | arbitrary_decimal |    987654 |   6 |      987654 |              4294 | 4241941630..4241945923 |              4296 | 4241941629..4241945924 |                2 |               -1 |                      -1 |                   0 |                   -1 |                          -1 |                                   0 |             nan           | False                       |                   -1 |                          -1 |                                   0 |             nan           | False                       | True                                |               nan |               nan |               nan |               nan |

## Summary

```json
{
  "queries_total": 19,
  "direct_found": 15,
  "contained_returned": 15,
  "intersect_returned": 15,
  "contained_precision": 1.0,
  "intersect_precision": 1.0,
  "intersect_matches_direct_first_fraction": 1.0
}
```

## Interpretation

- The finite matrix-sector index works inside the scanned horizon.
- `intersect` lookup is the complete target range: it should recover the same first candidate as direct search when the pattern exists within the horizon.
- `contained` lookup is stricter: when it returns a hit, it is a cross-base certificate because the quaternary cell is fully inside the decimal target sector.
- Boundary/intersect cells can include candidates requiring direct interval or chord refinement.
- Each returned position is also annotated with the proven decimal resonance chart:

```text
M = 1221 q + r
```

so the locate result is already compatible with the resonance coordinate model.

## Important limitation

This is a finite-horizon locate engine. It does not predict the first occurrence beyond `H`.

What it proves:

```text
within H, target sector lookup and cross-base certification work.
```

What it does not prove:

```text
a closed-form first-index oracle for arbitrary strings in the infinite expansion of pi.
```

## Next implementation step

Turn this into code modules:

```text
pifs/sector.py
pifs/transform.py
pifs/finite_index.py
pifs/certificate.py
pifs/resonance.py
```

and add tests:

```text
contained_cells(10, 1000, 0, 4, 1661) == [0]
locate("0000") == direct_search("0000")
returned M satisfies M = 1221 q + r
```
