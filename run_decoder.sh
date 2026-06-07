# GPT-2
python src/models/mlp_decoder.py --model-name "gpt2" --file "data/balanced_synonym_lepidoptera_dataset.csv" --output "results/gpt2/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "gpt2" --file "data/balanced_synonym_coleop_dataset.csv" --output "results/gpt2/synonym_results_coleop.csv" --threshold 0.70

# GPT-2 Medium
python src/models/mlp_decoder.py --model-name "gpt2-medium" --file "data/balanced_synonym_lepidoptera_dataset.csv" --output "results/gpt2-medium/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "gpt2-medium" --file "data/balanced_synonym_coleop_dataset.csv" --output "results/gpt2-medium/synonym_results_coleop.csv" --threshold 0.70

