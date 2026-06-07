# GPT-2
python src/models/mlp_decoder.py \
  --model-name "gpt2" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/gpt2/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp_decoder.py \
  --model-name "gpt2" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/gpt2/synonym_results_coleop.csv" \
  --threshold 0.70


# GPT-2 Medium
python src/models/mlp_decoder.py \
  --model-name "gpt2-medium" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/gpt2-medium/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp_decoder.py \
  --model-name "gpt2-medium" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/gpt2-medium/synonym_results_coleop.csv" \
  --threshold 0.70


# TinyLlama
python src/models/mlp_decoder.py \
  --model-name "TinyLlama/TinyLlama-1.1B-Chat-v1.0" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/TinyLlama-1.1B-Chat-v1.0/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp_decoder.py \
  --model-name "TinyLlama/TinyLlama-1.1B-Chat-v1.0" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/TinyLlama-1.1B-Chat-v1.0/synonym_results_coleop.csv" \
  --threshold 0.70


# Qwen 0.5B
python src/models/mlp_decoder.py \
  --model-name "Qwen/Qwen2.5-0.5B" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/Qwen2.5-0.5B/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp_decoder.py \
  --model-name "Qwen/Qwen2.5-0.5B" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/Qwen2.5-0.5B/synonym_results_coleop.csv" \
  --threshold 0.70