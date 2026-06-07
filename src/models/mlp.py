# pip install torch transformers scikit-learn numpy pandas

import argparse
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "allenai/scibert_scivocab_uncased"


def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model


def get_bert_embedding(text, tokenizer, model):
    inputs = tokenizer(
        str(text),
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=64
    )

    with torch.no_grad():
        outputs = model(**inputs)

    cls_embedding = outputs.last_hidden_state[:, 0, :]
    return cls_embedding.cpu().numpy()


def read_terms_from_file(file_path):
    df = pd.read_csv(file_path)

    required_cols = ["species", "oldSpeciesCanonicalName"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return df


def synonym_or_not(term1, term2, tokenizer, model, threshold=0.75):
    emb1 = get_bert_embedding(term1, tokenizer, model)
    emb2 = get_bert_embedding(term2, tokenizer, model)

    similarity = cosine_similarity(emb1, emb2)[0][0]
    prediction = "synonym" if similarity >= threshold else "not synonym"

    return prediction, similarity


def main():
    parser = argparse.ArgumentParser(
        description="Check whether biodiversity species names are synonyms using SciBERT embeddings."
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

    tokenizer, model = load_model()
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
            args.threshold
        )

        results.append({
            "species": term1,
            "oldSpeciesCanonicalName": term2,
            "similarity": round(float(score), 4),
            "prediction": prediction
        })

        print(f"{term1} <-> {term2}")
        print(f"Similarity: {score:.4f}")
        print(f"Prediction: {prediction}")
        print("-" * 50)

    output_df = pd.DataFrame(results)
    output_df.to_csv(args.output, index=False)

    print(f"Results saved to: {args.output}")


if __name__ == "__main__":
    main()