#!/bin/bash

set -e

THRESHOLD=0.7
BASELINE="levenshtein"

echo "Running classical baselines..."

python src/models/levenshtein_baseline.py \
  --file "data/balanced_synonym_lepidoptera_dataset.csv" \
  --output "results/${BASELINE}/synonym_results_lepo.csv" \
  --metrics-output "results/${BASELINE}/metrics_lepo.csv" \
  --threshold "$THRESHOLD"

python src/models/levenshtein_baseline.py \
  --file "data/balanced_synonym_coleop_dataset.csv" \
  --output "results/${BASELINE}/synonym_results_coleop.csv" \
  --metrics-output "results/${BASELINE}/metrics_coleop.csv" \
  --threshold "$THRESHOLD"

echo "All baseline runs completed."