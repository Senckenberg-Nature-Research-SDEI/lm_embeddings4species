#!/bin/bash

set -e

# THRESHOLD=0.7
# BASELINE="levenshtein"

# echo "Running classical baselines..."

# python src/models/levenshtein_baseline.py \
#   --file "data/balanced_synonym_lepidoptera_dataset.csv" \
#   --output "results/${BASELINE}/synonym_results_lepo.csv" \
#   --metrics-output "results/${BASELINE}/metrics_lepo.csv" \
#   --threshold "$THRESHOLD"

# python src/models/levenshtein_baseline.py \
#   --file "data/balanced_synonym_coleop_dataset.csv" \
#   --output "results/${BASELINE}/synonym_results_coleop.csv" \
#   --metrics-output "results/${BASELINE}/metrics_coleop.csv" \
#   --threshold "$THRESHOLD"

# echo "All baseline runs completed."


THRESHOLD=0.7
BASELINE="levenshtein"

echo "Running classical baselines..."

python src/models/levenshtein_baseline.py \
  --file "gbif_dataset/balanced_synonym_fabales_dataset.csv" \
  --output "results_plant/${BASELINE}/synonym_results_fabales.csv" \
  --metrics-output "results_plant/${BASELINE}/metrics_fabales.csv" \
  --threshold "$THRESHOLD"

python src/models/levenshtein_baseline.py \
  --file "gbif_dataset/balanced_synonym_lamiales_dataset.csv" \
  --output "results_plant/${BASELINE}/synonym_results_lamiales.csv" \
  --metrics-output "results_plant/${BASELINE}/metrics_lamiales.csv" \
  --threshold "$THRESHOLD"

python src/models/levenshtein_baseline.py \
  --file "gbif_dataset/balanced_synonym_poales_dataset.csv" \
  --output "results_plant/${BASELINE}/synonym_results_poales.csv" \
  --metrics-output "results_plant/${BASELINE}/metrics_poales.csv" \
  --threshold "$THRESHOLD"


python src/models/levenshtein_baseline.py \
  --file "gbif_dataset/balanced_synonym_rosales_dataset.csv" \
  --output "results_plant/${BASELINE}/synonym_results_rosales.csv" \
  --metrics-output "results_plant/${BASELINE}/metrics_rosales.csv" \
  --threshold "$THRESHOLD"

echo "All baseline runs completed."