# pi-fs experiment 002: sector-tree, chord margins, and drift features

## Setup

- Horizon: first 1,000,000 base-4 fractional digits of pi.
- Source: reused generated base-4 pi digits from prior run.
- Base/digit layer: B=4, Q=4.
- Pattern lengths for first occurrences: 8, 9, 10 base-4 digits.
- Goal: test whether the geometry developed for pi-fs gives measurable candidate-space compression.

## 1. First-occurrence coverage

|   L_base4 |   patterns_total |   patterns_found |   coverage |   mean_first_pos_found |   median_first_pos_found |   max_first_pos_found |
|----------:|-----------------:|-----------------:|-----------:|-----------------------:|-------------------------:|----------------------:|
|         8 |  65536           |            65536 |   1        |                65741.1 |                    45480 |                702826 |
|         9 | 262144           |           256404 |   0.978104 |               240292   |                   176748 |                999960 |
|        10 |      1.04858e+06 |           644370 |   0.614519 |               422021   |                   385446 |                999985 |

Interpretation:

- Short base-4 patterns are fully covered.
- L=10 is partial at this horizon, as expected because 4^10 ≈ 1.05M.

## 2. Sector-tree / quadtree prefix pruning

A base-4 string is a path in a quadtree over the circle. Prefix length k should reduce candidate count by about 4^k.

|   prefix_depth_k |   mean_candidates |   median_candidates |   p90_candidates |   expected_random_H_over_4k |   compression_vs_H_mean |
|-----------------:|------------------:|--------------------:|-----------------:|----------------------------:|------------------------:|
|                1 |       249996      |              249976 |           250657 |               250000        |                 4.00006 |
|                2 |        62500.8    |               62502 |            62791 |                62500        |                15.9998  |
|                3 |        15626.1    |               15633 |            15791 |                15625        |                63.9955  |
|                4 |         3908.06   |                3907 |             3993 |                 3906.25     |               255.882   |
|                5 |          976.692  |                 976 |             1021 |                  976.562    |              1023.86    |
|                6 |          244.709  |                 244 |              264 |                  244.141    |              4086.48    |
|                7 |           61.6622 |                  61 |               72 |                   61.0352   |             16217.4     |
|                8 |           15.9066 |                  16 |               21 |                   15.2588   |             62867       |
|                9 |            4.4536 |                   4 |                7 |                    3.8147   |            224537       |
|               10 |            1.5478 |                   1 |                3 |                    0.953674 |            646078       |

This confirms the finite sector-index behavior: after the index is built, lookup cost is O(L), and candidate count decays geometrically with prefix depth.

## 3. Chord margin distribution

For a first hit, the chord margin measures how far the phase lies from the nearest boundary of its sector.
Normalized margin:
- 0 = boundary,
- 1 = sector center.

|   L_base4 |   sample_size |   mean_margin_norm |   median_margin_norm |   p10_margin_norm |   p01_margin_norm |   fraction_margin_lt_0_01 |   fraction_margin_lt_0_001 |
|----------:|--------------:|-------------------:|---------------------:|------------------:|------------------:|--------------------------:|---------------------------:|
|         8 |         65536 |           0.499656 |             0.4991   |         0.0992432 |        0.00964355 |                 0.0102539 |                 0.00114441 |
|         9 |        100000 |           0.500765 |             0.502365 |         0.0996094 |        0.0100708  |                 0.0099    |                 0.00098    |
|        10 |        100000 |           0.500296 |             0.501175 |         0.100827  |        0.00961304 |                 0.01029   |                 0.00101    |

Interpretation:

- The margin distribution is close to uniform.
- Most hits are not pathological boundary cases.
- Interval certification should usually succeed without excessive precision.
- Boundary-near hits exist, so accept/reject/refine logic is necessary.

## 4. Base-4 resonance pairs

Convergents for log_4(pi), i.e. pi^N ≈ 4^K:

|   cf_index |     K |     N |      epsilon |   abs_epsilon |   K_over_N |
|-----------:|------:|------:|-------------:|--------------:|-----------:|
|          6 |    90 |   109 |  0.00906506  |   0.00906506  |   0.825688 |
|          7 |   109 |   132 | -0.00174043  |   0.00174043  |   0.825758 |
|          8 |   635 |   769 |  0.000362907 |   0.000362907 |   0.825748 |
|          9 |  2649 |  3208 | -0.000288802 |   0.000288802 |   0.825748 |
|         10 |  3284 |  3977 |  7.41053e-05 |   7.41053e-05 |   0.825748 |
|         11 | 12501 | 15139 | -6.64857e-05 |   6.64857e-05 |   0.825748 |
|         12 | 15785 | 19116 |  7.61966e-06 |   7.61966e-06 |   0.825748 |

## 5. Drift-phase feature benchmark

Tested three train/test window features for first occurrences of L=8 strings:

- `drift`: bin of frac(-q epsilon / ln 4);
- `rcoarse`: coarse bin of residue r/K;
- `r_drift_2d`: 2D bin combining coarse residue and drift.

A lift > 1 means better than selecting random bins of the same coverage.

| dataset   | feature    |     K |     N |   abs_epsilon |   n_bins |   coverage |   recall_mean |   recall_sd |   lift_mean |     lift_sd |
|:----------|:-----------|------:|------:|--------------:|---------:|-----------:|--------------:|------------:|------------:|------------:|
| pi        | drift      |    90 |   109 |   0.00906506  |      256 |  0.0507812 |     0.074588  | 0.0014832   |    1.46881  | 0.0292075   |
| pi        | rcoarse    |    90 |   109 |   0.00906506  |      256 |  0.0507812 |     0.142075  | 0.00172489  |    2.79778  | 0.0339671   |
| pi        | r_drift_2d |    90 |   109 |   0.00906506  |     1024 |  0.0498047 |     0.0510284 | 0.00106326  |    1.02457  | 0.0213486   |
| random    | drift      |    90 |   109 |   0.00906506  |      256 |  0.0507812 |     0.0763947 | 0.00117086  |    1.50439  | 0.023057    |
| random    | rcoarse    |    90 |   109 |   0.00906506  |      256 |  0.0507812 |     0.141211  | 0.0012229   |    2.78077  | 0.0240817   |
| random    | r_drift_2d |    90 |   109 |   0.00906506  |     1024 |  0.0498047 |     0.0530182 | 0.0011043   |    1.06452  | 0.0221727   |
| pi        | drift      |   109 |   132 |   0.00174043  |      256 |  0.0507812 |     0.0886292 | 0.000825307 |    1.74531  | 0.0162522   |
| pi        | rcoarse    |   109 |   132 |   0.00174043  |      256 |  0.0507812 |     0.117453  | 0.000829612 |    2.31292  | 0.016337    |
| pi        | r_drift_2d |   109 |   132 |   0.00174043  |     1024 |  0.0498047 |     0.0891907 | 0.00156797  |    1.79081  | 0.0314825   |
| random    | drift      |   109 |   132 |   0.00174043  |      256 |  0.0507812 |     0.0896698 | 0.000841649 |    1.76581  | 0.016574    |
| random    | rcoarse    |   109 |   132 |   0.00174043  |      256 |  0.0507812 |     0.115536  | 0.00117558  |    2.27518  | 0.0231498   |
| random    | r_drift_2d |   109 |   132 |   0.00174043  |     1024 |  0.0498047 |     0.0906433 | 0.00192105  |    1.81998  | 0.0385716   |
| pi        | drift      |   635 |   769 |   0.000362907 |      256 |  0.0507812 |     0.837079  | 0.0021524   |   16.484    | 0.0423856   |
| pi        | rcoarse    |   635 |   769 |   0.000362907 |      256 |  0.0507812 |     0.059552  | 0.000883556 |    1.17272  | 0.0173993   |
| pi        | r_drift_2d |   635 |   769 |   0.000362907 |     1024 |  0.0498047 |     0.803293  | 0.00100431  |   16.1289   | 0.0201649   |
| random    | drift      |   635 |   769 |   0.000362907 |      256 |  0.0507812 |     0.83613   | 0.0016808   |   16.4653   | 0.0330988   |
| random    | rcoarse    |   635 |   769 |   0.000362907 |      256 |  0.0507812 |     0.0615753 | 0.00110143  |    1.21256  | 0.0216897   |
| random    | r_drift_2d |   635 |   769 |   0.000362907 |     1024 |  0.0498047 |     0.802808  | 0.00179282  |   16.1191   | 0.0359971   |
| pi        | drift      |  2649 |  3208 |   0.000288802 |      256 |  0.0507812 |     0.999948  | 5.11568e-05 |   19.6913   | 0.0010074   |
| pi        | rcoarse    |  2649 |  3208 |   0.000288802 |      256 |  0.0507812 |     0.0516144 | 0.000723215 |    1.01641  | 0.0142418   |
| pi        | r_drift_2d |  2649 |  3208 |   0.000288802 |     1024 |  0.0498047 |     0.999146  | 0.000138511 |   20.0613   | 0.00278108  |
| random    | drift      |  2649 |  3208 |   0.000288802 |      256 |  0.0507812 |     0.99993   | 5.11568e-05 |   19.6909   | 0.0010074   |
| random    | rcoarse    |  2649 |  3208 |   0.000288802 |      256 |  0.0507812 |     0.053656  | 0.000639531 |    1.05661  | 0.0125938   |
| random    | r_drift_2d |  2649 |  3208 |   0.000288802 |     1024 |  0.0498047 |     0.998898  | 8.68009e-05 |   20.0563   | 0.00174283  |
| pi        | drift      |  3284 |  3977 |   7.41053e-05 |      256 |  0.0507812 |     1         | 0           |   19.6923   | 3.55271e-15 |
| pi        | rcoarse    |  3284 |  3977 |   7.41053e-05 |      256 |  0.0507812 |     0.049942  | 0.00127527  |    0.983474 | 0.0251131   |
| pi        | r_drift_2d |  3284 |  3977 |   7.41053e-05 |     1024 |  0.0498047 |     0.978683  | 0.000346143 |   19.6504   | 0.00695     |
| random    | drift      |  3284 |  3977 |   7.41053e-05 |      256 |  0.0507812 |     1         | 0           |   19.6923   | 3.55271e-15 |
| random    | rcoarse    |  3284 |  3977 |   7.41053e-05 |      256 |  0.0507812 |     0.0491852 | 0.000612644 |    0.96857  | 0.0120644   |
| random    | r_drift_2d |  3284 |  3977 |   7.41053e-05 |     1024 |  0.0498047 |     0.978696  | 0.000624001 |   19.6507   | 0.012529    |
| pi        | drift      | 12501 | 15139 |   6.64857e-05 |      256 |  0.0507812 |     1         | 0           |   19.6923   | 3.55271e-15 |
| pi        | rcoarse    | 12501 | 15139 |   6.64857e-05 |      256 |  0.0507812 |     0.0515381 | 0.00110504  |    1.0149   | 0.0217608   |
| pi        | r_drift_2d | 12501 | 15139 |   6.64857e-05 |     1024 |  0.0498047 |     1         | 0           |   20.0784   | 3.55271e-15 |
| random    | drift      | 12501 | 15139 |   6.64857e-05 |      256 |  0.0507812 |     1         | 0           |   19.6923   | 3.55271e-15 |
| random    | rcoarse    | 12501 | 15139 |   6.64857e-05 |      256 |  0.0507812 |     0.0518707 | 0.000744535 |    1.02145  | 0.0146616   |
| random    | r_drift_2d | 12501 | 15139 |   6.64857e-05 |     1024 |  0.0498047 |     1         | 0           |   20.0784   | 3.55271e-15 |
| pi        | drift      | 15785 | 19116 |   7.61966e-06 |      256 |  0.0507812 |     1         | 0           |   19.6923   | 3.55271e-15 |
| pi        | rcoarse    | 15785 | 19116 |   7.61966e-06 |      256 |  0.0507812 |     0.0529205 | 0.000930506 |    1.04213  | 0.0183238   |
| pi        | r_drift_2d | 15785 | 19116 |   7.61966e-06 |     1024 |  0.0498047 |     0.917078  | 0.00124411  |   18.4135   | 0.0249799   |
| random    | drift      | 15785 | 19116 |   7.61966e-06 |      256 |  0.0507812 |     1         | 0           |   19.6923   | 3.55271e-15 |
| random    | rcoarse    | 15785 | 19116 |   7.61966e-06 |      256 |  0.0507812 |     0.0528961 | 0.000926554 |    1.04165  | 0.018246    |
| random    | r_drift_2d | 15785 | 19116 |   7.61966e-06 |     1024 |  0.0498047 |     0.916635  | 0.00120489  |   18.4046   | 0.0241923   |

## Preliminary conclusion

- The sector/quadtree index is real and useful as a finite-horizon index.
- Chord geometry is useful for certification and margin scoring.
- Residue-only features failed in experiment 001.
- Drift-only and simple 2D residue+drift features also do not show robust lift over random data.
- Current evidence says: the finite geometric index is practical; the resonance layer has not yet demonstrated predictive compression.

## Next research direction

The next candidate should not be a low-dimensional residue/drift bin. It must rank candidates by an approximate chord score:

score(S,q,r) = p(q,r) · v_S

while computing p(q,r) cheaper than direct digit extraction. If no cheaper approximation exists, the method reduces to ordinary sector search.
