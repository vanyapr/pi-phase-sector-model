# pi-fs experiment 001: sector index and simple resonance-residue benchmark

## Setup

- Source: first 1,000,000 base-4 fractional digits of pi generated with `mpmath`.
- Precision: 602139 decimal digits.
- First 80 base-4 digits: `02100333122220202011220300203103010301212022023200031300130310102210002103200202`
- Tested pattern lengths: [6, 7, 8]
- Resonance moduli for `log_4(pi)`: [109, 635, 3284, 15785]
- Control moduli: [113, 641, 3251, 16001]

## First-occurrence coverage

|   L_base4 |   patterns_total |   patterns_found |   coverage |   mean_first_pos_found |   median_first_pos_found |   max_first_pos_found |   seconds |
|----------:|-----------------:|-----------------:|-----------:|-----------------------:|-------------------------:|----------------------:|----------:|
|         6 |             4096 |             4096 |          1 |                4052.14 |                   2826.5 |                 34927 |  0.410359 |
|         7 |            16384 |            16384 |          1 |               16346.8  |                  11237.5 |                177627 |  0.380559 |
|         8 |            65536 |            65536 |          1 |               65741.1  |                  45480   |                702826 |  0.39787  |

## ASCII anchor examples

The target is `0_4 + text`, i.e. two binary zero bits followed by UTF-8/ASCII bytes.

| text        | target            |   bits_length |   base4_length |                                 base4_pattern |   position_base4_1indexed |   position_binary_1indexed_if_aligned | expected_random_scale_base4   |
|:------------|:------------------|--------------:|---------------:|----------------------------------------------:|--------------------------:|--------------------------------------:|:------------------------------|
| he          | 0_4 + he          |            18 |              9 |                                     012201211 |                    375057 |                                750113 | 262144                        |
| hel         | 0_4 + hel         |            26 |             13 |                                 0122012111230 |                        -1 |                                    -1 | 67108864                      |
| hell        | 0_4 + hell        |            34 |             17 |                             01220121112301230 |                        -1 |                                    -1 | 4^17                          |
| hello       | 0_4 + hello       |            42 |             21 |                         012201211123012301233 |                        -1 |                                    -1 | 4^21                          |
| hello world | 0_4 + hello world |            90 |             45 | 012201211123012301233020013131233130212301210 |                        -1 |                                    -1 | 4^45                          |

## Residue-window lift benchmark

Method:

1. For each pattern length L, find first occurrence positions m for all found base-4 strings.
2. For each modulus K, convert first positions to residues `(m-1) mod K`.
3. Split patterns into train/test.
4. Select the top f fraction of residues by train frequency.
5. Measure recall on test positions and divide by coverage f.

This tests a very simple hypothesis: whether resonance residues alone provide non-random search-window compression.

Key result for L=8:

| K_kind    |     K |   coverage |   recall_mean |   lift_mean |   lift_sd |   residue_entropy_norm |   max_bin_share |
|:----------|------:|-----------:|--------------:|------------:|----------:|-----------------------:|----------------:|
| resonance |   109 |  0.0458716 |     0.0447225 |    0.97495  | 0.0181455 |               0.999897 |     0.0100098   |
| resonance |   635 |  0.0503937 |     0.0462952 |    0.91867  | 0.0126527 |               0.999609 |     0.0019989   |
| resonance |  3284 |  0.0499391 |     0.0411296 |    0.823594 | 0.0194631 |               0.998364 |     0.000488281 |
| resonance | 15785 |  0.0499842 |     0.0309916 |    0.620029 | 0.0160607 |               0.993357 |     0.000152588 |
| control   |   113 |  0.0530973 |     0.0519541 |    0.97847  | 0.0155407 |               0.999919 |     0.00958252  |
| control   |   641 |  0.049922  |     0.0452372 |    0.906158 | 0.0194451 |               0.99964  |     0.00195312  |
| control   |  3251 |  0.0501384 |     0.0410665 |    0.819062 | 0.0162772 |               0.998428 |     0.000488281 |
| control   | 16001 |  0.0499969 |     0.0310649 |    0.621336 | 0.01329   |               0.99319  |     0.000152588 |

## Preliminary interpretation

- The finite sector index works exactly as expected: a pattern maps to a sector/cell and can be found by indexed lookup.
- The simple residue-only resonance window does **not** show strong lift in this first experiment.
- Most lift values are close to 1, similar to control moduli.
- Therefore, the current resonance layer is not yet an accelerating locate algorithm by itself.
- A stronger candidate generator must use more information than `(m-1) mod K`, likely the full chord score, drift term, or a learned/analytic phase predictor in `(q,r)` coordinates.

## Files

- `first_occurrence_summary.csv`
- `residue_window_lift_benchmark.csv`
- `ascii_anchor_locate_examples.csv`
- `lift_L8_top5pct.png`
- `resonance_lift_vs_coverage_L8.png`
- `pattern_coverage.png`


## Random baseline addendum

A random base-4 string of the same length was generated with seed `20260617`.

| dataset      |   L_base4 |   patterns_total |   patterns_found |   coverage |   mean_first_pos_found |   median_first_pos_found |   max_first_pos_found |   seconds |
|:-------------|----------:|-----------------:|-----------------:|-----------:|-----------------------:|-------------------------:|----------------------:|----------:|
| random_base4 |         8 |            65536 |            65536 |          1 |                65516.3 |                  45220.5 |                680113 |  0.409719 |

Pi-vs-random comparison for L=8, resonance moduli, top 5% residue windows:

| dataset      |     K |   coverage |   recall_mean |   lift_mean |   lift_sd |   residue_entropy_norm |   max_bin_share |
|:-------------|------:|-----------:|--------------:|------------:|----------:|-----------------------:|----------------:|
| pi_base4     |   109 |  0.0458716 |     0.0447225 |    0.97495  | 0.0181455 |               0.999897 |     0.0100098   |
| pi_base4     |   635 |  0.0503937 |     0.0462952 |    0.91867  | 0.0126527 |               0.999609 |     0.0019989   |
| pi_base4     |  3284 |  0.0499391 |     0.0411296 |    0.823594 | 0.0194631 |               0.998364 |     0.000488281 |
| pi_base4     | 15785 |  0.0499842 |     0.0309916 |    0.620029 | 0.0160607 |               0.993357 |     0.000152588 |
| random_base4 |   109 |  0.0458716 |     0.0436818 |    0.952264 | 0.0170651 |               0.999938 |     0.00979614  |
| random_base4 |   635 |  0.0503937 |     0.0458425 |    0.909687 | 0.0156807 |               0.999643 |     0.00186157  |
| random_base4 |  3284 |  0.0499391 |     0.0411407 |    0.823818 | 0.0164091 |               0.998425 |     0.000473022 |
| random_base4 | 15785 |  0.0499842 |     0.0316783 |    0.633766 | 0.0193004 |               0.993272 |     0.000167847 |

Interpretation:

- The simple residue-window heuristic behaves similarly, or slightly worse, on pi than on random data.
- No evidence of resonance-specific compression is visible in this residue-only benchmark.
- This does **not** falsify the full pi-fs idea; it falsifies only the simplest candidate generator based on residue classes modulo K.
- Next candidate generator should use chord score and continuous phase information, not only residue `(m-1) mod K`.
