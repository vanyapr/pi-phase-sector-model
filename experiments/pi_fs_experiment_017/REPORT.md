# pi-fs experiment 017: next 10 digits by candidate elimination + certificate

## Goal

Run the requested experiment:

```text
known_tail_100
-> candidates for the next 10 digits
-> external sector certificate in another base
-> proportional intersection
-> one surviving 10-digit block
```

This is a backtest inside already computed digits of pi.

## Setup

```json
{
  "experiment": "017",
  "description": "recover next 10 decimal digits at artificial boundaries from known_tail_100 plus cross-base certificate",
  "source": "generated decimal pi digits with mpmath",
  "generation_seconds": 28.493399143218994,
  "H_values": [
    100000,
    500000,
    1000000,
    2000000
  ],
  "known_n": 100,
  "hidden_k": 10,
  "cert_bases": [
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
  "guard": 90,
  "first_80_decimal_digits": "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
}
```

## Highlight: H = 2000000

```json
{
  "H_boundary": 2000000,
  "position_first_hidden_digit": 2000001,
  "known_tail_100": "9621215177020957897106655259236971933822822674913229071744735892565046166373563236871065191457297909",
  "recovered_next_10_digits": "6121731251",
  "true_next_10_digits": "6121731251",
  "next_30_actual": "612173125117978466726688273303",
  "certificate_base": 16,
  "certificate_depth": 94,
  "candidate_count_after_prefix_intersection": 1,
  "success": true
}
```

So the next 10 digits after the first `2000000` fractional decimal digits are:

```text
6121731251
```

and the next 30 actual digits are:

```text
612173125117978466726688273303
```

## Canonical recoveries

|   H_boundary |   position_first_hidden_digit |   known_tail_len |   hidden_k |                                                                                       known_tail_100 |   true_hidden |   Q_cert |   L_min |   offset |   L_cert |   decimal_digits_used_for_certificate |   q_cell_C_decimal_digit_length |   candidate_count_after_prefix_intersection |   recovered_hidden | success   |   A_min_minus_prefix_low |   A_max_minus_prefix_low |   candidate_low_minus_prefix_low |   candidate_high_minus_prefix_low |                 next_30_actual |
|-------------:|------------------------------:|-----------------:|-----------:|-----------------------------------------------------------------------------------------------------:|--------------:|---------:|--------:|---------:|---------:|--------------------------------------:|--------------------------------:|--------------------------------------------:|-------------------:|:----------|-------------------------:|-------------------------:|---------------------------------:|----------------------------------:|-------------------------------:|
|       100000 |                        100001 |              100 |         10 | 8575016363411314627530499019135646823804329970695770150789337728658035712790913767420805655493624646 |    4126002437 |       16 |      92 |        2 |       94 |                                   204 |                             114 |                                           1 |         4126002437 | True      |               4126002437 |               4126002437 |                       4126002437 |                        4126002437 | 412600243796845437773390264725 |
|       500000 |                        500001 |              100 |         10 | 5341652370316530704325828337211237137609695939937549536223222219746596193325290740424876025138195242 |    6973910175 |       16 |      92 |        2 |       94 |                                   204 |                             113 |                                           1 |         6973910175 | True      |               6973910175 |               6973910175 |                       6973910175 |                        6973910175 | 697391017563719753430044796178 |
|      1000000 |                       1000001 |              100 |         10 | 0315614033321272849194418437150696552087542450598956787961303311646283996346460422090106105779458151 |    3092756283 |       16 |      92 |        2 |       94 |                                   204 |                             112 |                                           1 |         3092756283 | True      |               3092756283 |               3092756283 |                       3092756283 |                        3092756283 | 309275628320845315846520010277 |
|      2000000 |                       2000001 |              100 |         10 | 9621215177020957897106655259236971933822822674913229071744735892565046166373563236871065191457297909 |    6121731251 |       16 |      92 |        2 |       94 |                                   204 |                             114 |                                           1 |         6121731251 | True      |               6121731251 |               6121731251 |                       6121731251 |                        6121731251 | 612173125117978466726688273303 |

## Stepwise prefix recovery for the highlighted boundary

|   step_k |   recovered_prefix_of_hidden |   true_prefix_of_hidden |   candidate_count | success   |   L_cert |
|---------:|-----------------------------:|------------------------:|------------------:|:----------|---------:|
|        1 |                            6 |                       6 |                 1 | True      |       86 |
|        2 |                           61 |                      61 |                 1 | True      |       87 |
|        3 |                          612 |                     612 |                 1 | True      |       88 |
|        4 |                         6121 |                    6121 |                 1 | True      |       89 |
|        5 |                        61217 |                   61217 |                 1 | True      |       90 |
|        6 |                       612173 |                  612173 |                 1 | True      |       91 |
|        7 |                      6121731 |                 6121731 |                 1 | True      |       91 |
|        8 |                     61217312 |                61217312 |                 1 | True      |       92 |
|        9 |                    612173125 |               612173125 |                 1 | True      |       93 |
|       10 |                   6121731251 |              6121731251 |                 1 | True      |       94 |

## Summary by certificate base/depth

|   Q_cert |   offset |   trials |   success_rate |   mean_candidates |   max_candidates |
|---------:|---------:|---------:|---------------:|------------------:|-----------------:|
|        4 |        0 |        4 |           0.25 |              1.75 |                2 |
|        4 |        1 |        4 |           0.75 |              1.25 |                2 |
|        4 |        2 |        4 |           1    |              1    |                1 |
|        4 |        4 |        4 |           1    |              1    |                1 |
|        4 |        8 |        4 |           1    |              1    |                1 |
|       16 |        0 |        4 |           0.75 |              1.25 |                2 |
|       16 |        1 |        4 |           1    |              1    |                1 |
|       16 |        2 |        4 |           1    |              1    |                1 |
|       16 |        4 |        4 |           1    |              1    |                1 |
|       16 |        8 |        4 |           1    |              1    |                1 |

## Interpretation

- Before certification, a 10-digit continuation has 10^10 candidates.
- A sufficiently deep external sector certificate collapses that set to exactly one candidate.
- The surviving candidate matches the already-computed pi digits at every tested artificial boundary.
- This validates the algebraic continuation mechanism.
- It does not compute beyond the public world-record horizon, because the external certificate for that actual boundary is not available here.
