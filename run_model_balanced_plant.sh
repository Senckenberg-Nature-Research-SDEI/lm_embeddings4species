#!/bin/bash

INPUT_FILES=(
#   "data/balanced_synonym_fabales_dataset.csv"
#   "data/balanced_synonym_lamiales_dataset.csv"
#  "data/balanced_synonym_poales_dataset.csv"
  "data/balanced_synonym_rosales_dataset.csv"
)

MODELS=(
# "allenai/scibert_scivocab_uncased|scibert_scivocab_uncased"
# "allenai/scibert_scivocab_cased|scibert_scivocab_cased"
# "microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract|BiomedBERT"
# "pritamdeka/S-BioBERT-snli-multinli-stsb|S-BioBERT"
# "sentence-transformers/all-MiniLM-L6-v2|all-MiniLM-L6-v2"
# "sentence-transformers/all-mpnet-base-v2|all-mpnet-base-v2"
# "BAAI/bge-base-en-v1.5|bge-base-en-v1.5"
# "intfloat/e5-base-v2|e5-base-v2"
# "malteos/scincl|scincl"
# "AI-Growth-Lab/PatentSBERTa|PatentSBERTa"
# "BAAI/bge-large-zh-v1.5|bge-large-zh-v1.5"
# "BAAI/bge-large-en|bge-large-en"
# "BAAI/llm-embedder|llm-embedder"
# "BAAI/bge-reranker-v2-m3|bge-reranker-v2-m3"
# "BAAI/bge-reranker-v2-gemma|bge-reranker-v2-gemma"
"BAAI/bge-reranker-large|bge-reranker-large"
# "BAAI/bge-reranker-base|bge-reranker-base"
# "almanach/ModernBERT-bio-large|ModernBERT-bio-large"
# "answerdotai/ModernBERT-large|ModernBERT-large"
)

for INPUT_FILE in "${INPUT_FILES[@]}"; do
    DATASET_NAME="$(basename "$INPUT_FILE" .csv)"

    for entry in "${MODELS[@]}"; do
        MODEL="${entry%%|*}"
        OUTDIR="${entry##*|}"

        echo "======================================"
        echo "Dataset: $DATASET_NAME"
        echo "Model:   $MODEL"
        echo "======================================"

        mkdir -p "results_plant/${OUTDIR}"

        python src/models/mlp_balanced.py \
            --model-name "$MODEL" \
            --file "$INPUT_FILE" \
            --output "results_plant/${OUTDIR}/${DATASET_NAME}_results.csv" \
            --threshold 0.70
    done
done

echo "Done!"