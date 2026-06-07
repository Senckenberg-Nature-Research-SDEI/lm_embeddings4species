# make_balanced_dataset.py
import argparse
import pandas as pd


def make_balanced_dataset(args):
    df = pd.read_csv(args.input_csv)

    positives = df[[args.legacy_col, args.accepted_col, args.taxon_id_col]].copy()
    positives = positives.dropna().drop_duplicates().reset_index(drop=True)
    positives["label"] = 1

    if positives[args.taxon_id_col].nunique() < 2:
        raise ValueError("Need at least two different taxon IDs for negative sampling.")

    negatives = positives.copy()

    for i in range(len(negatives)):
        current_taxon_id = positives.loc[i, args.taxon_id_col]

        candidates = positives[
            positives[args.taxon_id_col] != current_taxon_id
        ]

        sampled = candidates.sample(
            n=1,
            random_state=args.seed + i
        ).iloc[0]

        negatives.loc[i, args.accepted_col] = sampled[args.accepted_col]
        negatives.loc[i, args.taxon_id_col] = sampled[args.taxon_id_col]
        negatives.loc[i, "label"] = 0

    balanced = pd.concat([positives, negatives], ignore_index=True)
    balanced = balanced.sample(frac=1, random_state=args.seed).reset_index(drop=True)

    balanced.to_csv(args.output_csv, index=False)

    print("Saved:", args.output_csv)
    print(balanced["label"].value_counts())


if __name__ == "__main__":
    print("Creating balanced dataset...")

    parser = argparse.ArgumentParser()

    parser.add_argument("--input_csv", required=True)
    parser.add_argument("--output_csv", required=True)

    parser.add_argument("--legacy_col", default="legacy_name")
    parser.add_argument("--accepted_col", default="accepted_name")
    parser.add_argument("--taxon_id_col", default="accepted_id")

    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()
    make_balanced_dataset(args)