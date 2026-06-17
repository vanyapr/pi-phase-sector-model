# pi-fs experiment 007: walk-forward zero-block prediction

## Goal

Before claiming prediction beyond the known horizon, test whether the current models can predict future zero blocks inside already computed digits.

For each cutoff `T`, the model may use only zero hits before `T`.
Then it predicts candidate windows/sets after `T`.
We compare with the true next zero-block start already known from the computed data.

This is a backtest of:

```text
can we predict future zero-block positions, not just certify them after finding them?
```

## Setup

```json
{
  "experiment": "007",
  "description": "walk-forward zero-block prediction on already computed pi digits",
  "H_decimal_positions": 2000000,
  "source": "generated decimal pi digits with mpmath",
  "mpmath_dps": 2000031,
  "generation_seconds": 29.517972230911255,
  "D_values": [
    3,
    4,
    5,
    6
  ],
  "K_values": [
    87,
    1221,
    5669
  ],
  "top_fracs": [
    0.01,
    0.05,
    0.1,
    0.2
  ],
  "first_80_decimal_digits": "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
}
```

## Zero-hit summary

|   D |   hits |         first_M |   first_position |      last_M |   mean_gap |   median_gap |   random_expected_gap_approx |
|----:|-------:|----------------:|-----------------:|------------:|-----------:|-------------:|-----------------------------:|
|   3 |   1920 |   600           |    601           | 1.99938e+06 |    1041.57 |          719 |                     1000     |
|   4 |    173 | 13389           |  13390           | 1.99937e+06 |   11546.4  |         8249 |                    10000     |
|   5 |     14 | 17533           |  17534           | 1.96186e+06 |  149563    |        83163 |                   100000     |
|   6 |      1 |     1.69993e+06 |      1.69993e+06 | 1.69993e+06 |     nan    |          nan |                        1e+06 |

## Walk-forward cutoffs

Number of cutoff tests:

```text
375
```

Per D:

|   D |   cutoff_tests |
|----:|---------------:|
|   3 |            157 |
|   4 |            161 |
|   5 |             57 |

## Random/extreme-value baseline

For a block of D zeros, the random model uses:

```text
P(hit within T_window) ~= 1 - exp(-T_window / 10^D)
```

so a nominal p-window is:

```text
T_window = -ln(1-p) * 10^D
```

Summary:

|   D |   confidence_nominal |   tests |   hit_rate |   mean_window_width |   mean_compression |
|----:|---------------------:|--------:|-----------:|--------------------:|-------------------:|
|   3 |                 0.5  |     157 |   0.726115 |                 694 |         0.00175335 |
|   3 |                 0.8  |     157 |   0.872611 |                1610 |         0.00406757 |
|   3 |                 0.95 |     157 |   0.974522 |                2996 |         0.00756921 |
|   4 |                 0.5  |     161 |   0.695652 |                6932 |         0.0865075  |
|   4 |                 0.8  |     161 |   0.826087 |               16095 |         0.200857   |
|   4 |                 0.95 |     161 |   0.981366 |               29958 |         0.373859   |
|   5 |                 0.5  |      57 |   0.491228 |               69315 |         0.25702    |
|   5 |                 0.8  |      57 |   0.666667 |              160944 |         0.59678    |
|   5 |                 0.95 |      57 |   0.807018 |              299574 |         1.11082    |

## Empirical gap baseline

Use observed train gaps before the cutoff and take empirical p-quantile as the predicted window width.

|   D |   confidence_nominal |   tests |   hit_rate |   mean_window_width |   mean_compression |
|----:|---------------------:|--------:|-----------:|--------------------:|-------------------:|
|   3 |                 0.5  |     157 |   0.713376 |             688.064 |         0.00176889 |
|   3 |                 0.8  |     157 |   0.898089 |            1746.69  |         0.00438711 |
|   3 |                 0.95 |     157 |   0.980892 |            3228.96  |         0.00824934 |
|   4 |                 0.5  |     160 |   0.7      |            7469.09  |         0.10257    |
|   4 |                 0.8  |     160 |   0.8625   |           19002.9   |         0.257949   |
|   4 |                 0.95 |     160 |   0.975    |           28607.9   |         0.422267   |
|   5 |                 0.5  |      47 |   0.680851 |          175060     |         0.597833   |
|   5 |                 0.8  |      47 |   0.723404 |          295241     |         1.17441    |
|   5 |                 0.95 |      47 |   0.829787 |          461671     |         2.15313    |

## Resonance-residue prediction

Use train zero hits before the cutoff.
For each K, select top residue classes modulo K.
Prediction set after cutoff is all positions with selected residues.
This tests whether zero hits have stable resonance residues.

|   D |    K |   top_fraction |   tests |     recall |   coverage |   mean_abs_error |   median_abs_error |     lift |
|----:|-----:|---------------:|--------:|-----------:|-----------:|-----------------:|-------------------:|---------:|
|   3 |   87 |           0.01 |     157 | 0.0127389  | 0.0114943  |          549.962 |                 83 | 1.10828  |
|   3 |   87 |           0.05 |     157 | 0.0382166  | 0.045977   |          549.357 |                 46 | 0.83121  |
|   3 |   87 |           0.1  |     157 | 0.11465    | 0.103448   |          549.076 |                 24 | 1.10828  |
|   3 |   87 |           0.2  |     157 | 0.216561   | 0.195402   |          549.229 |                 17 | 1.10828  |
|   3 | 1221 |           0.01 |     157 | 0          | 0.00982801 |          546.293 |                174 | 0        |
|   3 | 1221 |           0.05 |     157 | 0.0636943  | 0.049959   |          548.783 |                 79 | 1.27493  |
|   3 | 1221 |           0.1  |     157 | 0.10828    | 0.0999181  |          550.242 |                 79 | 1.08369  |
|   3 | 1221 |           0.2  |     157 | 0.235669   | 0.199836   |          550.013 |                 29 | 1.17931  |
|   3 | 5669 |           0.01 |     157 | 0.0191083  | 0.0100547  |          553.433 |                204 | 1.90044  |
|   3 | 5669 |           0.05 |     157 | 0.0700637  | 0.0499206  |          547.758 |                132 | 1.4035   |
|   3 | 5669 |           0.1  |     157 | 0.101911   | 0.100018   |          549.847 |                121 | 1.01893  |
|   3 | 5669 |           0.2  |     157 | 0.178344   | 0.200035   |          549.726 |                 55 | 0.891562 |
|   4 |   87 |           0.01 |     161 | 0.0124224  | 0.0114943  |         5810     |                 82 | 1.08075  |
|   4 |   87 |           0.05 |     161 | 0.0186335  | 0.045977   |         5818.62  |                 53 | 0.40528  |
|   4 |   87 |           0.1  |     161 | 0.0434783  | 0.103448   |         5818.51  |                 31 | 0.42029  |
|   4 |   87 |           0.2  |     161 | 0.10559    | 0.195402   |         5816.1   |                 17 | 0.540373 |
|   4 | 1221 |           0.01 |     161 | 0.00621118 | 0.00982801 |         5823.31  |                269 | 0.631988 |
|   4 | 1221 |           0.05 |     161 | 0.0496894  | 0.049959   |         5817.58  |                165 | 0.994603 |
|   4 | 1221 |           0.1  |     161 | 0.0807453  | 0.0999181  |         5818.58  |                165 | 0.808115 |
|   4 | 1221 |           0.2  |     161 | 0.173913   | 0.199836   |         5817.8   |                 77 | 0.870278 |
|   4 | 5669 |           0.01 |     161 | 0.0124224  | 0.0100547  |         5830.94  |                357 | 1.23548  |
|   4 | 5669 |           0.05 |     161 | 0.0372671  | 0.0499206  |         5828.41  |                338 | 0.746527 |
|   4 | 5669 |           0.1  |     161 | 0.0621118  | 0.100018   |         5824.12  |                293 | 0.621008 |
|   4 | 5669 |           0.2  |     161 | 0.15528    | 0.200035   |         5833.07  |                290 | 0.776261 |
|   5 |   87 |           0.01 |      57 | 0          | 0.0114943  |       147258     |              79643 | 0        |
|   5 |   87 |           0.05 |      57 | 0.0350877  | 0.045977   |       147259     |              79660 | 0.763158 |
|   5 |   87 |           0.1  |      57 | 0.105263   | 0.103448   |       147262     |              79660 | 1.01754  |
|   5 |   87 |           0.2  |      57 | 0.105263   | 0.195402   |       147266     |              79660 | 0.5387   |
|   5 | 1221 |           0.01 |      57 | 0          | 0.00982801 |       147171     |              79559 | 0        |
|   5 | 1221 |           0.05 |      57 | 0          | 0.049959   |       147177     |              79559 | 0        |
|   5 | 1221 |           0.1  |      57 | 0.105263   | 0.0999181  |       147180     |              79559 | 1.05349  |
|   5 | 1221 |           0.2  |      57 | 0.350877   | 0.199836   |       147194     |              79559 | 1.75582  |
|   5 | 5669 |           0.01 |      57 | 0          | 0.0100547  |       146823     |              78728 | 0        |
|   5 | 5669 |           0.05 |      57 | 0          | 0.0499206  |       146929     |              78728 | 0        |
|   5 | 5669 |           0.1  |      57 | 0          | 0.100018   |       146942     |              78728 | 0        |
|   5 | 5669 |           0.2  |      57 | 0          | 0.200035   |       147079     |              78728 | 0        |

## Compact model comparison

| model                      |   D | parameter       |   tests |   hit_rate_or_recall |   coverage_or_width |   lift_or_calibration |
|:---------------------------|----:|:----------------|--------:|---------------------:|--------------------:|----------------------:|
| random_80pct_window        |   3 | p=0.8           |     157 |            0.872611  |        1610         |              1.09076  |
| random_80pct_window        |   4 | p=0.8           |     161 |            0.826087  |       16095         |              1.03261  |
| random_80pct_window        |   5 | p=0.8           |      57 |            0.666667  |      160944         |              0.833333 |
| empirical_gap_80pct_window |   3 | p=0.8           |     157 |            0.898089  |        1746.69      |              1.12261  |
| empirical_gap_80pct_window |   4 | p=0.8           |     160 |            0.8625    |       19002.9       |              1.07812  |
| empirical_gap_80pct_window |   5 | p=0.8           |      47 |            0.723404  |      295241         |              0.904255 |
| residue_K1221_top10pct     |   3 | K=1221, top=10% |     157 |            0.10828   |           0.0999181 |              1.08369  |
| residue_K1221_top10pct     |   4 | K=1221, top=10% |     161 |            0.0807453 |           0.0999181 |              0.808115 |
| residue_K1221_top10pct     |   5 | K=1221, top=10% |      57 |            0.105263  |           0.0999181 |              1.05349  |

## Interpretation

- The random/extreme-value baseline is the honest default for prediction.
- Empirical gap windows are a simple non-resonant baseline.
- The resonance-residue model would be interesting only if recall is much larger than coverage, i.e. lift > 1.
- In this backtest, the residue model is noisy and does not show robust predictive power across D and K.
- Therefore, the currently confirmed pipeline remains:

```text
predictor unknown -> matrix-sector certificate -> resonance coordinate annotation
```

rather than:

```text
resonance residues -> accurate future prediction
```

## Meaning of "when corresponding digits are computed, we certify"

The certificate step is not a prediction step.
It means: once a candidate M is proposed, or once the digits/phases around M are available, pi-fs can prove the hit by checking:

```text
[û_M - E, û_M + E] subset target sector
```

or, for decimal zero blocks via quaternary cells:

```text
floor(4^L4 * {10^M pi}) in contained_cells
```

This experiment tests the missing part: whether the candidate M can be predicted before directly scanning that region.

## Conclusion

Confirmed again:

```text
zero-block existence can be certified by the matrix-sector pipeline.
```

Not confirmed:

```text
the tested resonance-residue features predict future zero-block positions better than simple baselines.
```

Next useful step:

Try prediction of *record-low phases* instead of all zero-block hits, because long zero blocks are extreme-value events:

```text
u_M = {10^M pi} is a new low record.
```

That is closer to predicting 50 or 1000 zeros than classifying all short zero hits.
