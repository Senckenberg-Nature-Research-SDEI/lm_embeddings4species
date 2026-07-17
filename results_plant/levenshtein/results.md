# Plant Levenshtein Baseline Metrics

| Model | Dataset | Threshold | Accuracy | Precision | Recall | F1 | TN | FP | FN | TP | Total |
|---------|---------|----------:|---------:|----------:|-------:|---:|---:|---:|----:|---:|------:|
| Levenshtein | fabales | 0.7 | 0.5681 | 0.9874 | 0.1380 | 0.2422 | 5684 | 10 | 4908 | 786 | 11388 |
| Levenshtein | lamiales | 0.7 | 0.5793 | 0.9535 | 0.1667 | 0.2837 | 244 | 2 | 205 | 41 | 492 |
| Levenshtein | poales | 0.7 | 0.5692 | 0.9973 | 0.1388 | 0.2437 | 13127 | 5 | 11309 | 1823 | 26264 |
| Levenshtein | rosales | 0.7 | 0.5698 | 0.9977 | 0.1398 | 0.2453 | 9415 | 3 | 8101 | 1317 | 18836 |
| **Levenshtein** | **overall** | **0.7** | **0.5693** | **0.9950** | **0.1392** | **0.2443** | **28470** | **20** | **24523** | **3967** | **56980** |

## Notes

- The `overall` row is computed by summing confusion-matrix counts across fabales, lamiales, poales, and rosales, then recomputing Accuracy, Precision, Recall, and F1 from those totals.