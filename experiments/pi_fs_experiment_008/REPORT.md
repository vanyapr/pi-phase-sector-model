# pi-fs experiment 008: inverse tree and hidden branch variable n

## Goal

Clarify the obstruction:

```text
n = floor(10^M pi)
```

or, for the fractional orbit,

```text
n = floor(10^M frac(pi)).
```

This `n` is the branch of the inverse tree. It is essentially the first `M` decimal digits of pi's fractional part. The certificate formula is exact, but inverting it requires knowing or compressing this branch.

## 1. Exact inverse formula

For a D-zero block:

```text
{10^M pi} < 10^-D
```

Equivalently, for the fractional part alpha = frac(pi):

```text
10^M alpha in [n, n + 10^-D)
```

for some integer:

```text
n = floor(10^M alpha)
```

So:

```text
alpha in [n / 10^M, (n + 10^-D) / 10^M)
```

The full inverse image is:

```text
f^(-M)([0,10^-D)) =
union over n=0..10^M-1 of [n/10^M, n/10^M + 10^-(D+M))
```

This is a comb: `10^M` tiny intervals.

## 2. Inverse preimage growth and quaternary grid counts

|   D |   M_preimage_depth |   Q |   L_grid |   grid_cells |   explicit_intervals |   interval_width_log10 |   total_measure |   intersect_cell_runs |   intersect_cells |   contained_cell_runs |   contained_cells |   boundary_cells | symbolic_pattern   |   symbolic_length_unrolled |
|----:|-------------------:|----:|---------:|-------------:|---------------------:|-----------------------:|----------------:|----------------------:|------------------:|----------------------:|------------------:|-----------------:|:-------------------|---------------------------:|
|   1 |                  0 |   4 |        2 |           16 |                    1 |                     -1 |           0.1   |                     1 |                 2 |                     1 |                 1 |                1 | 0                  |                          1 |
|   1 |                  0 |   4 |        3 |           64 |                    1 |                     -1 |           0.1   |                     1 |                 7 |                     1 |                 6 |                1 | 0                  |                          1 |
|   1 |                  0 |   4 |        4 |          256 |                    1 |                     -1 |           0.1   |                     1 |                26 |                     1 |                25 |                1 | 0                  |                          1 |
|   1 |                  1 |   4 |        4 |          256 |                   10 |                     -2 |           0.1   |                    10 |                34 |                    10 |                16 |               18 | *0                 |                          2 |
|   1 |                  1 |   4 |        5 |         1024 |                   10 |                     -2 |           0.1   |                    10 |               112 |                    10 |                94 |               18 | *0                 |                          2 |
|   1 |                  1 |   4 |        6 |         4096 |                   10 |                     -2 |           0.1   |                    10 |               418 |                    10 |               400 |               18 | *0                 |                          2 |
|   1 |                  2 |   4 |        5 |         1024 |                  100 |                     -3 |           0.1   |                   100 |               200 |                     4 |                 4 |              196 | **0                |                          3 |
|   1 |                  2 |   4 |        6 |         4096 |                  100 |                     -3 |           0.1   |                   100 |               508 |                   100 |               312 |              196 | **0                |                          3 |
|   1 |                  2 |   4 |        7 |        16384 |                  100 |                     -3 |           0.1   |                   100 |              1736 |                   100 |              1540 |              196 | **0                |                          3 |
|   1 |                  3 |   4 |        7 |        16384 |                 1000 |                     -4 |           0.1   |                  1000 |              2632 |                   640 |               640 |             1992 | ***0               |                          4 |
|   1 |                  3 |   4 |        8 |        65536 |                 1000 |                     -4 |           0.1   |                  1000 |              7552 |                  1000 |              5560 |             1992 | ***0               |                          4 |
|   1 |                  3 |   4 |        9 |       262144 |                 1000 |                     -4 |           0.1   |                  1000 |             27208 |                  1000 |             25216 |             1992 | ***0               |                          4 |
|   1 |                  4 |   4 |        9 |       262144 |                10000 |                     -5 |           0.1   |                 10000 |             36208 |                 10000 |             16224 |            19984 | ****0              |                          5 |
|   1 |                  4 |   4 |       10 |      1048576 |                10000 |                     -5 |           0.1   |                 10000 |            114848 |                 10000 |             94864 |            19984 | ****0              |                          5 |
|   1 |                  4 |   4 |       11 |      4194304 |                10000 |                     -5 |           0.1   |                 10000 |            429424 |                 10000 |            409440 |            19984 | ****0              |                          5 |
|   1 |                  5 |   4 |       10 |      1048576 |               100000 |                     -6 |           0.1   |                100000 |            204832 |                  4864 |              4864 |           199968 | *****0             |                          6 |
|   1 |                  5 |   4 |       11 |      4194304 |               100000 |                     -6 |           0.1   |                100000 |            519424 |                100000 |            319456 |           199968 | *****0             |                          6 |
|   1 |                  5 |   4 |       12 |     16777216 |               100000 |                     -6 |           0.1   |                100000 |           1777696 |                100000 |           1577728 |           199968 | *****0             |                          6 |
|   2 |                  0 |   4 |        4 |          256 |                    1 |                     -2 |           0.01  |                     1 |                 3 |                     1 |                 2 |                1 | 00                 |                          2 |
|   2 |                  0 |   4 |        5 |         1024 |                    1 |                     -2 |           0.01  |                     1 |                11 |                     1 |                10 |                1 | 00                 |                          2 |
|   2 |                  0 |   4 |        6 |         4096 |                    1 |                     -2 |           0.01  |                     1 |                41 |                     1 |                40 |                1 | 00                 |                          2 |
|   2 |                  1 |   4 |        5 |         1024 |                   10 |                     -3 |           0.01  |                    10 |                20 |                     2 |                 2 |               18 | *00                |                          3 |
|   2 |                  1 |   4 |        6 |         4096 |                   10 |                     -3 |           0.01  |                    10 |                50 |                    10 |                32 |               18 | *00                |                          3 |
|   2 |                  1 |   4 |        7 |        16384 |                   10 |                     -3 |           0.01  |                    10 |               172 |                    10 |               154 |               18 | *00                |                          3 |
|   2 |                  2 |   4 |        7 |        16384 |                  100 |                     -4 |           0.01  |                   100 |               260 |                    64 |                64 |              196 | **00               |                          4 |
|   2 |                  2 |   4 |        8 |        65536 |                  100 |                     -4 |           0.01  |                   100 |               752 |                   100 |               556 |              196 | **00               |                          4 |
|   2 |                  2 |   4 |        9 |       262144 |                  100 |                     -4 |           0.01  |                   100 |              2720 |                   100 |              2524 |              196 | **00               |                          4 |
|   2 |                  3 |   4 |        9 |       262144 |                 1000 |                     -5 |           0.01  |                  1000 |              3616 |                  1000 |              1624 |             1992 | ***00              |                          5 |
|   2 |                  3 |   4 |       10 |      1048576 |                 1000 |                     -5 |           0.01  |                  1000 |             11480 |                  1000 |              9488 |             1992 | ***00              |                          5 |
|   2 |                  3 |   4 |       11 |      4194304 |                 1000 |                     -5 |           0.01  |                  1000 |             42936 |                  1000 |             40944 |             1992 | ***00              |                          5 |
|   2 |                  4 |   4 |       10 |      1048576 |                10000 |                     -6 |           0.01  |                 10000 |             20480 |                   496 |               496 |            19984 | ****00             |                          6 |
|   2 |                  4 |   4 |       11 |      4194304 |                10000 |                     -6 |           0.01  |                 10000 |             51936 |                 10000 |             31952 |            19984 | ****00             |                          6 |
|   2 |                  4 |   4 |       12 |     16777216 |                10000 |                     -6 |           0.01  |                 10000 |            177760 |                 10000 |            157776 |            19984 | ****00             |                          6 |
|   2 |                  5 |   4 |       12 |     16777216 |               100000 |                     -7 |           0.01  |                100000 |            267744 |                 67776 |             67776 |           199968 | *****00            |                          7 |
|   2 |                  5 |   4 |       13 |     67108864 |               100000 |                     -7 |           0.01  |                100000 |            771072 |                100000 |            571104 |           199968 | *****00            |                          7 |
|   2 |                  5 |   4 |       14 |    268435456 |               100000 |                     -7 |           0.01  |                100000 |           2784352 |                100000 |           2584384 |           199968 | *****00            |                          7 |
|   3 |                  0 |   4 |        5 |         1024 |                    1 |                     -3 |           0.001 |                     1 |                 2 |                     1 |                 1 |                1 | 000                |                          3 |
|   3 |                  0 |   4 |        6 |         4096 |                    1 |                     -3 |           0.001 |                     1 |                 5 |                     1 |                 4 |                1 | 000                |                          3 |
|   3 |                  0 |   4 |        7 |        16384 |                    1 |                     -3 |           0.001 |                     1 |                17 |                     1 |                16 |                1 | 000                |                          3 |
|   3 |                  1 |   4 |        7 |        16384 |                   10 |                     -4 |           0.001 |                    10 |                26 |                     8 |                 8 |               18 | *000               |                          4 |
|   3 |                  1 |   4 |        8 |        65536 |                   10 |                     -4 |           0.001 |                    10 |                74 |                    10 |                56 |               18 | *000               |                          4 |
|   3 |                  1 |   4 |        9 |       262144 |                   10 |                     -4 |           0.001 |                    10 |               272 |                    10 |               254 |               18 | *000               |                          4 |
|   3 |                  2 |   4 |        9 |       262144 |                  100 |                     -5 |           0.001 |                   100 |               360 |                   100 |               164 |              196 | **000              |                          5 |
|   3 |                  2 |   4 |       10 |      1048576 |                  100 |                     -5 |           0.001 |                   100 |              1148 |                   100 |               952 |              196 | **000              |                          5 |
|   3 |                  2 |   4 |       11 |      4194304 |                  100 |                     -5 |           0.001 |                   100 |              4292 |                   100 |              4096 |              196 | **000              |                          5 |
|   3 |                  3 |   4 |       10 |      1048576 |                 1000 |                     -6 |           0.001 |                  1000 |              2048 |                    56 |                56 |             1992 | ***000             |                          6 |
|   3 |                  3 |   4 |       11 |      4194304 |                 1000 |                     -6 |           0.001 |                  1000 |              5192 |                  1000 |              3200 |             1992 | ***000             |                          6 |
|   3 |                  3 |   4 |       12 |     16777216 |                 1000 |                     -6 |           0.001 |                  1000 |             17776 |                  1000 |             15784 |             1992 | ***000             |                          6 |
|   3 |                  4 |   4 |       12 |     16777216 |                10000 |                     -7 |           0.001 |                 10000 |             26768 |                  6784 |              6784 |            19984 | ****000            |                          7 |
|   3 |                  4 |   4 |       13 |     67108864 |                10000 |                     -7 |           0.001 |                 10000 |             77104 |                 10000 |             57120 |            19984 | ****000            |                          7 |
|   3 |                  4 |   4 |       14 |    268435456 |                10000 |                     -7 |           0.001 |                 10000 |            278432 |                 10000 |            258448 |            19984 | ****000            |                          7 |
|   3 |                  5 |   4 |       14 |    268435456 |               100000 |                     -8 |           0.001 |                100000 |            368416 |                100000 |            168448 |           199968 | *****000           |                          8 |
|   3 |                  5 |   4 |       15 |   1073741824 |               100000 |                     -8 |           0.001 |                100000 |           1173728 |                100000 |            973760 |           199968 | *****000           |                          8 |
|   3 |                  5 |   4 |       16 |   4294967296 |               100000 |                     -8 |           0.001 |                100000 |           4394944 |                100000 |           4194976 |           199968 | *****000           |                          8 |

## 3. Hidden branch examples from actual pi

|   D_zero_block |   first_M_zero_based |   first_position_after_decimal |     suffix_at_hit |   hidden_branch_n_fraction_digits_prefix_len | hidden_branch_n_prefix_preview         | branch_formula                                       |   L4_cert_depth |   cell_at_hit_depth_L4 |
|---------------:|---------------------:|-------------------------------:|------------------:|---------------------------------------------:|:---------------------------------------|:-----------------------------------------------------|----------------:|-----------------------:|
|              1 |                   31 |                             32 |     0288419716939 |                                           31 | 1415926535897932384626433832795        | frac(pi) in [(n + 0)/10^31, (n + 10^-1)/10^31)       |               2 |                      0 |
|              2 |                  306 |                            307 |    00660631558817 |                                          306 | 1415926535897932384626433...1273724587 | frac(pi) in [(n + 0)/10^306, (n + 10^-2)/10^306)     |               4 |                      1 |
|              3 |                  600 |                            601 |   000568127145263 |                                          600 | 1415926535897932384626433...7669405132 | frac(pi) in [(n + 0)/10^600, (n + 10^-3)/10^600)     |               5 |                      0 |
|              4 |                13389 |                          13390 |  0000907151058236 |                                        13389 | 1415926535897932384626433...4585293095 | frac(pi) in [(n + 0)/10^13389, (n + 10^-4)/10^13389) |               7 |                      1 |
|              5 |                17533 |                          17534 | 00000106526248547 |                                        17533 | 1415926535897932384626433...9485366768 | frac(pi) in [(n + 0)/10^17533, (n + 10^-5)/10^17533) |               9 |                      0 |

The column `hidden_branch_n_prefix_preview` is exactly the hidden branch prefix. For large M, this is why the inverse formula does not directly reveal M: the branch is as hard as knowing the earlier digits.

## 4. Symbolic compression vs explicit intervals

|   D |    M | explicit_interval_count   | total_measure   | interval_width   | wildcard_description                         |   unrolled_pattern_length |   hidden_branch_digits_needed | conclusion                                                      |
|----:|-----:|:--------------------------|:----------------|:-----------------|:---------------------------------------------|--------------------------:|------------------------------:|:----------------------------------------------------------------|
|   1 |    0 | 1                         | 10^-1           | 10^-1            | any 0 decimal digits followed by 1 zeros     |                         1 |                             0 | compact as symbolic set; not predictive for pi without branch n |
|   1 |    1 | 10                        | 10^-1           | 10^-2            | any 1 decimal digits followed by 1 zeros     |                         2 |                             1 | compact as symbolic set; not predictive for pi without branch n |
|   1 |    2 | 100                       | 10^-1           | 10^-3            | any 2 decimal digits followed by 1 zeros     |                         3 |                             2 | compact as symbolic set; not predictive for pi without branch n |
|   1 |    3 | 1000                      | 10^-1           | 10^-4            | any 3 decimal digits followed by 1 zeros     |                         4 |                             3 | compact as symbolic set; not predictive for pi without branch n |
|   1 |    6 | 1000000                   | 10^-1           | 10^-7            | any 6 decimal digits followed by 1 zeros     |                         7 |                             6 | compact as symbolic set; not predictive for pi without branch n |
|   1 |   10 | 10^10                     | 10^-1           | 10^-11           | any 10 decimal digits followed by 1 zeros    |                        11 |                            10 | compact as symbolic set; not predictive for pi without branch n |
|   1 |   50 | 10^50                     | 10^-1           | 10^-51           | any 50 decimal digits followed by 1 zeros    |                        51 |                            50 | compact as symbolic set; not predictive for pi without branch n |
|   1 | 1000 | 10^1000                   | 10^-1           | 10^-1001         | any 1000 decimal digits followed by 1 zeros  |                      1001 |                          1000 | compact as symbolic set; not predictive for pi without branch n |
|   2 |    0 | 1                         | 10^-2           | 10^-2            | any 0 decimal digits followed by 2 zeros     |                         2 |                             0 | compact as symbolic set; not predictive for pi without branch n |
|   2 |    1 | 10                        | 10^-2           | 10^-3            | any 1 decimal digits followed by 2 zeros     |                         3 |                             1 | compact as symbolic set; not predictive for pi without branch n |
|   2 |    2 | 100                       | 10^-2           | 10^-4            | any 2 decimal digits followed by 2 zeros     |                         4 |                             2 | compact as symbolic set; not predictive for pi without branch n |
|   2 |    3 | 1000                      | 10^-2           | 10^-5            | any 3 decimal digits followed by 2 zeros     |                         5 |                             3 | compact as symbolic set; not predictive for pi without branch n |
|   2 |    6 | 1000000                   | 10^-2           | 10^-8            | any 6 decimal digits followed by 2 zeros     |                         8 |                             6 | compact as symbolic set; not predictive for pi without branch n |
|   2 |   10 | 10^10                     | 10^-2           | 10^-12           | any 10 decimal digits followed by 2 zeros    |                        12 |                            10 | compact as symbolic set; not predictive for pi without branch n |
|   2 |   50 | 10^50                     | 10^-2           | 10^-52           | any 50 decimal digits followed by 2 zeros    |                        52 |                            50 | compact as symbolic set; not predictive for pi without branch n |
|   2 | 1000 | 10^1000                   | 10^-2           | 10^-1002         | any 1000 decimal digits followed by 2 zeros  |                      1002 |                          1000 | compact as symbolic set; not predictive for pi without branch n |
|   3 |    0 | 1                         | 10^-3           | 10^-3            | any 0 decimal digits followed by 3 zeros     |                         3 |                             0 | compact as symbolic set; not predictive for pi without branch n |
|   3 |    1 | 10                        | 10^-3           | 10^-4            | any 1 decimal digits followed by 3 zeros     |                         4 |                             1 | compact as symbolic set; not predictive for pi without branch n |
|   3 |    2 | 100                       | 10^-3           | 10^-5            | any 2 decimal digits followed by 3 zeros     |                         5 |                             2 | compact as symbolic set; not predictive for pi without branch n |
|   3 |    3 | 1000                      | 10^-3           | 10^-6            | any 3 decimal digits followed by 3 zeros     |                         6 |                             3 | compact as symbolic set; not predictive for pi without branch n |
|   3 |    6 | 1000000                   | 10^-3           | 10^-9            | any 6 decimal digits followed by 3 zeros     |                         9 |                             6 | compact as symbolic set; not predictive for pi without branch n |
|   3 |   10 | 10^10                     | 10^-3           | 10^-13           | any 10 decimal digits followed by 3 zeros    |                        13 |                            10 | compact as symbolic set; not predictive for pi without branch n |
|   3 |   50 | 10^50                     | 10^-3           | 10^-53           | any 50 decimal digits followed by 3 zeros    |                        53 |                            50 | compact as symbolic set; not predictive for pi without branch n |
|   3 | 1000 | 10^1000                   | 10^-3           | 10^-1003         | any 1000 decimal digits followed by 3 zeros  |                      1003 |                          1000 | compact as symbolic set; not predictive for pi without branch n |
|   6 |    0 | 1                         | 10^-6           | 10^-6            | any 0 decimal digits followed by 6 zeros     |                         6 |                             0 | compact as symbolic set; not predictive for pi without branch n |
|   6 |    1 | 10                        | 10^-6           | 10^-7            | any 1 decimal digits followed by 6 zeros     |                         7 |                             1 | compact as symbolic set; not predictive for pi without branch n |
|   6 |    2 | 100                       | 10^-6           | 10^-8            | any 2 decimal digits followed by 6 zeros     |                         8 |                             2 | compact as symbolic set; not predictive for pi without branch n |
|   6 |    3 | 1000                      | 10^-6           | 10^-9            | any 3 decimal digits followed by 6 zeros     |                         9 |                             3 | compact as symbolic set; not predictive for pi without branch n |
|   6 |    6 | 1000000                   | 10^-6           | 10^-12           | any 6 decimal digits followed by 6 zeros     |                        12 |                             6 | compact as symbolic set; not predictive for pi without branch n |
|   6 |   10 | 10^10                     | 10^-6           | 10^-16           | any 10 decimal digits followed by 6 zeros    |                        16 |                            10 | compact as symbolic set; not predictive for pi without branch n |
|   6 |   50 | 10^50                     | 10^-6           | 10^-56           | any 50 decimal digits followed by 6 zeros    |                        56 |                            50 | compact as symbolic set; not predictive for pi without branch n |
|   6 | 1000 | 10^1000                   | 10^-6           | 10^-1006         | any 1000 decimal digits followed by 6 zeros  |                      1006 |                          1000 | compact as symbolic set; not predictive for pi without branch n |
|  50 |    0 | 1                         | 10^-50          | 10^-50           | any 0 decimal digits followed by 50 zeros    |                        50 |                             0 | compact as symbolic set; not predictive for pi without branch n |
|  50 |    1 | 10                        | 10^-50          | 10^-51           | any 1 decimal digits followed by 50 zeros    |                        51 |                             1 | compact as symbolic set; not predictive for pi without branch n |
|  50 |    2 | 100                       | 10^-50          | 10^-52           | any 2 decimal digits followed by 50 zeros    |                        52 |                             2 | compact as symbolic set; not predictive for pi without branch n |
|  50 |    3 | 1000                      | 10^-50          | 10^-53           | any 3 decimal digits followed by 50 zeros    |                        53 |                             3 | compact as symbolic set; not predictive for pi without branch n |
|  50 |    6 | 1000000                   | 10^-50          | 10^-56           | any 6 decimal digits followed by 50 zeros    |                        56 |                             6 | compact as symbolic set; not predictive for pi without branch n |
|  50 |   10 | 10^10                     | 10^-50          | 10^-60           | any 10 decimal digits followed by 50 zeros   |                        60 |                            10 | compact as symbolic set; not predictive for pi without branch n |
|  50 |   50 | 10^50                     | 10^-50          | 10^-100          | any 50 decimal digits followed by 50 zeros   |                       100 |                            50 | compact as symbolic set; not predictive for pi without branch n |
|  50 | 1000 | 10^1000                   | 10^-50          | 10^-1050         | any 1000 decimal digits followed by 50 zeros |                      1050 |                          1000 | compact as symbolic set; not predictive for pi without branch n |

There is a compact symbolic description:

```text
any M digits, followed by D zeros
```

But this does not identify whether pi follows one of those branches without knowing its first M digits.

## 5. Interpretation

This experiment shows three things:

1. The certificate formula is exact.
2. Its inverse is exact too.
3. But the inverse tree has `10^M` branches, and the branch variable `n` is the already-known prefix of pi.

So the statement

```text
we have a certificate formula
```

does not imply

```text
we can solve for the first index M in closed form
```

unless we find a way to compress or predict the branch `n`.

## 6. Why this does not prove absence of 1000 zeros

The fact that the inverse formula contains a hidden branch does not mean the 1000-zero block does not exist.

It means:

```text
existence is equivalent to pi's fractional part landing in one interval of an exponentially branching inverse comb.
```

To disprove 1000 zeros, one would need to prove that pi's orbit never enters `[0,10^-1000)`. This experiment does not do that.

## 7. Next mathematical target

The correct next problem is:

```text
Can the inverse comb f^(-M)(I) be compressed in a way that is useful for the specific point alpha = frac(pi)?
```

Not machine learning. Not residue guessing.

The exact target is:

```text
certificate -> inverse tree -> branch compression
```
