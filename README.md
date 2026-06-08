
# Language Model Embeddings for Species Synonym Detection in Biodiversity

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![GBIF](https://img.shields.io/badge/Data-GBIF-orange.svg)](https://www.gbif.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

This repository evaluates pretrained transformer-based language model embeddings for identifying synonym relationships between legacy and currently accepted species names in biodiversity datasets.

Rather than training a task-specific classifier, species names are embedded using a variety of pretrained language models and compared using cosine similarity. Synonym detection is performed using a fixed similarity threshold, providing a simple zero-shot evaluation of embedding quality for taxonomic name matching.

Experiments were conducted on balanced Coleoptera and Lepidoptera datasets derived from biodiversity taxonomic resources. The benchmark compares scientific, biomedical, retrieval-oriented, and general-purpose embedding models for their ability to distinguish synonym and non-synonym species name pairs without any fine-tuning.

## Features

* Taxonomic name embedding generation
* Zero-shot synonym detection using cosine similarity
* No model training or fine-tuning required
* Support for scientific, biomedical, and general-purpose language models
* Balanced synonym/non-synonym benchmark datasets
* Comparative evaluation across multiple embedding architectures
* Biodiversity-focused embedding benchmark

## Method Overview

1. Generate embeddings for species names using pretrained language models.
2. Compute cosine similarity between species-name pairs.
3. Classify pairs as synonyms when similarity exceeds a fixed threshold (0.7).
4. Evaluate performance using Accuracy, Precision, Recall, F1-score, and confusion matrices.

This benchmark focuses on the intrinsic ability of embedding models to capture synonym relationships in biodiversity nomenclature without supervised training.

## Folder Hierarchy

```text
lm_embeddings4species/
├── data/                  # Input datasets and balanced synonym datasets
├── figures/               # Generated figures and comparison plots
├── logs/                  # Harvester logs
├── results/               # Model outputs and metrics summaries
├── results_zero/          # Zero-shot model output files
├── src/
│   ├── data_preparation/  # Data harvesting and dataset preparation scripts
│   ├── evaluation/        # Evaluation metrics and notebooks
│   ├── models/            # MLP model implementations
│   └── notebooks/         # Analysis and visualization notebooks
├── run_*.sh               # Pipeline runner scripts
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Senckenberg-Nature-Research-SDEI/lm_embeddings_4_species.git
cd lm_embeddings_4_species
pip install -r requirements.txt
```

## Usage

Run the data harvesting pipeline:

```bash
bash run_harvester.sh
```

Run embedding generation and classification:

```bash
bash run_model.sh
```

## Supported Embeddings

## Supported Models

| Model | Best for |
|---------|---------|
| `BAAI/bge-base-en-v1.5` | **Recommended default.** Best overall synonym detection performance, highest accuracy and F1 across both benchmark datasets. |
| `AI-Growth-Lab/PatentSBERTa` | Technical terminology, taxonomy concepts, and domain-specific synonym matching with excellent precision. |
| `allenai/scibert_scivocab_cased` | Scientific names and taxonomy text where capitalization may be meaningful; strong recall and F1. |
| `allenai/scibert_scivocab_uncased` | Scientific literature and taxonomy text requiring high recall. |
| `sentence-transformers/all-mpnet-base-v2` | General semantic similarity with very high precision and moderate recall. |
| `malteos/scincl` | Scientific literature embeddings with near-perfect recall. |
| `llmrails/llm-embedder` | Retrieval-oriented embeddings with high recall for semantic matching tasks. |
| `BAAI/bge-large-zh-v1.5` | Large multilingual embedding model; strong precision but lower recall on taxonomy synonym detection. |
| `sentence-transformers/all-MiniLM-L6-v2` | Lightweight and fast embedding model for large-scale experiments and prototyping. |
| `pritamdeka/S-BioBERT-snli-multinli-stsb` | Biomedical sentence similarity with extremely high precision and conservative matching behavior. |
| `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract` | Biomedical and life-science text embeddings; baseline performance on synonym detection benchmarks. |
| `BAAI/bge-large-en` | Large English embedding model; high recall but weak discrimination on these datasets. |
| `intfloat/e5-base-v2` | Query-document retrieval and search-oriented embeddings; baseline performance on synonym detection benchmarks. |
| `answerdotai/ModernBERT-bio-large` | Biomedical adaptation of ModernBERT; baseline performance on synonym detection benchmarks. |
| `answerdotai/ModernBERT-large` | General-purpose ModernBERT embeddings; high recall but poor discrimination on these datasets. |
| `gpt2-medium` | Transformer language model used experimentally for embedding generation; baseline benchmark performance. |
| `gpt2` | Lightweight GPT-2 embedding baseline; baseline benchmark performance. |
| `BAAI/bge-reranker-large` | Cross-encoder reranker optimized for re-ranking candidate pairs rather than standalone embeddings. |
| `BAAI/bge-reranker-base` | Lightweight reranker model for candidate ranking tasks. |
| `BAAI/bge-reranker-v2-m3` | Multilingual reranker for retrieval pipelines; not intended as a primary embedding model. |
| `BAAI/bge-reranker-v2-gemma` | Gemma-based reranker optimized for ranking and retrieval refinement. |

## Decoder Embeddings

| Model         | Type         | Biodiversity Usefulness |
| ------------- | ------------ | ----------------------- |
| `gpt2`        | Decoder-only | Baseline                |
| `gpt2-medium` | Decoder-only | Improved baseline       |

## Balanced Binary Classification

| Model | Dataset | Accuracy | Precision | Recall | F1 | TN | FP | FN | TP | Total |
|---------|---------|---------:|---------:|---------:|---------:|----:|----:|----:|----:|------:|
| ModernBERT-bio-large | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| ModernBERT-bio-large | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| BiomedBERT | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| BiomedBERT | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| gpt2-medium | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| gpt2-medium | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| scibert_scivocab_uncased | coleop | 0.5568 | 0.5328 | 0.9231 | 0.6756 | 52 | 221 | 21 | 252 | 546 |
| scibert_scivocab_uncased | lepo | 0.5868 | 0.5534 | 0.8996 | 0.6853 | 404 | 1070 | 148 | 1326 | 2948 |
| bge-base-en-v1.5 | coleop | **0.8425** | 0.9652 | 0.7106 | **0.8186** | 266 | 7 | 79 | 194 | 546 |
| bge-base-en-v1.5 | lepo | **0.8385** | 0.9960 | 0.6798 | **0.8081** | 1470 | 4 | 472 | 1002 | 2948 |
| all-mpnet-base-v2 | coleop | 0.7198 | 0.9615 | 0.4579 | 0.6203 | 268 | 5 | 148 | 125 | 546 |
| all-mpnet-base-v2 | lepo | 0.6720 | 0.9903 | 0.3474 | 0.5143 | 1469 | 5 | 962 | 512 | 2948 |
| bge-reranker-large | coleop | 0.5018 | 0.5009 | 0.9890 | 0.6650 | 4 | 269 | 3 | 270 | 546 |
| bge-reranker-large | lepo | 0.5037 | 0.5019 | 0.9946 | 0.6671 | 19 | 1455 | 8 | 1466 | 2948 |
| bge-reranker-v2-m3 | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| bge-reranker-v2-m3 | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| PatentSBERTa | coleop | 0.8077 | 0.9667 | 0.6374 | 0.7682 | 267 | 6 | 99 | 174 | 546 |
| PatentSBERTa | lepo | 0.7965 | 0.9932 | 0.5970 | 0.7458 | 1468 | 6 | 594 | 880 | 2948 |
| bge-reranker-base | coleop | 0.5275 | 0.5149 | 0.9487 | 0.6675 | 29 | 244 | 14 | 259 | 546 |
| bge-reranker-base | lepo | 0.5129 | 0.5067 | 0.9756 | 0.6670 | 74 | 1400 | 36 | 1438 | 2948 |
| S-BioBERT | coleop | 0.6465 | 0.9878 | 0.2967 | 0.4563 | 272 | 1 | 192 | 81 | 546 |
| S-BioBERT | lepo | 0.6065 | 0.9968 | 0.2137 | 0.3520 | 1473 | 1 | 1159 | 315 | 2948 |
| bge-large-zh-v1.5 | coleop | 0.7436 | 0.9716 | 0.5018 | 0.6618 | 269 | 4 | 136 | 137 | 546 |
| bge-large-zh-v1.5 | lepo | 0.7405 | 0.9944 | 0.4837 | 0.6508 | 1470 | 4 | 761 | 713 | 2948 |
| sciNCL | coleop | 0.5073 | 0.5037 | 1.0000 | 0.6699 | 4 | 269 | 0 | 273 | 546 |
| sciNCL | lepo | 0.5146 | 0.5074 | 0.9939 | 0.6719 | 52 | 1422 | 9 | 1465 | 2948 |
| scibert_scivocab_cased | coleop | 0.5971 | 0.5563 | 0.9597 | 0.7043 | 64 | 209 | 11 | 262 | 546 |
| scibert_scivocab_cased | lepo | 0.5970 | 0.5577 | 0.9383 | 0.6995 | 377 | 1097 | 91 | 1383 | 2948 |
| bge-reranker-v2-gemma | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| bge-reranker-v2-gemma | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| ModernBERT-large | coleop | 0.4982 | 0.4991 | 0.9890 | 0.6634 | 2 | 271 | 3 | 270 | 546 |
| ModernBERT-large | lepo | 0.5007 | 0.5003 | 1.0000 | 0.6670 | 2 | 1472 | 0 | 1474 | 2948 |
| bge-large-en | coleop | 0.5037 | 0.5018 | 1.0000 | 0.6683 | 2 | 271 | 0 | 273 | 546 |
| bge-large-en | lepo | 0.5031 | 0.5015 | 1.0000 | 0.6680 | 9 | 1465 | 0 | 1474 | 2948 |
| all-MiniLM-L6-v2 | coleop | 0.6557 | 0.9775 | 0.3187 | 0.4807 | 271 | 2 | 186 | 87 | 546 |
| all-MiniLM-L6-v2 | lepo | 0.6214 | 0.9945 | 0.2442 | 0.3922 | 1472 | 2 | 1114 | 360 | 2948 |
| e5-base-v2 | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| e5-base-v2 | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| gpt2 | coleop | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| gpt2 | lepo | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| llm-embedder | coleop | 0.5165 | 0.5084 | 0.9927 | 0.6725 | 11 | 262 | 2 | 271 | 546 |
| llm-embedder | lepo | 0.5095 | 0.5048 | 0.9959 | 0.6700 | 34 | 1440 | 6 | 1468 | 2948 |
## Results-only Synonym

Number of synonym pairs identified as synonyms by each embedding model.

| Model | Coleoptera Synonym Pairs Detected | Lepidoptera Synonym Pairs Detected |
|---|---:|---:|
| all-MiniLM-L6-v2 | 87 / 273 | 361 / 1482 |
| all-mpnet-base-v2 | 125 / 273 | 516 / 1482 |
| bge-base-en-v1.5 | 194 / 273 | 1007 / 1482 |
| BiomedBERT | 273 / 273 | 1482 / 1482 |
| e5-base-v2 | 273 / 273 | 1482 / 1482 |
| gpt2 | 273 / 273 | 1482 / 1482 |
| gpt2-medium | 273 / 273 | 1482 / 1482 |
| PatentSBERTa | 174 / 273 | 883 / 1482 |
| S-BioBERT | 81 / 273 | 316 / 1482 |
| scibert_scivocab_cased | 262 / 273 | 1391 / 1482 |
| scibert_scivocab_uncased | 252 / 273 | 1332 / 1482 |
| scincl | 273 / 273 | 1473 / 1482 |
## Citation

If you use this repository in your research, please cite the associated publication and/or Zenodo record.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for details.
