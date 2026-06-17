# pi-fs experiment 012: 100-digit boundary-tail anchor

## Goal

Test the idea:

```text
Take the last 100 known digits before a boundary H.
Use them as an almost unique anchor.
Then reason about H+1 with 10 candidate digits.
```

This simulates the current world-record boundary without requiring the actual last 100 record digits.

## Setup

```json
{
  "experiment": "012",
  "description": "100-digit boundary tail anchor uniqueness and +1 candidate set",
  "source": "generated decimal pi digits with mpmath",
  "generation_seconds": 28.145358324050903,
  "H_MAX": 2000000,
  "tail_lengths": [
    20,
    50,
    100
  ],
  "cuts": [
    10000,
    50000,
    100000,
    500000,
    1000000,
    2000000
  ],
  "first_80_decimal_digits": "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
}
```

## 1. Boundary-tail uniqueness

For each artificial horizon H, the last L digits before the boundary are:

```text
tail = pi[H-L : H]
```

We search the computed prefix `pi[0:H]` for that exact tail.

|   horizon_H_digits |   tail_length_L |   tail_start_M_zero_based |   tail_position_1based |                                                                                                 tail |   occurrences_in_prefix |   earlier_occurrences_excluding_boundary | is_unique_anchor_in_prefix   | first_earlier_occurrence_M   |   expected_false_matches_random |   expected_false_matches_log10 |   negative_context_len | negative_context_verified   |
|-------------------:|----------------:|--------------------------:|-----------------------:|-----------------------------------------------------------------------------------------------------:|------------------------:|-----------------------------------------:|:-----------------------------|:-----------------------------|--------------------------------:|-------------------------------:|-----------------------:|:----------------------------|
|              10000 |              20 |                      9980 |                   9981 |                                                                                 05600101655256375678 |                       1 |                                        0 | True                         |                              |                     9.98e-17    |                       -16.0009 |                     32 | True                        |
|              10000 |              50 |                      9950 |                   9951 |                                                   46101264836999892256959688159205600101655256375678 |                       1 |                                        0 | True                         |                              |                     9.95e-47    |                       -46.0022 |                     32 | True                        |
|              10000 |             100 |                      9900 |                   9901 | 2645600162374288021092764579310657922955249887275846101264836999892256959688159205600101655256375678 |                       1 |                                        0 | True                         |                              |                     9.9e-97     |                       -96.0044 |                     32 | True                        |
|              50000 |              20 |                     49980 |                  49981 |                                                                                 10522900246574236041 |                       1 |                                        0 | True                         |                              |                     4.998e-16   |                       -15.3012 |                     32 | True                        |
|              50000 |              50 |                     49950 |                  49951 |                                                   06526234053394391421112718106910522900246574236041 |                       1 |                                        0 | True                         |                              |                     4.995e-46   |                       -45.3015 |                     32 | True                        |
|              50000 |             100 |                     49900 |                  49901 | 1584052295369374997106655948944592462866199635563506526234053394391421112718106910522900246574236041 |                       1 |                                        0 | True                         |                              |                     4.99e-96    |                       -95.3019 |                     32 | True                        |
|             100000 |              20 |                     99980 |                  99981 |                                                                                 67420805655493624646 |                       1 |                                        0 | True                         |                              |                     9.998e-16   |                       -15.0001 |                     32 | True                        |
|             100000 |              50 |                     99950 |                  99951 |                                                   70150789337728658035712790913767420805655493624646 |                       1 |                                        0 | True                         |                              |                     9.995e-46   |                       -45.0002 |                     32 | True                        |
|             100000 |             100 |                     99900 |                  99901 | 8575016363411314627530499019135646823804329970695770150789337728658035712790913767420805655493624646 |                       1 |                                        0 | True                         |                              |                     9.99e-96    |                       -95.0004 |                     32 | True                        |
|             500000 |              20 |                    499980 |                 499981 |                                                                                 40424876025138195242 |                       1 |                                        0 | True                         |                              |                     4.9998e-15  |                       -14.301  |                     32 | True                        |
|             500000 |              50 |                    499950 |                 499951 |                                                   49536223222219746596193325290740424876025138195242 |                       1 |                                        0 | True                         |                              |                     4.9995e-45  |                       -44.3011 |                     32 | True                        |
|             500000 |             100 |                    499900 |                 499901 | 5341652370316530704325828337211237137609695939937549536223222219746596193325290740424876025138195242 |                       1 |                                        0 | True                         |                              |                     4.999e-95   |                       -94.3011 |                     32 | True                        |
|            1000000 |              20 |                    999980 |                 999981 |                                                                                 22090106105779458151 |                       1 |                                        0 | True                         |                              |                     9.9998e-15  |                       -14      |                     32 | True                        |
|            1000000 |              50 |                    999950 |                 999951 |                                                   56787961303311646283996346460422090106105779458151 |                       1 |                                        0 | True                         |                              |                     9.9995e-45  |                       -44      |                     32 | True                        |
|            1000000 |             100 |                    999900 |                 999901 | 0315614033321272849194418437150696552087542450598956787961303311646283996346460422090106105779458151 |                       1 |                                        0 | True                         |                              |                     9.999e-95   |                       -94      |                     32 | True                        |
|            2000000 |              20 |                   1999980 |                1999981 |                                                                                 36871065191457297909 |                       1 |                                        0 | True                         |                              |                     1.99998e-14 |                       -13.699  |                     32 | True                        |
|            2000000 |              50 |                   1999950 |                1999951 |                                                   29071744735892565046166373563236871065191457297909 |                       1 |                                        0 | True                         |                              |                     1.99995e-44 |                       -43.699  |                     32 | True                        |
|            2000000 |             100 |                   1999900 |                1999901 | 9621215177020957897106655259236971933822822674913229071744735892565046166373563236871065191457297909 |                       1 |                                        0 | True                         |                              |                     1.9999e-94  |                       -93.699  |                     32 | True                        |

## 2. Negative context reads

For each boundary-tail anchor, we also read the 32 digits immediately before the tail.

|   horizon_H_digits |   tail_length_L |   tail_start_M_zero_based |                 negative_context |                                                                                                 tail |                                                                                                              combined_left_plus_tail |
|-------------------:|----------------:|--------------------------:|---------------------------------:|-----------------------------------------------------------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------:|
|              10000 |              20 |                      9980 | 58461012648369998922569596881592 |                                                                                 05600101655256375678 |                                                                                 5846101264836999892256959688159205600101655256375678 |
|              10000 |              50 |                      9950 | 10927645793106579229552498872758 |                                                   46101264836999892256959688159205600101655256375678 |                                                   1092764579310657922955249887275846101264836999892256959688159205600101655256375678 |
|              10000 |             100 |                      9900 | 53539459094407046912091409387001 | 2645600162374288021092764579310657922955249887275846101264836999892256959688159205600101655256375678 | 535394590944070469120914093870012645600162374288021092764579310657922955249887275846101264836999892256959688159205600101655256375678 |
|              50000 |              20 |                     49980 | 35065262340533943914211127181069 |                                                                                 10522900246574236041 |                                                                                 3506526234053394391421112718106910522900246574236041 |
|              50000 |              50 |                     49950 | 71066559489445924628661996355635 |                                                   06526234053394391421112718106910522900246574236041 |                                                   7106655948944592462866199635563506526234053394391421112718106910522900246574236041 |
|              50000 |             100 |                     49900 | 27626392344107146584895780241408 | 1584052295369374997106655948944592462866199635563506526234053394391421112718106910522900246574236041 | 276263923441071465848957802414081584052295369374997106655948944592462866199635563506526234053394391421112718106910522900246574236041 |
|             100000 |              20 |                     99980 | 57701507893377286580357127909137 |                                                                                 67420805655493624646 |                                                                                 5770150789337728658035712790913767420805655493624646 |
|             100000 |              50 |                     99950 | 75304990191356468238043299706957 |                                                   70150789337728658035712790913767420805655493624646 |                                                   7530499019135646823804329970695770150789337728658035712790913767420805655493624646 |
|             100000 |             100 |                     99900 | 17119687348468873818665675127929 | 8575016363411314627530499019135646823804329970695770150789337728658035712790913767420805655493624646 | 171196873484688738186656751279298575016363411314627530499019135646823804329970695770150789337728658035712790913767420805655493624646 |
|             500000 |              20 |                    499980 | 75495362232222197465961933252907 |                                                                                 40424876025138195242 |                                                                                 7549536223222219746596193325290740424876025138195242 |
|             500000 |              50 |                    499950 | 43258283372112371376096959399375 |                                                   49536223222219746596193325290740424876025138195242 |                                                   4325828337211237137609695939937549536223222219746596193325290740424876025138195242 |
|             500000 |             100 |                    499900 | 28268267484421213715468232751128 | 5341652370316530704325828337211237137609695939937549536223222219746596193325290740424876025138195242 | 282682674844212137154682327511285341652370316530704325828337211237137609695939937549536223222219746596193325290740424876025138195242 |
|            1000000 |              20 |                    999980 | 89567879613033116462839963464604 |                                                                                 22090106105779458151 |                                                                                 8956787961303311646283996346460422090106105779458151 |
|            1000000 |              50 |                    999950 | 91944184371506965520875424505989 |                                                   56787961303311646283996346460422090106105779458151 |                                                   9194418437150696552087542450598956787961303311646283996346460422090106105779458151 |
|            1000000 |             100 |                    999900 | 37471732470336976335792589151526 | 0315614033321272849194418437150696552087542450598956787961303311646283996346460422090106105779458151 | 374717324703369763357925891515260315614033321272849194418437150696552087542450598956787961303311646283996346460422090106105779458151 |
|            2000000 |              20 |                   1999980 | 32290717447358925650461663735632 |                                                                                 36871065191457297909 |                                                                                 3229071744735892565046166373563236871065191457297909 |
|            2000000 |              50 |                   1999950 | 71066552592369719338228226749132 |                                                   29071744735892565046166373563236871065191457297909 |                                                   7106655259236971933822822674913229071744735892565046166373563236871065191457297909 |
|            2000000 |             100 |                   1999900 | 75865593128739602791251059654044 | 9621215177020957897106655259236971933822822674913229071744735892565046166373563236871065191457297909 | 758655931287396027912510596540449621215177020957897106655259236971933822822674913229071744735892565046166373563236871065191457297909 |

## 3. Ten candidates for H+1

All 10 candidates share the same 100-digit left tail. The tail anchor verifies alignment, but it does not choose the next digit by itself.

|   horizon_H_digits |   tail_length |   candidate_digit | tail_anchor_matches   |     candidate_string |   true_next_digit | is_true_continuation   | note                                                                                        |
|-------------------:|--------------:|------------------:|:----------------------|---------------------:|------------------:|:-----------------------|:--------------------------------------------------------------------------------------------|
|              10000 |           100 |                 0 | True                  | 56001016552563756780 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 1 | True                  | 56001016552563756781 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 2 | True                  | 56001016552563756782 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 3 | True                  | 56001016552563756783 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 4 | True                  | 56001016552563756784 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 5 | True                  | 56001016552563756785 |                 5 | True                   | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 6 | True                  | 56001016552563756786 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 7 | True                  | 56001016552563756787 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 8 | True                  | 56001016552563756788 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              10000 |           100 |                 9 | True                  | 56001016552563756789 |                 5 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 0 | True                  | 05229002465742360410 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 1 | True                  | 05229002465742360411 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 2 | True                  | 05229002465742360412 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 3 | True                  | 05229002465742360413 |                 3 | True                   | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 4 | True                  | 05229002465742360414 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 5 | True                  | 05229002465742360415 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 6 | True                  | 05229002465742360416 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 7 | True                  | 05229002465742360417 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 8 | True                  | 05229002465742360418 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|              50000 |           100 |                 9 | True                  | 05229002465742360419 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 0 | True                  | 74208056554936246460 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 1 | True                  | 74208056554936246461 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 2 | True                  | 74208056554936246462 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 3 | True                  | 74208056554936246463 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 4 | True                  | 74208056554936246464 |                 4 | True                   | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 5 | True                  | 74208056554936246465 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 6 | True                  | 74208056554936246466 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 7 | True                  | 74208056554936246467 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 8 | True                  | 74208056554936246468 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             100000 |           100 |                 9 | True                  | 74208056554936246469 |                 4 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 0 | True                  | 04248760251381952420 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 1 | True                  | 04248760251381952421 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 2 | True                  | 04248760251381952422 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 3 | True                  | 04248760251381952423 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 4 | True                  | 04248760251381952424 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 5 | True                  | 04248760251381952425 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 6 | True                  | 04248760251381952426 |                 6 | True                   | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 7 | True                  | 04248760251381952427 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 8 | True                  | 04248760251381952428 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|             500000 |           100 |                 9 | True                  | 04248760251381952429 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 0 | True                  | 20901061057794581510 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 1 | True                  | 20901061057794581511 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 2 | True                  | 20901061057794581512 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 3 | True                  | 20901061057794581513 |                 3 | True                   | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 4 | True                  | 20901061057794581514 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 5 | True                  | 20901061057794581515 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 6 | True                  | 20901061057794581516 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 7 | True                  | 20901061057794581517 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 8 | True                  | 20901061057794581518 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            1000000 |           100 |                 9 | True                  | 20901061057794581519 |                 3 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 0 | True                  | 68710651914572979090 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 1 | True                  | 68710651914572979091 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 2 | True                  | 68710651914572979092 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 3 | True                  | 68710651914572979093 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 4 | True                  | 68710651914572979094 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 5 | True                  | 68710651914572979095 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 6 | True                  | 68710651914572979096 |                 6 | True                   | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 7 | True                  | 68710651914572979097 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 8 | True                  | 68710651914572979098 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |
|            2000000 |           100 |                 9 | True                  | 68710651914572979099 |                 6 | False                  | tail anchor verifies boundary alignment; independent interval/next-digit data selects digit |

## Interpretation

- A 100-digit tail is unique inside every tested horizon up to 2,000,000 digits.
- The random expected number of false matches is approximately H * 10^-100, effectively zero for any real-world digit horizon.
- Therefore, the last 100 digits of a known computation make an excellent boundary anchor.
- From that anchor, negative indexing is strict and cheap.
- For H+1, there are exactly 10 candidate continuations.
- The 100-digit tail verifies boundary alignment for all 10 candidates.
- Choosing the correct candidate still requires independent information: an interval refinement, a digit computation, or a sector certificate at H+1.

## Consequence for pi-fs

Boundary continuation should be modeled as:

```text
known_tail_100 -> unique boundary anchor
candidate digit d in 0..9
negative-context alignment certificate
independent next-digit/phase certificate
```

The anchor part is O(100), which is O(log H) for any realistic H. The candidate set is constant size 10.
