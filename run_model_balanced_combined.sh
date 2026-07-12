#!/bin/bash
#SBATCH --job-name=mlp_balanced_combined
#SBATCH --mail-user=sefie08@zedat.fu-berlin.de
#SBATCH --mail-type=end
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=480960
#SBATCH --time=48:00:00
#SBATCH --qos=standard
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=1

set -euo pipefail

cd /home/${USER}/projects/biodiv/lm_embeddings_4_species

module add Python/3.9.5-GCCcore-10.3.0

source ~/path/to/new/virtual/environment/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

INPUT_FILES=(
    "data/balanced_synonym_coleop_dataset.csv"
    "data/balanced_synonym_lepidoptera_dataset.csv"
    "data/balanced_synonym_fabales_dataset.csv"
    "data/balanced_synonym_lamiales_dataset.csv"
    "data/balanced_synonym_poales_dataset.csv"
    "data/balanced_synonym_rosales_dataset.csv"
)

if [[ ${#INPUT_FILES[@]} -eq 0 ]]; then
    echo "No plant/insect balanced dataset files configured."
    exit 1
fi

COMBINED_FILE="data/balanced_synonym_all_combined_dataset.csv"

first_file=1
> "$COMBINED_FILE"

for input_file in "${INPUT_FILES[@]}"; do
    if [[ $first_file -eq 1 ]]; then
        cat "$input_file" > "$COMBINED_FILE"
        first_file=0
    else
        tail -n +2 "$input_file" >> "$COMBINED_FILE"
    fi
    echo "Added: $input_file"
done

echo "Combined dataset created: $COMBINED_FILE"
echo "Total rows (including header): $(wc -l < \"$COMBINED_FILE\")"

MODELS=(
"allenai/scibert_scivocab_uncased|scibert_scivocab_uncased"
"allenai/scibert_scivocab_cased|scibert_scivocab_cased"
"microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract|BiomedBERT"
"pritamdeka/S-BioBERT-snli-multinli-stsb|S-BioBERT"
"sentence-transformers/all-MiniLM-L6-v2|all-MiniLM-L6-v2"
"sentence-transformers/all-mpnet-base-v2|all-mpnet-base-v2"
"BAAI/bge-base-en-v1.5|bge-base-en-v1.5"
"intfloat/e5-base-v2|e5-base-v2"
"malteos/scincl|scincl"
"AI-Growth-Lab/PatentSBERTa|PatentSBERTa"
"BAAI/bge-large-zh-v1.5|bge-large-zh-v1.5"
"BAAI/bge-large-en|bge-large-en"
"BAAI/llm-embedder|llm-embedder"
"BAAI/bge-reranker-v2-m3|bge-reranker-v2-m3"
"BAAI/bge-reranker-v2-gemma|bge-reranker-v2-gemma"
"BAAI/bge-reranker-large|bge-reranker-large"
"BAAI/bge-reranker-base|bge-reranker-base"
"almanach/ModernBERT-bio-large|ModernBERT-bio-large"
"answerdotai/ModernBERT-large|ModernBERT-large"
)

DATASET_NAME="$(basename "$COMBINED_FILE" .csv)"

for entry in "${MODELS[@]}"; do
    MODEL="${entry%%|*}"
    OUTDIR="${entry##*|}"

    echo "======================================"
    echo "Dataset: $DATASET_NAME"
    echo "Model:   $MODEL"
    echo "======================================"

    mkdir -p "results_combined/${OUTDIR}"

    python src/models/mlp_balanced.py \
        --model-name "$MODEL" \
        --file "$COMBINED_FILE" \
        --output "results_combined/${OUTDIR}/${DATASET_NAME}_results.csv" \
        --threshold 0.70
done

echo "Done!"