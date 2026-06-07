# GPT-2
python src/models/mlp_decoder.py --model-name "gpt2" --file "data/only_synonyms_lepo.csv" --output "results/gpt2/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "gpt2" --file "data/only_synonyms_coleop.csv" --output "results/gpt2/synonym_results_coleop.csv" --threshold 0.70

# GPT-2 Medium
python src/models/mlp_decoder.py --model-name "gpt2-medium" --file "data/only_synonyms_lepo.csv" --output "results/gpt2-medium/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "gpt2-medium" --file "data/only_synonyms_coleop.csv" --output "results/gpt2-medium/synonym_results_coleop.csv" --threshold 0.70

# TinyLlama
python src/models/mlp_decoder.py --model-name "TinyLlama/TinyLlama-1.1B-Chat-v1.0" --file "data/only_synonyms_lepo.csv" --output "results/TinyLlama-1.1B-Chat-v1.0/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "TinyLlama/TinyLlama-1.1B-Chat-v1.0" --file "data/only_synonyms_coleop.csv" --output "results/TinyLlama-1.1B-Chat-v1.0/synonym_results_coleop.csv" --threshold 0.70

# Qwen 0.5B
python src/models/mlp_decoder.py --model-name "Qwen/Qwen2.5-0.5B" --file "data/only_synonyms_lepo.csv" --output "results/Qwen2.5-0.5B/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "Qwen/Qwen2.5-0.5B" --file "data/only_synonyms_coleop.csv" --output "results/Qwen2.5-0.5B/synonym_results_coleop.csv" --threshold 0.70

# Qwen 1.5B
python src/models/mlp_decoder.py --model-name "Qwen/Qwen2.5-1.5B" --file "data/only_synonyms_lepo.csv" --output "results/Qwen2.5-1.5B/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "Qwen/Qwen2.5-1.5B" --file "data/only_synonyms_coleop.csv" --output "results/Qwen2.5-1.5B/synonym_results_coleop.csv" --threshold 0.70

# SmolLM2 360M
python src/models/mlp_decoder.py --model-name "HuggingFaceTB/SmolLM2-360M" --file "data/only_synonyms_lepo.csv" --output "results/SmolLM2-360M/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "HuggingFaceTB/SmolLM2-360M" --file "data/only_synonyms_coleop.csv" --output "results/SmolLM2-360M/synonym_results_coleop.csv" --threshold 0.70

# SmolLM2 1.7B
python src/models/mlp_decoder.py --model-name "HuggingFaceTB/SmolLM2-1.7B" --file "data/only_synonyms_lepo.csv" --output "results/SmolLM2-1.7B/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "HuggingFaceTB/SmolLM2-1.7B" --file "data/only_synonyms_coleop.csv" --output "results/SmolLM2-1.7B/synonym_results_coleop.csv" --threshold 0.70

# Phi-2
python src/models/mlp_decoder.py --model-name "microsoft/phi-2" --file "data/only_synonyms_lepo.csv" --output "results/phi-2/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "microsoft/phi-2" --file "data/only_synonyms_coleop.csv" --output "results/phi-2/synonym_results_coleop.csv" --threshold 0.70

# OLMo 1B
python src/models/mlp_decoder.py --model-name "allenai/OLMo-1B-hf" --file "data/only_synonyms_lepo.csv" --output "results/OLMo-1B-hf/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "allenai/OLMo-1B-hf" --file "data/only_synonyms_coleop.csv" --output "results/OLMo-1B-hf/synonym_results_coleop.csv" --threshold 0.70

# Mistral 7B
python src/models/mlp_decoder.py --model-name "mistralai/Mistral-7B-v0.1" --file "data/only_synonyms_lepo.csv" --output "results/Mistral-7B-v0.1/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "mistralai/Mistral-7B-v0.1" --file "data/only_synonyms_coleop.csv" --output "results/Mistral-7B-v0.1/synonym_results_coleop.csv" --threshold 0.70

# Llama 3.2 1B
python src/models/mlp_decoder.py --model-name "meta-llama/Llama-3.2-1B" --file "data/only_synonyms_lepo.csv" --output "results/Llama-3.2-1B/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "meta-llama/Llama-3.2-1B" --file "data/only_synonyms_coleop.csv" --output "results/Llama-3.2-1B/synonym_results_coleop.csv" --threshold 0.70

# Llama 3.2 3B
python src/models/mlp_decoder.py --model-name "meta-llama/Llama-3.2-3B" --file "data/only_synonyms_lepo.csv" --output "results/Llama-3.2-3B/synonym_results_lepo.csv" --threshold 0.70
python src/models/mlp_decoder.py --model-name "meta-llama/Llama-3.2-3B" --file "data/only_synonyms_coleop.csv" --output "results/Llama-3.2-3B/synonym_results_coleop.csv" --threshold 0.70