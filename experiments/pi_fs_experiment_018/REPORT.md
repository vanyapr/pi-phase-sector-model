# pi-fs experiment 018: next 10 digits beyond an artificial known boundary

## Goal

Test the real continuation contour in a feasible setting:

```text
known decimal tail
-> unknown next 10 digits
-> external certificate not derived from the known tail
-> proportional selection
```

The external certificate is produced from the Machin formula:

```text
pi = 16 atan(1/5) - 4 atan(1/239)
```

The ground truth for verification is `mp.pi`.

## Setup

```json
{
  "experiment": "018",
  "description": "recover next 10 digits beyond artificial known boundary using independent Machin-formula certificate",
  "H_values": [
    10000,
    50000,
    100000
  ],
  "known_tail_len": 100,
  "hidden_k": 10,
  "cert_base": 16,
  "cert_offset": 2,
  "guard": 80,
  "need_digits": 100310,
  "ground_truth_source": "mp.pi",
  "external_certificate_source": "Machin formula 16 atan(1/5) - 4 atan(1/239)",
  "ground_truth_seconds": 0.04940295219421387,
  "machin_seconds": 10.860318899154663,
  "machin_mp_pi_agreement_prefix_digits": 100310,
  "first_80_ground_truth_decimal_digits": "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
}
```

## Results

|   H_boundary |                                                                                       known_tail_100 | external_certificate_source                  |   cert_base |   cert_depth |   cert_offset |   decimal_digits_used_for_Q_cell |   candidate_count_after_intersection |   recovered_next_10 |   true_next_10 |                   next_30_true | success   |   A_min_minus_prefix_low |   A_max_minus_prefix_low |   candidate_low_minus_prefix_low |   candidate_high_minus_prefix_low |
|-------------:|-----------------------------------------------------------------------------------------------------:|:---------------------------------------------|------------:|-------------:|--------------:|---------------------------------:|-------------------------------------:|--------------------:|---------------:|-------------------------------:|:----------|-------------------------:|-------------------------:|---------------------------------:|----------------------------------:|
|        10000 | 2645600162374288021092764579310657922955249887275846101264836999892256959688159205600101655256375678 | Machin formula: 16 atan(1/5) - 4 atan(1/239) |          16 |           94 |             2 |                              194 |                                    1 |          5667227966 |     5667227966 | 566722796619885782794848855834 | True      |               5667227966 |               5667227966 |                       5667227966 |                        5667227966 |
|        50000 | 1584052295369374997106655948944592462866199635563506526234053394391421112718106910522900246574236041 | Machin formula: 16 atan(1/5) - 4 atan(1/239) |          16 |           94 |             2 |                              194 |                                    1 |          3009369188 |     3009369188 | 300936918892558657846684612156 | True      |               3009369188 |               3009369188 |                       3009369188 |                        3009369188 |
|       100000 | 8575016363411314627530499019135646823804329970695770150789337728658035712790913767420805655493624646 | Machin formula: 16 atan(1/5) - 4 atan(1/239) |          16 |           94 |             2 |                              194 |                                    1 |          4126002437 |     4126002437 | 412600243796845437773390264725 | True      |               4126002437 |               4126002437 |                       4126002437 |                        4126002437 |

## Negative control

|   H_boundary |   known_tail_only_candidates_for_next10 |   with_external_certificate_candidates |
|-------------:|----------------------------------------:|---------------------------------------:|
|        10000 |                                   1e+10 |                                      1 |
|        50000 |                                   1e+10 |                                      1 |
|       100000 |                                   1e+10 |                                      1 |

## Interpretation

- If we know only the last 100 digits before H, the next 10 digits have `10^10` candidates.
- The external Machin certificate gives a sector in base 16 for the same local phase.
- Proportional intersection with the known 100-digit tail leaves exactly one 10-digit block.
- The recovered block matches the ground truth at every tested artificial boundary.

## Boundary

This demonstrates the mechanism beyond an artificial known boundary. It does not compute after the actual public world-record horizon, because that would require computing the corresponding external certificate at the world-record scale.
