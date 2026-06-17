# pi-fs experiment 004: matrix target transform + resonance coordinates

## Goal

Test option C:

```text
target transform matrix + proven resonance chart + sector state vector + certificate
```

For a decimal zero block of length `D`, the decimal target sector is:

```text
[0, 10^-D)
```

We transform it into quaternary cells at depth:

```text
L4 = ceil(D log_4 10)
```

A contained quaternary cell gives a strict certificate:

```text
I_b^(4,L4) subset [0, 10^-D)
```

Then every position `M` is also mapped to resonance coordinates using the proven decimal resonance chart:

```text
K = 1221
N = 2456
M = q K + r
```

and, for comparison, the smaller chart:

```text
K = 87
N = 175
```

This experiment scans the first `200,000` decimal positions of pi.

Generated decimal digits with mpmath precision `200100` in `0.64` seconds.

## 1. Target transform: decimal zero sector -> quaternary certifying cells

|   D_decimal_zeros |   L4 |   intersect_cells |   contained_cells |   boundary_cells | intersect_range   | contained_range   |   boundary_cells_list | claim                                                 |
|------------------:|-----:|------------------:|------------------:|-----------------:|:------------------|:------------------|----------------------:|:------------------------------------------------------|
|                 1 |    2 |                 2 |                 1 |                1 | 0..1              | 0..0              |                     1 | base4 cells [0] at depth 2 certify 1 decimal zeros    |
|                 2 |    4 |                 3 |                 2 |                1 | 0..2              | 0..1              |                     2 | base4 cells [0, 1] at depth 4 certify 2 decimal zeros |
|                 3 |    5 |                 2 |                 1 |                1 | 0..1              | 0..0              |                     1 | base4 cells [0] at depth 5 certify 3 decimal zeros    |
|                 4 |    7 |                 2 |                 1 |                1 | 0..1              | 0..0              |                     1 | base4 cells [0] at depth 7 certify 4 decimal zeros    |
|                 5 |    9 |                 3 |                 2 |                1 | 0..2              | 0..1              |                     2 | base4 cells [0, 1] at depth 9 certify 5 decimal zeros |
|                 6 |   10 |                 2 |                 1 |                1 | 0..1              | 0..0              |                     1 | base4 cells [0] at depth 10 certify 6 decimal zeros   |

## 2. First direct zero hits with resonance coordinates

|   D_decimal_zeros |   first_M_zero_based |   first_position_after_decimal |   first_suffix_preview |   L4 |   base4_cell | matrix_class   |   K87_N175_q |   K87_N175_r |   K87_N175_M_reconstructed |   K1221_N2456_q |   K1221_N2456_r |   K1221_N2456_M_reconstructed |
|------------------:|---------------------:|-------------------------------:|-----------------------:|-----:|-------------:|:---------------|-------------:|-------------:|---------------------------:|----------------:|----------------:|------------------------------:|
|                 1 |                   31 |                             32 |   02884197169399375105 |    2 |            0 | contained      |            0 |           31 |                         31 |               0 |              31 |                            31 |
|                 2 |                  306 |                            307 |   00660631558817488152 |    4 |            1 | contained      |            3 |           45 |                        306 |               0 |             306 |                           306 |
|                 3 |                  600 |                            601 |   00056812714526356082 |    5 |            0 | contained      |            6 |           78 |                        600 |               0 |             600 |                           600 |
|                 4 |                13389 |                          13390 |   00009071510582362672 |    7 |            1 | boundary       |          153 |           78 |                      13389 |              10 |            1179 |                         13389 |
|                 5 |                17533 |                          17534 |   00000106526248547305 |    9 |            0 | contained      |          201 |           46 |                      17533 |              14 |             439 |                         17533 |

## 3. Scan summary

|   D_decimal_zeros |   H_decimal_positions_scanned |   direct_hits |   contained_cert_hits |   intersect_candidates |   boundary_candidates |   false_contained_hits |   false_boundary_candidates |   contained_recall_of_direct |   intersect_recall_of_direct |   contained_precision |   intersect_precision |   first_direct_M |   first_contained_M |   first_intersect_M |
|------------------:|------------------------------:|--------------:|----------------------:|-----------------------:|----------------------:|-----------------------:|----------------------------:|-----------------------------:|-----------------------------:|----------------------:|----------------------:|-----------------:|--------------------:|--------------------:|
|                 1 |                        200000 |         20104 |                 12564 |                  25209 |                 12645 |                      0 |                        5105 |                     0.62495  |                            1 |                     1 |              0.797493 |               31 |                  31 |                  31 |
|                 2 |                        200000 |          2040 |                  1595 |                   2402 |                   807 |                      0 |                         362 |                     0.781863 |                            1 |                     1 |              0.849292 |              306 |                 306 |                 306 |
|                 3 |                        200000 |           197 |                   192 |                    399 |                   207 |                      0 |                         202 |                     0.974619 |                            1 |                     1 |              0.493734 |              600 |                 600 |                 359 |
|                 4 |                        200000 |            18 |                     9 |                     23 |                    14 |                      0 |                           5 |                     0.5      |                            1 |                     1 |              0.782609 |            13389 |               17533 |               13389 |
|                 5 |                        200000 |             1 |                     1 |                      2 |                     1 |                      0 |                           1 |                     1        |                            1 |                     1 |              0.5      |            17533 |               17533 |               17533 |
|                 6 |                        200000 |             0 |                     0 |                      1 |                     1 |                      0 |                           1 |                   nan        |                          nan |                   nan |              0        |              nan |                 nan |               17533 |

Interpretation:

- `contained_cert_hits` are strict hits: every contained quaternary cell is fully inside the decimal zero sector.
- `intersect_candidates` include contained cells plus boundary cells.
- `intersect_recall_of_direct` should be 1.0: every direct decimal zero hit lies in an intersecting quaternary cell.
- `contained_precision` should be 1.0: every contained-cell hit is a guaranteed decimal zero hit.
- Boundary cells add recall but may introduce false positives that need interval/chord refinement.

## 4. Meaning for pi-fs

The experiment confirms the matrix-resonance pipeline on small zero blocks:

```text
decimal target -> quaternary certifying cells -> decimal phase state -> resonance coordinates (q,r)
```

For the 1000-zero target, the same matrix transform gives:

```text
D = 1000
L4 = 1661
contained cell: 0
boundary cell: 1
```

The corresponding sufficient certificate is:

```text
floor(4^1661 * {10^M pi}) = 0
    => {10^M pi} < 10^-1000
```

With the proven medium resonance chart:

```text
M = 1221 q + r
```

the sufficient certificate becomes:

```text
floor(4^1661 * {10^r pi^(2456 q + 1) rho^(-q)}) = 0
    => 1000 decimal zeros at position M + 1
```

where:

```text
rho = pi^2456 / 10^1221
```

This does not produce the first `q,r` automatically. It validates the target-transform and certification algebra that any future candidate generator must satisfy.
