# pip install pandas scikit-learn

import argparse
import os
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


def normalize_text(text):
    return str(text).lower().strip()


def normalize_label(label):
    label = str(label).lower().strip()

    mapping = {
        "1": "synonym",
        "true": "synonym",
        "yes": "synonym",
        "positive": "synonym",
        "synonym": "synonym",
        "0": "not synonym",
        "false": "not synonym",
        "no": "not synonym",
        "negative": "not synonym",
        "not synonym": "not synonym",
        "non-synonym": "not synonym",
        "nonsynonym": "not synonym",
    }

    if label not in mapping:
        raise ValueError(f"Unknown label value: {label}")

    return mapping[label]


def levenshtein_distance(a, b):
    a = normalize_text(a)
    b = normalize_text(b)

    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    prev = list(range(len(b) + 1))

    for i, ca in enumerate(a, start=1):
        curr = [i]

        for j, cb in enumerate(b, start=1):
            curr.append(
                min(
                    curr[j - 1] + 1,
                    prev[j] + 1,
                    prev[j - 1] + int(ca != cb),
                )
            )

        prev = curr

    return prev[-1]


def levenshtein_similarity(a, b):
    a = normalize_text(a)
    b = normalize_text(b)

    max_len = max(len(a), len(b))
    if max_len == 0:
        return 1.0

    return 1.0 - (levenshtein_distance(a, b) / max_len)


def read_terms_from_file(file_path):
    df = pd.read_csv(file_path)

    required_cols = ["species", "oldSpeciesCanonicalName", "label"]
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    df = df.dropna(subset=required_cols).copy()
    df["label"] = df["label"].apply(normalize_label)

    return df


def make_output_path(input_file, output_file):
    if output_file is not None:
        return output_file

    input_dir = os.path.dirname(input_file)
    input_name = os.path.splitext(os.path.basename(input_file))[0]

    return os.path.join(input_dir, f"{input_name}_levenshtein_results.csv")


def make_metrics_output_path(output_path, metrics_output_file):
    if metrics_output_file is not None:
        return metrics_output_file

    output_dir = os.path.dirname(output_path)
    output_name = os.path.splitext(os.path.basename(output_path))[0]

    return os.path.join(output_dir, f"{output_name}_metrics.csv")


def main():
    parser = argparse.ArgumentParser(
        description="Levenshtein baseline for biodiversity species synonym detection."
    )

    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--metrics-output", type=str, default=None)
    parser.add_argument("--threshold", type=float, default=0.75)

    args = parser.parse_args()

    df = read_terms_from_file(args.file)
    results = []

    for _, row in df.iterrows():
        term1 = row["species"]
        term2 = row["oldSpeciesCanonicalName"]

        score = levenshtein_similarity(term1, term2)
        prediction = "synonym" if score >= args.threshold else "not synonym"

        results.append(
            {
                "species": term1,
                "oldSpeciesCanonicalName": term2,
                "similarity": round(float(score), 4),
                "prediction": prediction,
                "label": row["label"],
                "model": "Levenshtein",
                "threshold": args.threshold,
            }
        )

    output_df = pd.DataFrame(results)

    y_true = output_df["label"]
    y_pred = output_df["prediction"]

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(
        y_true, y_pred, pos_label="synonym", zero_division=0
    )
    recall = recall_score(
        y_true, y_pred, pos_label="synonym", zero_division=0
    )
    f1 = f1_score(
        y_true, y_pred, pos_label="synonym", zero_division=0
    )

    tn, fp, fn, tp = confusion_matrix(
        y_true,
        y_pred,
        labels=["not synonym", "synonym"],
    ).ravel()

    metrics_df = pd.DataFrame(
        [
            {
                "model": "Levenshtein",
                "dataset": os.path.basename(args.file),
                "threshold": args.threshold,
                "accuracy": round(float(accuracy), 4),
                "precision": round(float(precision), 4),
                "recall": round(float(recall), 4),
                "f1": round(float(f1), 4),
                "tn": int(tn),
                "fp": int(fp),
                "fn": int(fn),
                "tp": int(tp),
                "total": int(len(output_df)),
            }
        ]
    )

    print("Model: Levenshtein")
    print("Dataset:", os.path.basename(args.file))
    print("Threshold:", args.threshold)
    print("Total examples:", len(output_df))
    print("Accuracy:", round(float(accuracy), 4))
    print("Precision:", round(float(precision), 4))
    print("Recall:", round(float(recall), 4))
    print("F1:", round(float(f1), 4))
    print("Confusion matrix labels: ['not synonym', 'synonym']")
    print(confusion_matrix(y_true, y_pred, labels=["not synonym", "synonym"]))

    output_path = make_output_path(args.file, args.output)
    metrics_output_path = make_metrics_output_path(output_path, args.metrics_output)

    output_dir = os.path.dirname(output_path)
    metrics_output_dir = os.path.dirname(metrics_output_path)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    if metrics_output_dir:
        os.makedirs(metrics_output_dir, exist_ok=True)

    output_df.to_csv(output_path, index=False)
    metrics_df.to_csv(metrics_output_path, index=False)

    print(f"Results saved to: {output_path}")
    print(f"Metrics saved to: {metrics_output_path}")


if __name__ == "__main__":
    main()