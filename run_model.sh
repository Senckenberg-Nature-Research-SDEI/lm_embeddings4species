# SciBERT (uncased)
python src/models/mlp.py \
  --model-name "allenai/scibert_scivocab_uncased" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/scibert_scivocab_uncased/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "allenai/scibert_scivocab_uncased" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/scibert_scivocab_uncased/synonym_results_coleop.csv" \
  --threshold 0.70


# SciBERT (cased)
python src/models/mlp.py \
  --model-name "allenai/scibert_scivocab_cased" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/scibert_scivocab_cased/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "allenai/scibert_scivocab_cased" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/scibert_scivocab_cased/synonym_results_coleop.csv" \
  --threshold 0.70


# BiomedBERT
python src/models/mlp.py \
  --model-name "microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/BiomedBERT/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/BiomedBERT/synonym_results_coleop.csv" \
  --threshold 0.70


# S-BioBERT
python src/models/mlp.py \
  --model-name "pritamdeka/S-BioBERT-snli-multinli-stsb" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/S-BioBERT/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "pritamdeka/S-BioBERT-snli-multinli-stsb" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/S-BioBERT/synonym_results_coleop.csv" \
  --threshold 0.70


# all-MiniLM-L6-v2
python src/models/mlp.py \
  --model-name "sentence-transformers/all-MiniLM-L6-v2" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/all-MiniLM-L6-v2/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "sentence-transformers/all-MiniLM-L6-v2" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/all-MiniLM-L6-v2/synonym_results_coleop.csv" \
  --threshold 0.70


# all-mpnet-base-v2
python src/models/mlp.py \
  --model-name "sentence-transformers/all-mpnet-base-v2" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/all-mpnet-base-v2/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "sentence-transformers/all-mpnet-base-v2" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/all-mpnet-base-v2/synonym_results_coleop.csv" \
  --threshold 0.70


# BGE Base
python src/models/mlp.py \
  --model-name "BAAI/bge-base-en-v1.5" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/bge-base-en-v1.5/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "BAAI/bge-base-en-v1.5" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/bge-base-en-v1.5/synonym_results_coleop.csv" \
  --threshold 0.70


# E5 Base v2
python src/models/mlp.py \
  --model-name "intfloat/e5-base-v2" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/e5-base-v2/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "intfloat/e5-base-v2" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/e5-base-v2/synonym_results_coleop.csv" \
  --threshold 0.70


# SciNCL
python src/models/mlp.py \
  --model-name "malteos/scincl" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/scincl/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "malteos/scincl" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/scincl/synonym_results_coleop.csv" \
  --threshold 0.70


# PatentSBERTa
python src/models/mlp.py \
  --model-name "AI-Growth-Lab/PatentSBERTa" \
  --file "data/only_synonyms_lepo.csv" \
  --output "results/PatentSBERTa/synonym_results_lepo.csv" \
  --threshold 0.70

python src/models/mlp.py \
  --model-name "AI-Growth-Lab/PatentSBERTa" \
  --file "data/only_synonyms_coleop.csv" \
  --output "results/PatentSBERTa/synonym_results_coleop.csv" \
  --threshold 0.70