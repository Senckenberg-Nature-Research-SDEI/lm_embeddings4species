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

## Results

Number of correctly classified synonym and non-synonym pairs.

| Model                    | Coleoptera Synonyms | Coleoptera Non-synonyms | Lepidoptera Synonyms | Lepidoptera Non-synonyms |
| ------------------------ | ------------------: | ----------------------: | -------------------: | -----------------------: |
| all-MiniLM-L6-v2         |                  87 |                     186 |                  361 |                     1121 |
| all-mpnet-base-v2        |                 125 |                     148 |                  516 |                      966 |
| bge-base-en-v1.5         |                 194 |                      79 |                 1007 |                      475 |
| BiomedBERT               |                 273 |                       0 |                 1482 |                        0 |
| e5-base-v2               |                 273 |                       0 |                 1482 |                        0 |
| gpt2                     |                 273 |                       0 |                 1482 |                        0 |
| gpt2-medium              |                 273 |                       0 |                 1482 |                        0 |
| PatentSBERTa             |                 174 |                      99 |                  883 |                      599 |
| S-BioBERT                |                  81 |                     192 |                  316 |                     1166 |
| scibert_scivocab_cased   |                 262 |                      11 |                 1391 |                       91 |
| scibert_scivocab_uncased |                 252 |                      21 |                 1332 |                      150 |
| scincl                   |                 273 |                       0 |                 1473 |                        9 |

## Citation

If you use this repository in your research, please cite the associated publication and/or Zenodo record.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for details.
