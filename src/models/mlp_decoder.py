# pip install torch transformers scikit-learn numpy pandas accelerate

import argparse
import os
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


def load_model(model_name, device):
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModel.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    model.to(device)
    model.eval()

    return tokenizer, model


def get_decoder_embedding(text, tokenizer, model, device):
    inputs = tokenizer(
        str(text),
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=64
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    token_embeddings = outputs.last_hidden_state
    attention_mask = inputs["attention_mask"]

    last_token_indices = attention_mask.sum(dim=1) - 1

    batch_indices = torch.arange(
        token_embeddings.size(0),
        device=device
    )

    last_token_embedding = token_embeddings[
        batch_indices,
        last_token_indices
    ]

    return last_token_embedding.cpu().numpy()


def read_terms_from_file(file_path):
    df = pd.read_csv(file_path)

    required_cols = ["species", "oldSpeciesCanonicalName"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df = df.dropna(subset=required_cols)
    return df


def synonym_or_not(term1, term2, tokenizer, model, device, threshold=0.75):
    emb1 = get_decoder_embedding(term1, tokenizer, model, device)
    emb2 = get_decoder_embedding(term2, tokenizer, model, device)

    similarity = cosine_similarity(emb1, emb2)[0][0]
    prediction = "synonym" if similarity >= threshold else "not synonym"

    return prediction, similarity


def main():
    parser = argparse.ArgumentParser(
        description="Check biodiversity species synonyms using decoder-model embeddings."
    )

    parser.add_argument(
        "--model-name",
        type=str,
        default="gpt2",
        help="Decoder-only Hugging Face model name"
    )

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="synonym_results.csv",
        help="Path to save output CSV file"
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=0.75,
        help="Cosine similarity threshold"
    )

    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer, model = load_model(args.model_name, device)
    df = read_terms_from_file(args.file)

    results = []

    for _, row in df.iterrows():
        term1 = row["species"]
        term2 = row["oldSpeciesCanonicalName"]

        prediction, score = synonym_or_not(
            term1,
            term2,
            tokenizer,
            model,
            device,
            args.threshold
        )

        results.append({
            "species": term1,
            "oldSpeciesCanonicalName": term2,
            "similarity": round(float(score), 4),
            "prediction": prediction,
            "model": args.model_name,
            "threshold": args.threshold,
            "pooling": "last_token"
        })

    if os.path.dirname(args.output):
        os.makedirs(os.path.dirname(args.output), exist_ok=True)

    pd.DataFrame(results).to_csv(args.output, index=False)
    print(f"Results saved to: {args.output}")


if __name__ == "__main__":
    main()