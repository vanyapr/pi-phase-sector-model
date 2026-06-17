# pi-fs experiment 003: sector transform matrices

## Goal

Test the next proposed layer: matrices between sector partitions.

The object is not a symbolic conversion of digits. It is a geometric conversion of target sectors on the same unit circle.

For a system `(Q,L)`:

```text
I_a^(Q,L) = [a / Q^L, (a + 1) / Q^L)
```

A transform between `(Q,L)` and `(Q',L')` is represented by overlap and containment of these intervals.

## A. Binary <-> quaternary exact mapping

For `(4,L)` and `(2,2L)`, the partitions are identical. The transform is a permutation/identity after grouping two bits per base-4 digit.

|   Q_from |   L_from |   Q_to |   L_to |   source_sectors_total |   source_sectors_sampled |   target_cells_total |   mean_intersect |   min_intersect |   max_intersect |   mean_contained |   min_contained |   max_contained |   mean_boundary |   min_boundary |   max_boundary |   fraction_with_any_contained |   fraction_exact_one_to_one |
|---------:|---------:|-------:|-------:|-----------------------:|-------------------------:|---------------------:|-----------------:|----------------:|----------------:|-----------------:|----------------:|----------------:|----------------:|---------------:|---------------:|------------------------------:|----------------------------:|
|        4 |        1 |      2 |      2 |            4           |              4           |          4           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        2 |      2 |      4 |           16           |             16           |         16           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        3 |      2 |      6 |           64           |             64           |         64           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        4 |      2 |      8 |          256           |            256           |        256           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        5 |      2 |     10 |         1024           |           1024           |       1024           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        6 |      2 |     12 |         4096           |           4096           |       4096           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        7 |      2 |     14 |        16384           |          16384           |      16384           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        8 |      2 |     16 |        65536           |          65536           |      65536           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |        9 |      2 |     18 |       262144           |         262144           |     262144           |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |       10 |      2 |     20 |            1.04858e+06 |              1.04858e+06 |          1.04858e+06 |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |       11 |      2 |     22 |            4.1943e+06  |              4.1943e+06  |          4.1943e+06  |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |
|        4 |       12 |      2 |     24 |            1.67772e+07 |              1.67772e+07 |          1.67772e+07 |                1 |               1 |               1 |                1 |               1 |               1 |               0 |              0 |              0 |                             1 |                           1 |

Result: exact one-to-one mapping is confirmed.

## B. Decimal -> quaternary overlap/containment

For decimal sectors of depth `D`, we map them into quaternary cells of depth:

```text
L4 = ceil(D log_4 10) + offset
```

Summary:

|   Q_from |   L_from |   Q_to |   L_to |   source_sectors_total |   source_sectors_sampled |   target_cells_total |   mean_intersect |   min_intersect |   max_intersect |   mean_contained |   min_contained |   max_contained |   mean_boundary |   min_boundary |   max_boundary |   fraction_with_any_contained |   fraction_exact_one_to_one |   offset_from_ceil |   ceil_D_log4_10 |
|---------:|---------:|-------:|-------:|-----------------------:|-------------------------:|---------------------:|-----------------:|----------------:|----------------:|-----------------:|----------------:|----------------:|----------------:|---------------:|---------------:|------------------------------:|----------------------------:|-------------------:|-----------------:|
|       10 |        1 |      4 |      2 |                 10     |                       10 |         16           |           2.4    |               2 |               3 |           0.8    |               0 |               1 |          1.6    |              1 |              2 |                        0.8    |                           0 |                  0 |                2 |
|       10 |        1 |      4 |      3 |                 10     |                       10 |         64           |           7.2    |               7 |               8 |           5.6    |               5 |               6 |          1.6    |              1 |              2 |                        1      |                           0 |                  1 |                2 |
|       10 |        1 |      4 |      4 |                 10     |                       10 |        256           |          26.4    |              26 |              27 |          24.8    |              24 |              25 |          1.6    |              1 |              2 |                        1      |                           0 |                  2 |                2 |
|       10 |        1 |      4 |      5 |                 10     |                       10 |       1024           |         103.2    |             103 |             104 |         101.6    |             101 |             102 |          1.6    |              1 |              2 |                        1      |                           0 |                  3 |                2 |
|       10 |        1 |      4 |      6 |                 10     |                       10 |       4096           |         410.4    |             410 |             411 |         408.8    |             408 |             409 |          1.6    |              1 |              2 |                        1      |                           0 |                  4 |                2 |
|       10 |        2 |      4 |      4 |                100     |                      100 |        256           |           3.52   |               3 |               4 |           1.6    |               1 |               2 |          1.92   |              1 |              2 |                        1      |                           0 |                  0 |                4 |
|       10 |        2 |      4 |      5 |                100     |                      100 |       1024           |          11.2    |              11 |              12 |           9.28   |               9 |              10 |          1.92   |              1 |              2 |                        1      |                           0 |                  1 |                4 |
|       10 |        2 |      4 |      6 |                100     |                      100 |       4096           |          41.92   |              41 |              42 |          40      |              40 |              40 |          1.92   |              1 |              2 |                        1      |                           0 |                  2 |                4 |
|       10 |        2 |      4 |      7 |                100     |                      100 |      16384           |         164.8    |             164 |             165 |         162.88   |             162 |             163 |          1.92   |              1 |              2 |                        1      |                           0 |                  3 |                4 |
|       10 |        2 |      4 |      8 |                100     |                      100 |      65536           |         656.32   |             656 |             657 |         654.4    |             654 |             655 |          1.92   |              1 |              2 |                        1      |                           0 |                  4 |                4 |
|       10 |        3 |      4 |      5 |               1000     |                     1000 |       1024           |           2.016  |               2 |               3 |           0.032  |               0 |               1 |          1.984  |              1 |              2 |                        0.032  |                           0 |                  0 |                5 |
|       10 |        3 |      4 |      6 |               1000     |                     1000 |       4096           |           5.088  |               5 |               6 |           3.104  |               3 |               4 |          1.984  |              1 |              2 |                        1      |                           0 |                  1 |                5 |
|       10 |        3 |      4 |      7 |               1000     |                     1000 |      16384           |          17.376  |              17 |              18 |          15.392  |              15 |              16 |          1.984  |              1 |              2 |                        1      |                           0 |                  2 |                5 |
|       10 |        3 |      4 |      8 |               1000     |                     1000 |      65536           |          66.528  |              66 |              67 |          64.544  |              64 |              65 |          1.984  |              1 |              2 |                        1      |                           0 |                  3 |                5 |
|       10 |        3 |      4 |      9 |               1000     |                     1000 |     262144           |         263.136  |             263 |             264 |         261.152  |             261 |             262 |          1.984  |              1 |              2 |                        1      |                           0 |                  4 |                5 |
|       10 |        4 |      4 |      7 |              10000     |                    10000 |      16384           |           2.6368 |               2 |               3 |           0.64   |               0 |               1 |          1.9968 |              1 |              2 |                        0.64   |                           0 |                  0 |                7 |
|       10 |        4 |      4 |      8 |              10000     |                    10000 |      65536           |           7.552  |               7 |               8 |           5.5552 |               5 |               6 |          1.9968 |              1 |              2 |                        1      |                           0 |                  1 |                7 |
|       10 |        4 |      4 |      9 |              10000     |                    10000 |     262144           |          27.2128 |              27 |              28 |          25.216  |              25 |              26 |          1.9968 |              1 |              2 |                        1      |                           0 |                  2 |                7 |
|       10 |        4 |      4 |     10 |              10000     |                    10000 |          1.04858e+06 |         105.856  |             105 |             106 |         103.859  |             103 |             104 |          1.9968 |              1 |              2 |                        1      |                           0 |                  3 |                7 |
|       10 |        4 |      4 |     11 |              10000     |                    10000 |          4.1943e+06  |         420.429  |             420 |             421 |         418.432  |             418 |             419 |          1.9968 |              1 |              2 |                        1      |                           0 |                  4 |                7 |
|       10 |        5 |      4 |      9 |             100000     |                    10000 |     262144           |           3.632  |               3 |               4 |           1.6328 |               1 |               2 |          1.9992 |              1 |              2 |                        1      |                           0 |                  0 |                9 |
|       10 |        5 |      4 |     10 |             100000     |                    10000 |          1.04858e+06 |          11.4792 |              11 |              12 |           9.48   |               9 |              10 |          1.9992 |              1 |              2 |                        1      |                           0 |                  1 |                9 |
|       10 |        5 |      4 |     11 |             100000     |                    10000 |          4.1943e+06  |          42.9401 |              42 |              43 |          40.9407 |              40 |              41 |          1.9994 |              1 |              2 |                        1      |                           0 |                  2 |                9 |
|       10 |        5 |      4 |     12 |             100000     |                    10000 |          1.67772e+07 |         168.768  |             168 |             169 |         166.768  |             166 |             167 |          1.9993 |              1 |              2 |                        1      |                           0 |                  3 |                9 |
|       10 |        5 |      4 |     13 |             100000     |                    10000 |          6.71089e+07 |         672.088  |             672 |             673 |         670.089  |             670 |             671 |          1.9995 |              1 |              2 |                        1      |                           0 |                  4 |                9 |
|       10 |        6 |      4 |     10 |                  1e+06 |                    10000 |          1.04858e+06 |           2.0488 |               2 |               3 |           0.0489 |               0 |               1 |          1.9999 |              1 |              2 |                        0.0489 |                           0 |                  0 |               10 |
|       10 |        6 |      4 |     11 |                  1e+06 |                    10000 |          4.1943e+06  |           5.1982 |               5 |               6 |           3.1983 |               3 |               4 |          1.9999 |              1 |              2 |                        1      |                           0 |                  1 |               10 |
|       10 |        6 |      4 |     12 |                  1e+06 |                    10000 |          1.67772e+07 |          17.7816 |              17 |              18 |          15.7818 |              15 |              16 |          1.9998 |              1 |              2 |                        1      |                           0 |                  2 |               10 |
|       10 |        6 |      4 |     13 |                  1e+06 |                    10000 |          6.71089e+07 |          68.11   |              68 |              69 |          66.1102 |              66 |              67 |          1.9998 |              1 |              2 |                        1      |                           0 |                  3 |               10 |
|       10 |        6 |      4 |     14 |                  1e+06 |                    10000 |          2.68435e+08 |         269.426  |             269 |             270 |         267.427  |             267 |             268 |          1.9999 |              1 |              2 |                        1      |                           0 |                  4 |               10 |

Interpretation:

- At the minimal depth `ceil(D log_4 10)`, each decimal sector intersects only a small number of quaternary cells.
- Boundary ambiguity is small and controlled.
- Increasing `L4` gives more contained cells and separates guaranteed interior cells from boundary cells.

## C. Decimal zero block extrapolation

For a decimal zero block `[0,10^-D)`, the quaternary depth needed is:

```text
L4 >= ceil(D log_4 10)
```

For `D=1000`, this gives `L4=1661`.

|   decimal_zero_length_D |   L4 |   offset_from_ceil |   intersect_count |   contained_count |   boundary_count |   intersect_min |   intersect_max |   contained_min |   contained_max |   ratio_4L_over_10D_log10 | guarantee                                 |
|------------------------:|-----:|-------------------:|------------------:|------------------:|-----------------:|----------------:|----------------:|----------------:|----------------:|--------------------------:|:------------------------------------------|
|                       1 |    2 |                  0 |                 2 |                 1 |                1 |               0 |               1 |               0 |               0 |                 0.20412   | contained cells imply decimal zero-sector |
|                       1 |    3 |                  1 |                 7 |                 6 |                1 |               0 |               6 |               0 |               5 |                 0.80618   | contained cells imply decimal zero-sector |
|                       1 |    4 |                  2 |                26 |                25 |                1 |               0 |              25 |               0 |              24 |                 1.40824   | contained cells imply decimal zero-sector |
|                       1 |    5 |                  3 |               103 |               102 |                1 |               0 |             102 |               0 |             101 |                 2.0103    | contained cells imply decimal zero-sector |
|                       1 |    6 |                  4 |               410 |               409 |                1 |               0 |             409 |               0 |             408 |                 2.61236   | contained cells imply decimal zero-sector |
|                       1 |    7 |                  5 |              1639 |              1638 |                1 |               0 |            1638 |               0 |            1637 |                 3.21442   | contained cells imply decimal zero-sector |
|                       1 |    8 |                  6 |              6554 |              6553 |                1 |               0 |            6553 |               0 |            6552 |                 3.81648   | contained cells imply decimal zero-sector |
|                       2 |    4 |                  0 |                 3 |                 2 |                1 |               0 |               2 |               0 |               1 |                 0.40824   | contained cells imply decimal zero-sector |
|                       2 |    5 |                  1 |                11 |                10 |                1 |               0 |              10 |               0 |               9 |                 1.0103    | contained cells imply decimal zero-sector |
|                       2 |    6 |                  2 |                41 |                40 |                1 |               0 |              40 |               0 |              39 |                 1.61236   | contained cells imply decimal zero-sector |
|                       2 |    7 |                  3 |               164 |               163 |                1 |               0 |             163 |               0 |             162 |                 2.21442   | contained cells imply decimal zero-sector |
|                       2 |    8 |                  4 |               656 |               655 |                1 |               0 |             655 |               0 |             654 |                 2.81648   | contained cells imply decimal zero-sector |
|                       2 |    9 |                  5 |              2622 |              2621 |                1 |               0 |            2621 |               0 |            2620 |                 3.41854   | contained cells imply decimal zero-sector |
|                       2 |   10 |                  6 |             10486 |             10485 |                1 |               0 |           10485 |               0 |           10484 |                 4.0206    | contained cells imply decimal zero-sector |
|                       3 |    5 |                  0 |                 2 |                 1 |                1 |               0 |               1 |               0 |               0 |                 0.0103    | contained cells imply decimal zero-sector |
|                       3 |    6 |                  1 |                 5 |                 4 |                1 |               0 |               4 |               0 |               3 |                 0.61236   | contained cells imply decimal zero-sector |
|                       3 |    7 |                  2 |                17 |                16 |                1 |               0 |              16 |               0 |              15 |                 1.21442   | contained cells imply decimal zero-sector |
|                       3 |    8 |                  3 |                66 |                65 |                1 |               0 |              65 |               0 |              64 |                 1.81648   | contained cells imply decimal zero-sector |
|                       3 |    9 |                  4 |               263 |               262 |                1 |               0 |             262 |               0 |             261 |                 2.41854   | contained cells imply decimal zero-sector |
|                       3 |   10 |                  5 |              1049 |              1048 |                1 |               0 |            1048 |               0 |            1047 |                 3.0206    | contained cells imply decimal zero-sector |
|                       3 |   11 |                  6 |              4195 |              4194 |                1 |               0 |            4194 |               0 |            4193 |                 3.62266   | contained cells imply decimal zero-sector |
|                       6 |   10 |                  0 |                 2 |                 1 |                1 |               0 |               1 |               0 |               0 |                 0.0205999 | contained cells imply decimal zero-sector |
|                       6 |   11 |                  1 |                 5 |                 4 |                1 |               0 |               4 |               0 |               3 |                 0.62266   | contained cells imply decimal zero-sector |
|                       6 |   12 |                  2 |                17 |                16 |                1 |               0 |              16 |               0 |              15 |                 1.22472   | contained cells imply decimal zero-sector |
|                       6 |   13 |                  3 |                68 |                67 |                1 |               0 |              67 |               0 |              66 |                 1.82678   | contained cells imply decimal zero-sector |
|                       6 |   14 |                  4 |               269 |               268 |                1 |               0 |             268 |               0 |             267 |                 2.42884   | contained cells imply decimal zero-sector |
|                       6 |   15 |                  5 |              1074 |              1073 |                1 |               0 |            1073 |               0 |            1072 |                 3.0309    | contained cells imply decimal zero-sector |
|                       6 |   16 |                  6 |              4295 |              4294 |                1 |               0 |            4294 |               0 |            4293 |                 3.63296   | contained cells imply decimal zero-sector |
|                      10 |   17 |                  0 |                 2 |                 1 |                1 |               0 |               1 |               0 |               0 |                 0.23502   | contained cells imply decimal zero-sector |
|                      10 |   18 |                  1 |                 7 |                 6 |                1 |               0 |               6 |               0 |               5 |                 0.83708   | contained cells imply decimal zero-sector |
|                      10 |   19 |                  2 |                28 |                27 |                1 |               0 |              27 |               0 |              26 |                 1.43914   | contained cells imply decimal zero-sector |
|                      10 |   20 |                  3 |               110 |               109 |                1 |               0 |             109 |               0 |             108 |                 2.0412    | contained cells imply decimal zero-sector |
|                      10 |   21 |                  4 |               440 |               439 |                1 |               0 |             439 |               0 |             438 |                 2.64326   | contained cells imply decimal zero-sector |
|                      10 |   22 |                  5 |              1760 |              1759 |                1 |               0 |            1759 |               0 |            1758 |                 3.24532   | contained cells imply decimal zero-sector |
|                      10 |   23 |                  6 |              7037 |              7036 |                1 |               0 |            7036 |               0 |            7035 |                 3.84738   | contained cells imply decimal zero-sector |
|                      50 |   84 |                  0 |                 4 |                 3 |                1 |               0 |               3 |               0 |               2 |                 0.573039  | contained cells imply decimal zero-sector |
|                      50 |   85 |                  1 |                15 |                14 |                1 |               0 |              14 |               0 |              13 |                 1.1751    | contained cells imply decimal zero-sector |
|                      50 |   86 |                  2 |                60 |                59 |                1 |               0 |              59 |               0 |              58 |                 1.77716   | contained cells imply decimal zero-sector |
|                      50 |   87 |                  3 |               240 |               239 |                1 |               0 |             239 |               0 |             238 |                 2.37922   | contained cells imply decimal zero-sector |
|                      50 |   88 |                  4 |               958 |               957 |                1 |               0 |             957 |               0 |             956 |                 2.98128   | contained cells imply decimal zero-sector |
|                      50 |   89 |                  5 |              3832 |              3831 |                1 |               0 |            3831 |               0 |            3830 |                 3.58334   | contained cells imply decimal zero-sector |
|                      50 |   90 |                  6 |             15325 |             15324 |                1 |               0 |           15324 |               0 |           15323 |                 4.1854    | contained cells imply decimal zero-sector |
|                     100 |  167 |                  0 |                 4 |                 3 |                1 |               0 |               3 |               0 |               2 |                 0.544019  | contained cells imply decimal zero-sector |
|                     100 |  168 |                  1 |                14 |                13 |                1 |               0 |              13 |               0 |              12 |                 1.14608   | contained cells imply decimal zero-sector |
|                     100 |  169 |                  2 |                56 |                55 |                1 |               0 |              55 |               0 |              54 |                 1.74814   | contained cells imply decimal zero-sector |
|                     100 |  170 |                  3 |               224 |               223 |                1 |               0 |             223 |               0 |             222 |                 2.3502    | contained cells imply decimal zero-sector |
|                     100 |  171 |                  4 |               896 |               895 |                1 |               0 |             895 |               0 |             894 |                 2.95226   | contained cells imply decimal zero-sector |
|                     100 |  172 |                  5 |              3584 |              3583 |                1 |               0 |            3583 |               0 |            3582 |                 3.55432   | contained cells imply decimal zero-sector |
|                     100 |  173 |                  6 |             14335 |             14334 |                1 |               0 |           14334 |               0 |           14333 |                 4.15638   | contained cells imply decimal zero-sector |
|                    1000 | 1661 |                  0 |                 2 |                 1 |                1 |               0 |               1 |               0 |               0 |                 0.0216456 | contained cells imply decimal zero-sector |
|                    1000 | 1662 |                  1 |                 5 |                 4 |                1 |               0 |               4 |               0 |               3 |                 0.623706  | contained cells imply decimal zero-sector |
|                    1000 | 1663 |                  2 |                17 |                16 |                1 |               0 |              16 |               0 |              15 |                 1.22577   | contained cells imply decimal zero-sector |
|                    1000 | 1664 |                  3 |                68 |                67 |                1 |               0 |              67 |               0 |              66 |                 1.82783   | contained cells imply decimal zero-sector |
|                    1000 | 1665 |                  4 |               270 |               269 |                1 |               0 |             269 |               0 |             268 |                 2.42989   | contained cells imply decimal zero-sector |
|                    1000 | 1666 |                  5 |              1077 |              1076 |                1 |               0 |            1076 |               0 |            1075 |                 3.03195   | contained cells imply decimal zero-sector |
|                    1000 | 1667 |                  6 |              4306 |              4305 |                1 |               0 |            4305 |               0 |            4304 |                 3.63401   | contained cells imply decimal zero-sector |

Interpretation:

- Decimal 1000 zeros can be represented as a tiny target sector.
- At quaternary depth 1661, the decimal-zero sector intersects a very small number of quaternary cells.
- Contained cells give strict certificates: if a phase point lands in such a quaternary cell, it is guaranteed to be inside the decimal zero sector.
- Boundary cells require refinement.

## D. Dynamics matrix summaries

For the phase map:

```text
f_B(u) = {B u}
```

the finite-grid dynamics matrix maps source cells to target cells.

|       B |   Q |   L |   N_cells |   mean_target_cells_per_source |   min_target_cells_per_source |   max_target_cells_per_source |
|--------:|----:|----:|----------:|-------------------------------:|------------------------------:|------------------------------:|
|  4      |   4 |   1 |         4 |                         4      |                             4 |                             4 |
| 10      |  10 |   1 |        10 |                        10      |                            10 |                            10 |
| 12.5664 |   4 |   1 |         4 |                         4      |                             4 |                             4 |
|  4      |   4 |   2 |        16 |                         4      |                             4 |                             4 |
| 10      |  10 |   2 |       100 |                        10.7    |                            10 |                            12 |
| 12.5664 |   4 |   2 |        16 |                        13.5625 |                            13 |                            14 |
|  4      |   4 |   3 |        64 |                         4      |                             4 |                             4 |
| 10      |  10 |   3 |      1000 |                        10.789  |                            10 |                            12 |
| 12.5664 |   4 |   3 |        64 |                        13.5625 |                            13 |                            14 |
|  4      |   4 |   4 |       256 |                         4      |                             4 |                             4 |
| 10      |  10 |   4 |     10000 |                        10.7905 |                            10 |                            12 |
| 12.5664 |   4 |   4 |       256 |                        13.5625 |                            13 |                            14 |
|  4      |   4 |   5 |      1024 |                         4      |                             4 |                             4 |
| 12.5664 |   4 |   5 |      1024 |                        13.5654 |                            13 |                            14 |

Interpretation:

- Integer `B=Q` dynamics has the expected finite branching.
- The internal `B=4π, Q=4` layer has a wider image per source cell because one source interval expands by about `4π`.

## E. Same-orbit decimal sector query through a base-4 index

This demonstrates the transform machinery. It uses the base-4 phase orbit `{4^(m-1)π}` and asks whether that same orbit falls into decimal-defined sectors. This is **not** decimal digit lookup, because decimal digit lookup uses `{10^(m-1)π}`.

Input stream source: `fallback random base-4 stream; mechanics only`.

Index depth: `Lmax4 = 12`.

Sample query results:

|   decimal_D |   A |   Lmax4 |   intersect_cells_total |   contained_cells_total |   boundary_cells_total |   occupied_intersect_cells |   min_m_intersect_candidate |   occupied_contained_cells |   min_m_contained_guaranteed_same_orbit | note                                                         |
|------------:|----:|--------:|------------------------:|------------------------:|-----------------------:|---------------------------:|----------------------------:|---------------------------:|----------------------------------------:|:-------------------------------------------------------------|
|           1 |   0 |      12 |                 1677722 |                 1677721 |                      1 |                      97159 |                           4 |                      97159 |                                       4 | same phase-orbit transform only; not decimal digit positions |
|           1 |   5 |      12 |                 1677722 |                 1677721 |                      1 |                      96941 |                          17 |                      96941 |                                      17 | same phase-orbit transform only; not decimal digit positions |
|           1 |   9 |      12 |                 1677722 |                 1677721 |                      1 |                      96945 |                          23 |                      96945 |                                      23 | same phase-orbit transform only; not decimal digit positions |
|           1 |   0 |      12 |                 1677722 |                 1677721 |                      1 |                      97159 |                           4 |                      97159 |                                       4 | same phase-orbit transform only; not decimal digit positions |
|           1 |   4 |      12 |                 1677722 |                 1677721 |                      1 |                      96956 |                          35 |                      96956 |                                      35 | same phase-orbit transform only; not decimal digit positions |
|           1 |   1 |      12 |                 1677723 |                 1677721 |                      2 |                      97029 |                           8 |                      97029 |                                       8 | same phase-orbit transform only; not decimal digit positions |
|           1 |   6 |      12 |                 1677723 |                 1677721 |                      2 |                      96769 |                           9 |                      96769 |                                       9 | same phase-orbit transform only; not decimal digit positions |
|           1 |   3 |      12 |                 1677723 |                 1677721 |                      2 |                      96689 |                          30 |                      96689 |                                      30 | same phase-orbit transform only; not decimal digit positions |
|           1 |   2 |      12 |                 1677722 |                 1677720 |                      2 |                      97375 |                           1 |                      97375 |                                       1 | same phase-orbit transform only; not decimal digit positions |
|           1 |   9 |      12 |                 1677722 |                 1677721 |                      1 |                      96945 |                          23 |                      96945 |                                      23 | same phase-orbit transform only; not decimal digit positions |
|           1 |   5 |      12 |                 1677722 |                 1677721 |                      1 |                      96941 |                          17 |                      96941 |                                      17 | same phase-orbit transform only; not decimal digit positions |
|           1 |   7 |      12 |                 1677722 |                 1677720 |                      2 |                      97044 |                          10 |                      97044 |                                      10 | same phase-orbit transform only; not decimal digit positions |
|           1 |   8 |      12 |                 1677723 |                 1677721 |                      2 |                      97668 |                           2 |                      97668 |                                       2 | same phase-orbit transform only; not decimal digit positions |
|           2 |   0 |      12 |                  167773 |                  167772 |                      1 |                       9785 |                         295 |                       9785 |                                     295 | same phase-orbit transform only; not decimal digit positions |
|           2 |  50 |      12 |                  167773 |                  167772 |                      1 |                       9712 |                         189 |                       9712 |                                     189 | same phase-orbit transform only; not decimal digit positions |
|           2 |  99 |      12 |                  167773 |                  167772 |                      1 |                       9684 |                          92 |                       9684 |                                      92 | same phase-orbit transform only; not decimal digit positions |
|           2 |  43 |      12 |                  167774 |                  167772 |                      2 |                       9694 |                         222 |                       9694 |                                     222 | same phase-orbit transform only; not decimal digit positions |
|           2 |   6 |      12 |                  167774 |                  167772 |                      2 |                       9762 |                           5 |                       9761 |                                       5 | same phase-orbit transform only; not decimal digit positions |
|           2 |  20 |      12 |                  167773 |                  167771 |                      2 |                       9691 |                           1 |                       9691 |                                       1 | same phase-orbit transform only; not decimal digit positions |
|           2 |  17 |      12 |                  167773 |                  167771 |                      2 |                       9717 |                           8 |                       9717 |                                       8 | same phase-orbit transform only; not decimal digit positions |
|           2 |  71 |      12 |                  167773 |                  167771 |                      2 |                       9559 |                          36 |                       9559 |                                      36 | same phase-orbit transform only; not decimal digit positions |
|           2 |  42 |      12 |                  167773 |                  167771 |                      2 |                       9504 |                          35 |                       9504 |                                      35 | same phase-orbit transform only; not decimal digit positions |
|           2 |  89 |      12 |                  167773 |                  167771 |                      2 |                       9890 |                          16 |                       9890 |                                      16 | same phase-orbit transform only; not decimal digit positions |
|           2 |  31 |      12 |                  167774 |                  167772 |                      2 |                       9623 |                          42 |                       9622 |                                      42 | same phase-orbit transform only; not decimal digit positions |
|           2 |   0 |      12 |                  167773 |                  167772 |                      1 |                       9785 |                         295 |                       9785 |                                     295 | same phase-orbit transform only; not decimal digit positions |
|           2 |  55 |      12 |                  167773 |                  167771 |                      2 |                       9650 |                          98 |                       9650 |                                      98 | same phase-orbit transform only; not decimal digit positions |
|           2 |  99 |      12 |                  167773 |                  167772 |                      1 |                       9684 |                          92 |                       9684 |                                      92 | same phase-orbit transform only; not decimal digit positions |
|           2 |  11 |      12 |                  167773 |                  167771 |                      2 |                       9709 |                          53 |                       9709 |                                      53 | same phase-orbit transform only; not decimal digit positions |
|           2 |  76 |      12 |                  167773 |                  167771 |                      2 |                       9786 |                          82 |                       9786 |                                      82 | same phase-orbit transform only; not decimal digit positions |
|           2 |  48 |      12 |                  167773 |                  167771 |                      2 |                       9816 |                          39 |                       9816 |                                      39 | same phase-orbit transform only; not decimal digit positions |
|           2 |   8 |      12 |                  167773 |                  167771 |                      2 |                       9654 |                          32 |                       9654 |                                      32 | same phase-orbit transform only; not decimal digit positions |
|           2 |  40 |      12 |                  167773 |                  167771 |                      2 |                       9716 |                          74 |                       9715 |                                      74 | same phase-orbit transform only; not decimal digit positions |
|           2 |  93 |      12 |                  167774 |                  167772 |                      2 |                       9729 |                         231 |                       9729 |                                     231 | same phase-orbit transform only; not decimal digit positions |
|           2 |  57 |      12 |                  167773 |                  167771 |                      2 |                       9835 |                          17 |                       9835 |                                      17 | same phase-orbit transform only; not decimal digit positions |
|           2 |  13 |      12 |                  167773 |                  167771 |                      2 |                       9732 |                          59 |                       9732 |                                      59 | same phase-orbit transform only; not decimal digit positions |
|           2 |   5 |      12 |                  167773 |                  167771 |                      2 |                       9778 |                          27 |                       9778 |                                      27 | same phase-orbit transform only; not decimal digit positions |
|           3 |   0 |      12 |                   16778 |                   16777 |                      1 |                       1019 |                         970 |                       1019 |                                     970 | same phase-orbit transform only; not decimal digit positions |
|           3 | 500 |      12 |                   16778 |                   16777 |                      1 |                        973 |                        2355 |                        973 |                                    2355 | same phase-orbit transform only; not decimal digit positions |
|           3 | 999 |      12 |                   16778 |                   16777 |                      1 |                        915 |                        1453 |                        915 |                                    1453 | same phase-orbit transform only; not decimal digit positions |
|           3 |  94 |      12 |                   16778 |                   16776 |                      2 |                        978 |                        1186 |                        978 |                                    1186 | same phase-orbit transform only; not decimal digit positions |

Interpretation:

- A decimal target sector can be transformed into a small base-4 cell range.
- The sparse base-4 sector index can answer range-min queries over that transformed range.
- Contained-cell results are guaranteed for the same phase orbit.
- Boundary-cell results are candidates needing interval/chord certification.

## Conclusion

Confirmed:

1. Binary/quaternary conversion is exactly a sector permutation.
2. Decimal/quaternary transforms are sparse at comparable depths.
3. Containment matrices give strict cross-grid certificates.
4. Dynamics matrices describe how a chosen oscillator `(B,Q)` moves sector cells.
5. A base-4 finite index can query transformed decimal sectors on the same orbit.

Not claimed:

- This does not locate decimal digits of pi using a base-4 orbit.
- It does not solve first occurrence outside a built finite horizon.
- It does not prove resonance compression.

Next step:

Build an implementation module for:

```text
sector_overlap(Q,L,Q2,L2)
sector_containment(Q,L,Q2,L2)
sector_transform_query(target, source_index)
```

and integrate it into `pi-fs locate` as a cross-layer target transform.
