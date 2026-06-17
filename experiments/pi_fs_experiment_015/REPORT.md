# pi-fs experiment 015: next digit recovery at boundary

## Goal

Answer the direct question:

```text
Given a known index H and the last 100 known digits,
can we recover the next decimal digit by checking 10 candidates with a cross-base certificate?
```

This is a backtest inside already computed digits of pi.

## Setup

```json
{
  "experiment": "015",
  "description": "recover next decimal digit from 100-tail plus cross-base certificate",
  "source": "generated decimal pi digits with mpmath",
  "generation_seconds": 16.747454404830933,
  "cuts": [
    10000,
    50000,
    100000,
    500000,
    1000000,
    1500000
  ],
  "known_tail_len": 100,
  "certificate_bases": [
    4,
    16
  ],
  "offsets": [
    0,
    1,
    2,
    4,
    8
  ],
  "first_80_decimal_digits": "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
}
```

## Highlight: H = 1000000

```json
{
  "H": 1000000,
  "position_after_decimal": 1000001,
  "known_tail_100": "0315614033321272849194418437150696552087542450598956787961303311646283996346460422090106105779458151",
  "recovered_next_digit": "3",
  "true_next_digit": "3",
  "next_20_actual": "30927562832084531584",
  "certificate_base": 4,
  "certificate_depth": 172,
  "candidate_count_after_proportional_intersection": 1,
  "success": true
}
```

So the next digit after the first `1000000` fractional decimal digits is:

```text
3
```

and the next 20 actual digits are:

```text
30927562832084531584
```

## Recovery summary

|   Q_cert |   offset |   trials |   success_rate |   mean_candidates |   max_candidates |
|---------:|---------:|---------:|---------------:|------------------:|-----------------:|
|        4 |        0 |        6 |       0.166667 |           1.83333 |                2 |
|        4 |        1 |        6 |       0.5      |           1.5     |                2 |
|        4 |        2 |        6 |       1        |           1       |                1 |
|        4 |        4 |        6 |       1        |           1       |                1 |
|        4 |        8 |        6 |       1        |           1       |                1 |
|       16 |        0 |        6 |       0.166667 |           1.83333 |                2 |
|       16 |        1 |        6 |       1        |           1       |                1 |
|       16 |        2 |        6 |       1        |           1       |                1 |
|       16 |        4 |        6 |       1        |           1       |                1 |
|       16 |        8 |        6 |       1        |           1       |                1 |

## Canonical recoveries, Q=4, offset=4

|       H |   position_after_decimal |   known_tail_len |                                                                                       known_tail_100 |   true_next_digit |   Q_cert |   L_min |   offset |   L_cert |   decimal_digits_used_for_certificate |   q_cell_digits |   Amin_minus_prefix_low |   Amax_minus_prefix_low |   candidate_count |   recovered_digit | success   |       next_20_actual |
|--------:|-------------------------:|-----------------:|-----------------------------------------------------------------------------------------------------:|------------------:|---------:|--------:|---------:|---------:|--------------------------------------:|----------------:|------------------------:|------------------------:|------------------:|------------------:|:----------|---------------------:|
|   10000 |                    10001 |              100 | 2645600162374288021092764579310657922955249887275846101264836999892256959688159205600101655256375678 |                 5 |        4 |     168 |        4 |      172 |                                   184 |             103 |                       5 |                       5 |                 1 |                 5 | True      | 56672279661988578279 |
|   50000 |                    50001 |              100 | 1584052295369374997106655948944592462866199635563506526234053394391421112718106910522900246574236041 |                 3 |        4 |     168 |        4 |      172 |                                   184 |             103 |                       3 |                       3 |                 1 |                 3 | True      | 30093691889255865784 |
|  100000 |                   100001 |              100 | 8575016363411314627530499019135646823804329970695770150789337728658035712790913767420805655493624646 |                 4 |        4 |     168 |        4 |      172 |                                   184 |             104 |                       4 |                       4 |                 1 |                 4 | True      | 41260024379684543777 |
|  500000 |                   500001 |              100 | 5341652370316530704325828337211237137609695939937549536223222219746596193325290740424876025138195242 |                 6 |        4 |     168 |        4 |      172 |                                   184 |             104 |                       6 |                       6 |                 1 |                 6 | True      | 69739101756371975343 |
| 1000000 |                  1000001 |              100 | 0315614033321272849194418437150696552087542450598956787961303311646283996346460422090106105779458151 |                 3 |        4 |     168 |        4 |      172 |                                   184 |             103 |                       3 |                       3 |                 1 |                 3 | True      | 30927562832084531584 |
| 1500000 |                  1500001 |              100 | 1297544217105825909273186342563811411106337015947872936495004049671124794715117319607737991914462295 |                 2 |        4 |     168 |        4 |      172 |                                   184 |             103 |                       2 |                       2 |                 1 |                 2 | True      | 24435205950168142137 |

## Candidate table

|       H |   Q |   offset |   candidate_digit |   candidate_A_minus_prefix | q_certificate_decimal_range_contains_candidate   | selected_by_prefix_intersection   |   true_digit | is_true   |
|--------:|----:|---------:|------------------:|---------------------------:|:-------------------------------------------------|:----------------------------------|-------------:|:----------|
| 1000000 |   4 |        4 |                 0 |                          0 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 1 |                          1 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 2 |                          2 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 3 |                          3 | True                                             | True                              |            3 | True      |
| 1000000 |   4 |        4 |                 4 |                          4 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 5 |                          5 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 6 |                          6 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 7 |                          7 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 8 |                          8 | False                                            | False                             |            3 | False     |
| 1000000 |   4 |        4 |                 9 |                          9 | False                                            | False                             |            3 | False     |

## Interpretation

- At each boundary there are exactly 10 decimal candidates.
- The 100-digit left tail fixes the boundary alignment.
- A cross-base certificate gives a narrow sector.
- Proportional intersection of that sector with the 10 decimal candidates leaves exactly one digit.
- In this backtest the recovered digit matches the already-computed digit.

## Boundary

This still requires a certificate source. In the backtest, the cross-base
certificate is computed from already-known future digits. Beyond a world-record
horizon, the certificate must come from an independent interval/digit computation
or another verified phase source.
