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
| `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | Decoder-only | Modern small LLM |
| `Qwen/Qwen2.5-0.5B` | Decoder-only | Compact modern model |
| `Qwen/Qwen2.5-1.5B` | Decoder-only | Better semantic representation |
| `HuggingFaceTB/SmolLM2-360M` | Decoder-only | Small and practical |
| `HuggingFaceTB/SmolLM2-1.7B` | Decoder-only | Better quality, heavier |
| `microsoft/phi-2` | Decoder-only | Strong small model, heavier |
| `allenai/OLMo-1B-hf` | Decoder-only | Scientific/general text baseline |
| `mistralai/Mistral-7B-v0.1` | Decoder-only | Strong, but heavy |
| `meta-llama/Llama-3.2-1B` | Decoder-only | Good small LLaMA-style option |
| `meta-llama/Llama-3.2-3B` | Decoder-only | Better, heavier |