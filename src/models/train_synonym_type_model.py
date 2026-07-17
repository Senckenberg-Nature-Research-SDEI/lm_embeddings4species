import argparse
import json
import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


TARGET_CLASSES = ["not synonym", "synonym", "homotypical", "heterotypical"]


def normalize_label(value):
    if pd.isna(value):
        return None

    s = str(value).strip().lower().replace("-", "_").replace(" ", "_")

    mapping = {
        "0": "not synonym",
        "1": "synonym",
        "false": "not synonym",
        "true": "synonym",
        "negative": "not synonym",
        "positive": "synonym",
        "not_synonym": "not synonym",
        "nonsynonym": "not synonym",
        "synonym": "synonym",
        "synonyms": "synonym",
        "proparte_synonym": "synonym",
        "homotypic_synonym": "homotypical",
        "homotypical": "homotypical",
        "heterotypic_synonym": "heterotypical",
        "heterotypical": "heterotypical",
    }

    return mapping.get(s)


def build_training_labels(df, label_col, status_col, binary_col):
    if label_col and label_col in df.columns:
        labels = df[label_col].map(normalize_label)
        if labels.notna().sum() > 0:
            return labels

    if status_col and status_col in df.columns:
        labels = df[status_col].map(normalize_label)
        if labels.notna().sum() > 0:
            return labels

    if binary_col and binary_col in df.columns:
        labels = df[binary_col].map(normalize_label)
        if labels.notna().sum() > 0:
            return labels

    raise ValueError(
        "Could not infer labels. Provide one of: "
        f"{label_col}, {status_col}, or {binary_col} with valid values."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Train a synonym-type classifier (not synonym, synonym, homotypical, heterotypical)."
    )
    parser.add_argument("--file", required=True, help="Input CSV path")
    parser.add_argument("--output-dir", default="models/synonym_type_classifier", help="Output directory")
    parser.add_argument("--species-col", default="species", help="Species column name")
    parser.add_argument("--old-col", default="oldSpeciesCanonicalName", help="Old species column name")
    parser.add_argument("--label-col", default="synonym_type", help="Preferred label column")
    parser.add_argument("--status-col", default="oldSpeciesTaxonomicStatus", help="Taxonomic status label column")
    parser.add_argument("--binary-col", default="label", help="Fallback binary label column")
    parser.add_argument("--test-size", type=float, default=0.2, help="Test split ratio")
    parser.add_argument("--random-state", type=int, default=42, help="Random seed")

    args = parser.parse_args()

    df = pd.read_csv(args.file)

    required = [args.species_col, args.old_col]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing required text column: {col}")

    labels = build_training_labels(df, args.label_col, args.status_col, args.binary_col)

    work = pd.DataFrame(
        {
            "species": df[args.species_col].astype(str),
            "old": df[args.old_col].astype(str),
            "label": labels,
        }
    )

    work = work.dropna(subset=["label"]).copy()
    work = work[work["label"].isin(TARGET_CLASSES)].copy()

    if work.empty:
        raise ValueError("No valid rows left after label normalization.")

    class_counts = work["label"].value_counts().to_dict()
    text = "species=" + work["species"] + " [SEP] old=" + work["old"]
    y = work["label"]

    # Stratified split when every class has at least 2 rows.
    if all(count >= 2 for count in class_counts.values()) and args.test_size > 0:
        X_train, X_test, y_train, y_test = train_test_split(
            text,
            y,
            test_size=args.test_size,
            random_state=args.random_state,
            stratify=y,
        )
    else:
        X_train, y_train = text, y
        X_test = pd.Series([], dtype=str)
        y_test = pd.Series([], dtype=str)

    pipeline = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    analyzer="char_wb",
                    ngram_range=(2, 5),
                    min_df=2,
                ),
            ),
            (
                "clf",
                LogisticRegression(
                    max_iter=2000,
                    class_weight="balanced",
                    random_state=args.random_state,
                ),
            ),
        ]
    )

    pipeline.fit(X_train, y_train)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with (out_dir / "synonym_type_model.pkl").open("wb") as f:
        pickle.dump(pipeline, f)

    metadata = {
        "classes": TARGET_CLASSES,
        "class_counts": class_counts,
        "input_file": args.file,
        "species_col": args.species_col,
        "old_col": args.old_col,
        "label_col_used": (
            args.label_col if args.label_col in df.columns else args.status_col if args.status_col in df.columns else args.binary_col
        ),
    }

    if len(X_test) > 0:
        y_pred = pipeline.predict(X_test)

        report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
        confusion = confusion_matrix(y_test, y_pred, labels=TARGET_CLASSES)
        metadata["test_accuracy"] = float(accuracy_score(y_test, y_pred))
        metadata["classification_report"] = report
        metadata["confusion_matrix_labels"] = TARGET_CLASSES
        metadata["confusion_matrix"] = confusion.tolist()

        pred_df = pd.DataFrame({"text": X_test, "y_true": y_test, "y_pred": y_pred})
        pred_df.to_csv(out_dir / "test_predictions.csv", index=False)

    with (out_dir / "metadata.json").open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"Saved model: {out_dir / 'synonym_type_model.pkl'}")
    print(f"Saved metadata: {out_dir / 'metadata.json'}")
    if len(X_test) > 0:
        print(f"Saved test predictions: {out_dir / 'test_predictions.csv'}")
        print(f"Test accuracy: {metadata['test_accuracy']:.4f}")


if __name__ == "__main__":
    main()
