# Language Model Embeddings for Species in Biodiversity

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![GBIF](https://img.shields.io/badge/Data-GBIF-orange.svg)](https://www.gbif.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

This repository evaluates transformer-based language model embeddings for identifying synonym relationships between legacy and currently accepted species names in biodiversity datasets.

The workflow generates embeddings from taxonomic names and performs zero-shot classification using a Multi-Layer Perceptron (MLP) to distinguish synonym and non-synonym pairs. Experiments were conducted on Coleoptera and Lepidoptera datasets derived from biodiversity taxonomic resources.

## Features

* Taxonomic name embedding generation
* Support for scientific, biomedical, and general-purpose language models
* Zero-shot synonym classification
* Comparative evaluation across multiple embedding architectures
* Biodiversity-focused benchmarking

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

| Model                                                  | Best for                                      |
| ------------------------------------------------------ | --------------------------------------------- |
| `allenai/scibert_scivocab_uncased`                     | Scientific papers, taxonomy text              |
| `allenai/scibert_scivocab_cased`                       | Scientific names where capitalization matters |
| `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract` | Biomedical and species-related text           |
| `pritamdeka/S-BioBERT-snli-multinli-stsb`              | Biomedical sentence similarity                |
| `sentence-transformers/all-MiniLM-L6-v2`               | Fast general semantic similarity              |
| `sentence-transformers/all-mpnet-base-v2`              | Strong general-purpose similarity             |
| `BAAI/bge-base-en-v1.5`                                | Retrieval and semantic search                 |
| `intfloat/e5-base-v2`                                  | Search-style embeddings                       |
| `malteos/scincl`                                       | Scientific paper embeddings                   |
| `AI-Growth-Lab/PatentSBERTa`                           | Technical terminology similarity              |

## Decoder Embeddings

| Model         | Type         | Biodiversity Usefulness |
| ------------- | ------------ | ----------------------- |
| `gpt2`        | Decoder-only | Baseline                |
| `gpt2-medium` | Decoder-only | Improved baseline       |

## Balanced Binary Classification

### Coleoptera Results

| Model | Accuracy | Precision | Recall | F1 | TN | FP | FN | TP | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BGE | 0.8425 | 0.9652 | 0.7106 | 0.8186 | 266 | 7 | 79 | 194 | 546 |
| PatentSBERTa | 0.8077 | 0.9667 | 0.6374 | 0.7682 | 267 | 6 | 99 | 174 | 546 |
| SciBERT-C | 0.5971 | 0.5563 | 0.9597 | 0.7043 | 64 | 209 | 11 | 262 | 546 |
| SciBERT-U | 0.5568 | 0.5328 | 0.9231 | 0.6756 | 52 | 221 | 21 | 252 | 546 |
| SciNCL | 0.5073 | 0.5037 | 1.0000 | 0.6699 | 4 | 269 | 0 | 273 | 546 |
| GPT-2 Medium | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| BiomedBERT | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| E5 | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| GPT-2 | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 273 | 0 | 273 | 546 |
| MPNet | 0.7198 | 0.9615 | 0.4579 | 0.6203 | 268 | 5 | 148 | 125 | 546 |
| MiniLM | 0.6557 | 0.9775 | 0.3187 | 0.4807 | 271 | 2 | 186 | 87 | 546 |
| S-BioBERT | 0.6465 | 0.9878 | 0.2967 | 0.4563 | 272 | 1 | 192 | 81 | 546 |


### Lepidoptera Results

| Model | Accuracy | Precision | Recall | F1 | TN | FP | FN | TP | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BGE | 0.8385 | 0.9960 | 0.6798 | 0.8081 | 1470 | 4 | 472 | 1002 | 2948 |
| PatentSBERTa | 0.7965 | 0.9932 | 0.5970 | 0.7458 | 1468 | 6 | 594 | 880 | 2948 |
| SciBERT-C | 0.5970 | 0.5577 | 0.9383 | 0.6995 | 377 | 1097 | 91 | 1383 | 2948 |
| SciBERT-U | 0.5868 | 0.5534 | 0.8996 | 0.6853 | 404 | 1070 | 148 | 1326 | 2948 |
| SciNCL | 0.5146 | 0.5074 | 0.9939 | 0.6719 | 52 | 1422 | 9 | 1465 | 2948 |
| GPT-2 Medium | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| BiomedBERT | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| E5 | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| GPT-2 | 0.5000 | 0.5000 | 1.0000 | 0.6667 | 0 | 1474 | 0 | 1474 | 2948 |
| MPNet | 0.6720 | 0.9903 | 0.3474 | 0.5143 | 1469 | 5 | 962 | 512 | 2948 |
| MiniLM | 0.6214 | 0.9945 | 0.2442 | 0.3922 | 1472 | 2 | 1114 | 360 | 2948 |
| S-BioBERT | 0.6065 | 0.9968 | 0.2137 | 0.3520 | 1473 | 1 | 1159 | 315 | 2948 |
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
