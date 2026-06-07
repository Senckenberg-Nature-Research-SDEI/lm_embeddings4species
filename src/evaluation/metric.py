# src/evaluation/metric.py
import argparse
from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


LABEL_MAPPING = {
    "synonym": 1,
    "synonyms": 1,
    "positive": 1,
    "true": 1,
    "1": 1,
    "not synonym": 0,
    "not_synonym": 0,
    "non-synonym": 0,
    "non synonym": 0,
    "nonsynonym": 0,
    "negative": 0,
    "false": 0,
    "0": 0,
}


def to_binary(series):
    return series.astype(str).str.lower().str.strip().map(LABEL_MAPPING).astype(int)

def compute_metrics(csv_file, label_col, pred_col):
    print(f"Processing: {csv_file}")
    try:
        print(f"Processing: {csv_file}")
        df = pd.read_csv(csv_file)
    except pd.errors.EmptyDataError:
        print(f"Skipping {csv_file}: empty file")
        return None

    if label_col not in df.columns or pred_col not in df.columns:
        print(f"Skipping {csv_file}: missing {label_col} or {pred_col}")
        return None

    y_true = to_binary(df[label_col])
    y_pred = to_binary(df[pred_col])

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

    return {
        "model": csv_file.parent.name,
        "file": csv_file.name,
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "tp": tp,
        "total": len(df),
    }

def main(args):
    rows = []

    for csv_file in sorted(Path(args.input_folder).rglob("*.csv")):
        result = compute_metrics(csv_file, args.label_col, args.pred_col)
        if result is not None:
            rows.append(result)

    results = pd.DataFrame(rows)
    results.to_csv(args.output_file, index=False)

    print(f"Saved metrics to: {args.output_file}")
    print(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_folder", required=True)
    parser.add_argument("--output_file", default="results/metrics_summary.csv")
    parser.add_argument("--label_col", default="label")
    parser.add_argument("--pred_col", default="prediction")
    args = parser.parse_args()
    main(args)