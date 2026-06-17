# pi-fs experiment 009: quaternary resonant address read

## Goal

Correct the framing:

```text
We do not need first occurrence for this layer.
We know pi[index] once an index is supplied.
Resonant indices are exact pointers.
The question is: what do quaternary values at those pointers look like?
```

This experiment reads exact quaternary words of pi at resonant pointer addresses.

## Setup

```json
{
  "experiment": "009",
  "description": "read exact quaternary words at resonant pointer addresses",
  "H_base4_digits": 1000000,
  "word_L": 12,
  "preview_L": 24,
  "source": "generated base-4 pi digits with mpmath",
  "generation_seconds": 7.836211681365967,
  "first_80_base4_digits": "02100333122220202011220300203103010301212022023200031300130310102210002103200202",
  "periods": [
    {
      "name": "base4_res_K109",
      "K": 109,
      "kind": "base4_resonance"
    },
    {
      "name": "base4_res_K635",
      "K": 635,
      "kind": "base4_resonance"
    },
    {
      "name": "base4_res_K3284",
      "K": 3284,
      "kind": "base4_resonance"
    },
    {
      "name": "base4_res_K15785",
      "K": 15785,
      "kind": "base4_resonance"
    },
    {
      "name": "decimal_res_K1221",
      "K": 1221,
      "kind": "decimal_resonance_pointer"
    }
  ]
}
```

For each period K, we inspect positions:

```text
M = q K
```

and read:

```text
word_L(M) = floor(4^L * {4^M pi})
```

which is simply the base-4 word starting at quaternary position M.

Included periods:

- K=109, 635, 3284, 15785: base-4 resonance scales from log_4(pi);
- K=1221: the medium decimal resonance scale, used here as an external pointer period over the quaternary digit stream.

## 1. Summary statistics

| period_name       | kind                      |     K |   positions_sampled |   first_digit_freq_0 |   first_digit_freq_1 |   first_digit_freq_2 |   first_digit_freq_3 |   first_digit_entropy_bits |   first_digit_chi2_vs_uniform |   random_first_digit_chi2_vs_uniform |   unique_words_L12 |   random_unique_words_L12 |   unique_fraction |   random_unique_fraction |
|:------------------|:--------------------------|------:|--------------------:|---------------------:|---------------------:|---------------------:|---------------------:|---------------------------:|------------------------------:|-------------------------------------:|-------------------:|--------------------------:|------------------:|-------------------------:|
| base4_res_K109    | base4_resonance           |   109 |                9175 |             0.252861 |             0.244578 |             0.24436  |             0.258202 |                    1.99961 |                      5.01569  |                              1.09373 |               9172 |                      9175 |          0.999673 |                        1 |
| base4_res_K635    | base4_resonance           |   635 |                1575 |             0.251429 |             0.251429 |             0.254603 |             0.24254  |                    1.99977 |                      0.509841 |                              4.76635 |               1575 |                      1575 |          1        |                        1 |
| base4_res_K3284   | base4_resonance           |  3284 |                 305 |             0.245902 |             0.239344 |             0.255738 |             0.259016 |                    1.99929 |                      0.298361 |                             10.7377  |                305 |                       305 |          1        |                        1 |
| base4_res_K15785  | base4_resonance           | 15785 |                  64 |             0.1875   |             0.28125  |             0.34375  |             0.1875   |                    1.94992 |                      4.5      |                              2.375   |                 64 |                        64 |          1        |                        1 |
| decimal_res_K1221 | decimal_resonance_pointer |  1221 |                 819 |             0.240537 |             0.267399 |             0.241758 |             0.250305 |                    1.99869 |                      1.50794  |                              3.70574 |                819 |                       819 |          1        |                        1 |

## 2. First pointer previews

| period_name     | kind            |    K |   q |   M_base4_zero_based |   position_base4_1indexed |       word_base4_preview |   zero_prefix_len |
|:----------------|:----------------|-----:|----:|---------------------:|--------------------------:|-------------------------:|------------------:|
| base4_res_K109  | base4_resonance |  109 |   0 |                    0 |                         1 | 021003331222202020112203 |                 1 |
| base4_res_K109  | base4_resonance |  109 |   1 |                  109 |                       110 | 120323010321230202110110 |                 0 |
| base4_res_K109  | base4_resonance |  109 |   2 |                  218 |                       219 | 003131033320103111231123 |                 2 |
| base4_res_K109  | base4_resonance |  109 |   3 |                  327 |                       328 | 113023123310001223133231 |                 0 |
| base4_res_K109  | base4_resonance |  109 |   4 |                  436 |                       437 | 210112303313002000013302 |                 0 |
| base4_res_K109  | base4_resonance |  109 |   5 |                  545 |                       546 | 031211113102033130220322 |                 1 |
| base4_res_K109  | base4_resonance |  109 |   6 |                  654 |                       655 | 210222330212000103301131 |                 0 |
| base4_res_K109  | base4_resonance |  109 |   7 |                  763 |                       764 | 000321230213200322023230 |                 3 |
| base4_res_K109  | base4_resonance |  109 |   8 |                  872 |                       873 | 021133032222111122232110 |                 1 |
| base4_res_K109  | base4_resonance |  109 |   9 |                  981 |                       982 | 001322030322201111020122 |                 2 |
| base4_res_K109  | base4_resonance |  109 |  10 |                 1090 |                      1091 | 321130033201122123201321 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  11 |                 1199 |                      1200 | 012231023232122333010233 |                 1 |
| base4_res_K109  | base4_resonance |  109 |  12 |                 1308 |                      1309 | 030232332010113111313221 |                 1 |
| base4_res_K109  | base4_resonance |  109 |  13 |                 1417 |                      1418 | 233330320033310100203210 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  14 |                 1526 |                      1527 | 211230212212130030213012 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  15 |                 1635 |                      1636 | 232330023123001031322032 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  16 |                 1744 |                      1745 | 200210030032202020303232 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  17 |                 1853 |                      1854 | 303100001221010213311123 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  18 |                 1962 |                      1963 | 130210310000220102102031 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  19 |                 2071 |                      2072 | 031323313320333321100012 |                 1 |
| base4_res_K109  | base4_resonance |  109 |  20 |                 2180 |                      2181 | 113021323002012112220210 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  21 |                 2289 |                      2290 | 123030021110230303020011 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  22 |                 2398 |                      2399 | 033000302322201113101130 |                 1 |
| base4_res_K109  | base4_resonance |  109 |  23 |                 2507 |                      2508 | 030121000023013021321121 |                 1 |
| base4_res_K109  | base4_resonance |  109 |  24 |                 2616 |                      2617 | 122301110233110001323020 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  25 |                 2725 |                      2726 | 130111323233022123320302 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  26 |                 2834 |                      2835 | 301033111113031221112302 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  27 |                 2943 |                      2944 | 010223330231112300231310 |                 1 |
| base4_res_K109  | base4_resonance |  109 |  28 |                 3052 |                      3053 | 312222103023133203031202 |                 0 |
| base4_res_K109  | base4_resonance |  109 |  29 |                 3161 |                      3162 | 133231021113123312210312 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   0 |                    0 |                         1 | 021003331222202020112203 |                 1 |
| base4_res_K635  | base4_resonance |  635 |   1 |                  635 |                       636 | 123112130030031110321022 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   2 |                 1270 |                      1271 | 012221210110201330223012 |                 1 |
| base4_res_K635  | base4_resonance |  635 |   3 |                 1905 |                      1906 | 312033313130012012333323 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   4 |                 2540 |                      2541 | 333233230133220330302032 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   5 |                 3175 |                      3176 | 331221031223221002101212 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   6 |                 3810 |                      3811 | 000211003202310200130123 |                 3 |
| base4_res_K635  | base4_resonance |  635 |   7 |                 4445 |                      4446 | 203223112322212230010212 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   8 |                 5080 |                      5081 | 230333332232003033110122 |                 0 |
| base4_res_K635  | base4_resonance |  635 |   9 |                 5715 |                      5716 | 110231331203032301322323 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  10 |                 6350 |                      6351 | 030132002202313310330233 |                 1 |
| base4_res_K635  | base4_resonance |  635 |  11 |                 6985 |                      6986 | 221232112111122232311001 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  12 |                 7620 |                      7621 | 103303230131100130310201 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  13 |                 8255 |                      8256 | 033313111121300110032013 |                 1 |
| base4_res_K635  | base4_resonance |  635 |  14 |                 8890 |                      8891 | 211001312202111013321222 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  15 |                 9525 |                      9526 | 111212211203030222102211 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  16 |                10160 |                     10161 | 211123132110333112101331 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  17 |                10795 |                     10796 | 203132313210211013213001 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  18 |                11430 |                     11431 | 230212120120230131313320 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  19 |                12065 |                     12066 | 101321221323113020303203 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  20 |                12700 |                     12701 | 233231110101203221312333 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  21 |                13335 |                     13336 | 200221121200032102221011 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  22 |                13970 |                     13971 | 123130330301211311030331 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  23 |                14605 |                     14606 | 232233303301233101331022 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  24 |                15240 |                     15241 | 030113303200230102231033 |                 1 |
| base4_res_K635  | base4_resonance |  635 |  25 |                15875 |                     15876 | 020333102301133123323020 |                 1 |
| base4_res_K635  | base4_resonance |  635 |  26 |                16510 |                     16511 | 300001300312223210311232 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  27 |                17145 |                     17146 | 011023120213030130133303 |                 1 |
| base4_res_K635  | base4_resonance |  635 |  28 |                17780 |                     17781 | 200131110332102010021032 |                 0 |
| base4_res_K635  | base4_resonance |  635 |  29 |                18415 |                     18416 | 002010021300302330011023 |                 2 |
| base4_res_K3284 | base4_resonance | 3284 |   0 |                    0 |                         1 | 021003331222202020112203 |                 1 |
| base4_res_K3284 | base4_resonance | 3284 |   1 |                 3284 |                      3285 | 131121102313203333123202 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   2 |                 6568 |                      6569 | 313132332332123011222211 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   3 |                 9852 |                      9853 | 310133022330300120331001 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   4 |                13136 |                     13137 | 213033023100221020033000 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   5 |                16420 |                     16421 | 302333321032202232202031 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   6 |                19704 |                     19705 | 233200321200211303230010 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   7 |                22988 |                     22989 | 200000023212023111133202 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   8 |                26272 |                     26273 | 321030312110002332001213 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |   9 |                29556 |                     29557 | 322002231321222012221000 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  10 |                32840 |                     32841 | 302320213300231000320003 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  11 |                36124 |                     36125 | 030313323033330321331322 |                 1 |
| base4_res_K3284 | base4_resonance | 3284 |  12 |                39408 |                     39409 | 313113031112330222121220 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  13 |                42692 |                     42693 | 013221102102332303003221 |                 1 |
| base4_res_K3284 | base4_resonance | 3284 |  14 |                45976 |                     45977 | 321112022320221033302221 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  15 |                49260 |                     49261 | 123110121002032223313202 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  16 |                52544 |                     52545 | 313330022321312223130301 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  17 |                55828 |                     55829 | 313313313330121311012013 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  18 |                59112 |                     59113 | 233222010021313223303030 |                 0 |
| base4_res_K3284 | base4_resonance | 3284 |  19 |                62396 |                     62397 | 013323103132201030210233 |                 1 |

## 3. Zero-prefix rates

| period_name       |     K |   zero_prefix_length_at_least |   resonant_count |   resonant_rate |   random_count |   random_rate |   expected_rate |
|:------------------|------:|------------------------------:|-----------------:|----------------:|---------------:|--------------:|----------------:|
| base4_res_K109    |   109 |                             1 |             2320 |     0.252861    |           2266 |   0.246975    |     0.25        |
| base4_res_K109    |   109 |                             2 |              609 |     0.066376    |            554 |   0.0603815   |     0.0625      |
| base4_res_K109    |   109 |                             3 |              155 |     0.0168937   |            149 |   0.0162398   |     0.015625    |
| base4_res_K109    |   109 |                             4 |               36 |     0.00392371  |             30 |   0.00326975  |     0.00390625  |
| base4_res_K109    |   109 |                             5 |                5 |     0.000544959 |              9 |   0.000980926 |     0.000976562 |
| base4_res_K109    |   109 |                             6 |                2 |     0.000217984 |              3 |   0.000326975 |     0.000244141 |
| base4_res_K635    |   635 |                             1 |              396 |     0.251429    |            370 |   0.234921    |     0.25        |
| base4_res_K635    |   635 |                             2 |               85 |     0.0539683   |             89 |   0.0565079   |     0.0625      |
| base4_res_K635    |   635 |                             3 |               18 |     0.0114286   |             24 |   0.0152381   |     0.015625    |
| base4_res_K635    |   635 |                             4 |                7 |     0.00444444  |              5 |   0.0031746   |     0.00390625  |
| base4_res_K635    |   635 |                             5 |                3 |     0.00190476  |              0 |   0           |     0.000976562 |
| base4_res_K635    |   635 |                             6 |                1 |     0.000634921 |              0 |   0           |     0.000244141 |
| base4_res_K3284   |  3284 |                             1 |               75 |     0.245902    |             80 |   0.262295    |     0.25        |
| base4_res_K3284   |  3284 |                             2 |               15 |     0.0491803   |             21 |   0.0688525   |     0.0625      |
| base4_res_K3284   |  3284 |                             3 |                3 |     0.00983607  |              8 |   0.0262295   |     0.015625    |
| base4_res_K3284   |  3284 |                             4 |                0 |     0           |              0 |   0           |     0.00390625  |
| base4_res_K3284   |  3284 |                             5 |                0 |     0           |              0 |   0           |     0.000976562 |
| base4_res_K3284   |  3284 |                             6 |                0 |     0           |              0 |   0           |     0.000244141 |
| base4_res_K15785  | 15785 |                             1 |               12 |     0.1875      |             21 |   0.328125    |     0.25        |
| base4_res_K15785  | 15785 |                             2 |                2 |     0.03125     |              2 |   0.03125     |     0.0625      |
| base4_res_K15785  | 15785 |                             3 |                2 |     0.03125     |              2 |   0.03125     |     0.015625    |
| base4_res_K15785  | 15785 |                             4 |                0 |     0           |              1 |   0.015625    |     0.00390625  |
| base4_res_K15785  | 15785 |                             5 |                0 |     0           |              0 |   0           |     0.000976562 |
| base4_res_K15785  | 15785 |                             6 |                0 |     0           |              0 |   0           |     0.000244141 |
| decimal_res_K1221 |  1221 |                             1 |              197 |     0.240537    |            182 |   0.222222    |     0.25        |
| decimal_res_K1221 |  1221 |                             2 |               44 |     0.0537241   |             39 |   0.047619    |     0.0625      |
| decimal_res_K1221 |  1221 |                             3 |               12 |     0.014652    |             12 |   0.014652    |     0.015625    |
| decimal_res_K1221 |  1221 |                             4 |                4 |     0.004884    |              2 |   0.002442    |     0.00390625  |
| decimal_res_K1221 |  1221 |                             5 |                1 |     0.001221    |              0 |   0           |     0.000976562 |
| decimal_res_K1221 |  1221 |                             6 |                0 |     0           |              0 |   0           |     0.000244141 |

## Interpretation

- The quaternary read formula is exact: an address M gives a word immediately inside the computed horizon.
- Resonant K values are valid pointer grids.
- In these first simple statistics, the words at resonant pointer positions look close to random quaternary samples.
- Zero-prefix rates are close to the expected 4^-z baseline.
- Therefore, the current evidence says: resonant pointer grids are useful as address systems, but simple K-step sampling does not by itself reveal a visible deterministic pattern.

## Important distinction

There are two translations:

1. **Value/sector translation**: a quaternary sector can be mapped to a decimal sector by overlap/containment matrices.
2. **Dynamic/index translation**: quaternary digit positions use {4^M pi}, decimal digit positions use {10^M pi}.

These are not the same orbit. A quaternary pointer can certify a decimal sector only when the phase dynamics and sector grid are chosen consistently, e.g. B=10, Q=4 for decimal-phase certification.

## Next useful step

Do not ask "first occurrence" yet. Build a `read` surface:

```text
read_base4(M, L) -> exact quaternary word
read_decimal_phase_quaternary_cell(M, L4) -> certifying cell for decimal targets
resonance_address(M, K) -> (q,r)
```

Then study deterministic maps between these surfaces, not just distributional statistics.
