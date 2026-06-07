# pip install torch transformers scikit-learn numpy pandas

import argparse
import os
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


def load_model(model_name, device):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model.to(device)
    model.eval()
    return tokenizer, model


def get_bert_embedding(text, tokenizer, model, device):
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
    attention_mask = inputs["attention_mask"].unsqueeze(-1)

    masked_embeddings = token_embeddings * attention_mask
    summed = masked_embeddings.sum(dim=1)
    counts = attention_mask.sum(dim=1).clamp(min=1)

    mean_embedding = summed / counts
    return mean_embedding.cpu().numpy()


def read_terms_from_file(file_path):
    df = pd.read_csv(file_path)

    required_cols = ["species", "oldSpeciesCanonicalName"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df = df.dropna(subset=required_cols)
    return df


def synonym_or_not(term1, term2, tokenizer, model, device, threshold=0.75):
    emb1 = get_bert_embedding(term1, tokenizer, model, device)
    emb2 = get_bert_embedding(term2, tokenizer, model, device)

    similarity = cosine_similarity(emb1, emb2)[0][0]
    prediction = "synonym" if similarity >= threshold else "not synonym"

    return prediction, similarity


def main():
    parser = argparse.ArgumentParser(
        description="Check whether biodiversity species names are synonyms using BERT embeddings."
    )

    parser.add_argument(
        "--model-name",
        type=str,
        default="pritamdeka/S-BioBERT-snli-multinli-stsb",
        help="Hugging Face model name"
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
            "threshold": args.threshold
        })

        print(f"{term1} <-> {term2}")
        print(f"Similarity: {score:.4f}")
        print(f"Prediction: {prediction}")
        print("-" * 50)

    os.makedirs(os.path.dirname(args.output), exist_ok=True) if os.path.dirname(args.output) else None

    output_df = pd.DataFrame(results)
    output_df.to_csv(args.output, index=False)

    print(f"Results saved to: {args.output}")


if __name__ == "__main__":
    main()