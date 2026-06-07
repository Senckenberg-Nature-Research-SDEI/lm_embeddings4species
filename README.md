# Language Model Embeddings for Species in Biodiversity
Similarity between legacy and current names


Zero-shot Classification with SciBERT embeddings

# Supported Embeddings
| Model | Best for |
|---|---|
| `allenai/scibert_scivocab_uncased` | Scientific papers, taxonomy text |
| `allenai/scibert_scivocab_cased` | Scientific names where capitalization matters |
| `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract` | Biomedical and species-related text |
| `pritamdeka/S-BioBERT-snli-multinli-stsb` | Biomedical sentence similarity |
| `sentence-transformers/all-MiniLM-L6-v2` | Fast general semantic similarity |
| `sentence-transformers/all-mpnet-base-v2` | Strong general-purpose similarity |
| `BAAI/bge-base-en-v1.5` | Retrieval and semantic search |
| `intfloat/e5-base-v2` | Search-style embeddings |
| `malteos/scincl` | Scientific paper embeddings |
| `AI-Growth-Lab/PatentSBERTa` | Technical terminology similarity |


## Decoder Embeddings
| Model | Type | Biodiversity usefulness |
|---|---|---|
| `gpt2` | Decoder-only | Baseline only |
| `gpt2-medium` | Decoder-only | Better baseline |


## Results:
| Model | Coleoptera Synonyms | Coleoptera Non-synonyms | Lepidoptera Synonyms | Lepidoptera Non-synonyms |
|-------|--------------------:|------------------------:|---------------------:|-------------------------:|
| all-MiniLM-L6-v2 | 87 | 186 | 361 | 1121 |
| all-mpnet-base-v2 | 125 | 148 | 516 | 966 |
| bge-base-en-v1.5 | 194 | 79 | 1007 | 475 |
| BiomedBERT | 273 | 0 | 1482 | 0 |
| e5-base-v2 | 273 | 0 | 1482 | 0 |
| gpt2 | 273 | 0 | 1482 | 0 |
| gpt2-medium | 273 | 0 | 1482 | 0 |
| PatentSBERTa | 174 | 99 | 883 | 599 |
| S-BioBERT | 81 | 192 | 316 | 1166 |
| scibert_scivocab_cased | 262 | 11 | 1391 | 91 |
| scibert_scivocab_uncased | 252 | 21 | 1332 | 150 |
| scincl | 273 | 0 | 1473 | 9 |

## License:
GNU General Public License v3.0
