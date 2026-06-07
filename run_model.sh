python src/models/mlp.py \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/scibert_scivocab_uncased/synonym_results_lepo.csv" \
  --threshold 0.70
python src/models/mlp.py \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/scibert_scivocab_uncased/synonym_results_coleop.csv" \
  --threshold 0.70