import argparse
import re
from pathlib import Path

import pandas as pd

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError as exc:
    raise SystemExit(
        "matplotlib is not installed in the active environment. "
        "Install dependencies with: pip install -r requirements.txt"
    ) from exc


def collect_metrics(metrics_file=None, results_root="results_plant"):
    """Load one or many metrics_summary.csv files into one DataFrame."""
    if metrics_file:
        path = Path(metrics_file)
        if not path.exists():
            raise FileNotFoundError(f"Metrics file not found: {path}")
        df = pd.read_csv(path)
        if "model" not in df.columns:
            # If model column is missing, infer from parent directory name.
            df["model"] = path.parent.name
        return df

    root = Path(results_root)
    files = sorted(root.glob("*/metrics_summary.csv"))

    if not files:
        raise FileNotFoundError(
            f"No metrics_summary.csv found under {root}. "
            "Run metric generation first."
        )

    frames = []
    for file_path in files:
        part = pd.read_csv(file_path)
        if "model" not in part.columns:
            part["model"] = file_path.parent.name
        frames.append(part)

    return pd.concat(frames, ignore_index=True)


def extract_plant_name(file_name):
    """Extract plant group from filenames like balanced_synonym_fabales_dataset_results.csv."""
    if pd.isna(file_name):
        return "unknown"

    text = str(file_name).lower()
    match = re.search(r"balanced_synonym_(.*?)_dataset", text)
    if match:
        return match.group(1)
    return "unknown"


def plot_metric_figure(
    df,
    metric="accuracy",
    output_file="figures/results_plant_accuracy.png",
    title="Plant Model Accuracy",
    style="bars",
    score_fontsize=8,
    score_rotation=0,
):
    """Create a grouped chart of metric values per model and plant."""
    if metric not in df.columns:
        raise ValueError(f"Input metrics must include a '{metric}' column.")

    work_df = df.copy()

    if "file" in work_df.columns:
        work_df["plant"] = work_df["file"].map(extract_plant_name)
    elif "plant" not in work_df.columns:
        work_df["plant"] = "all"

    plot_df = (
        work_df.groupby(["model", "plant"], as_index=False)[metric]
        .mean()
    )

    model_order = (
        plot_df.groupby("model", as_index=False)[metric]
        .mean()
        .sort_values(metric, ascending=False)["model"]
        .tolist()
    )
    plant_order = sorted(plot_df["plant"].unique().tolist())
    pivot_df = (
        plot_df.pivot(index="model", columns="plant", values=metric)
        .reindex(model_order)
    )

    plt.figure(figsize=(13, 6))
    ax = plt.gca()

    x_positions = range(len(model_order))

    if style == "points":
        for plant in plant_order:
            y_values = pivot_df[plant].values
            ax.scatter(x_positions, y_values, label=plant, s=36)
    else:
        width = 0.8 / max(len(plant_order), 1)
        offsets = [
            (idx - (len(plant_order) - 1) / 2) * width
            for idx in range(len(plant_order))
        ]
        for plant_idx, plant in enumerate(plant_order):
            y_values = pivot_df[plant].values
            bar_positions = [x + offsets[plant_idx] for x in x_positions]
            bars = ax.bar(bar_positions, y_values, width=width, label=plant)
            for bar in bars:
                height = bar.get_height()
                if pd.notna(height):
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        height + 0.01,
                        f"{height:.3f}",
                        ha="center",
                        va="bottom",
                        fontsize=score_fontsize,
                        rotation=score_rotation,
                    )

    ax.set_xticks(list(x_positions))
    ax.set_xticklabels(model_order, rotation=45, ha="right")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel(metric.upper())
    plt.xlabel("Model")
    plt.ylim(0, 1.0)
    plt.title(title)
    plt.grid(axis="y", linestyle="--", alpha=0.35)
    plt.legend(title="Plant", ncol=2, fontsize=8)

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

    return output_path


def plot_metric_per_plant(
    df,
    metric="accuracy",
    output_file="figures/results_plant_accuracy.png",
    title="Plant Model Accuracy",
    score_fontsize=8,
    score_rotation=0,
):
    """Create one bar chart per plant group and return saved paths."""
    if metric not in df.columns:
        raise ValueError(f"Input metrics must include a '{metric}' column.")

    work_df = df.copy()
    if "file" in work_df.columns:
        work_df["plant"] = work_df["file"].map(extract_plant_name)
    elif "plant" not in work_df.columns:
        work_df["plant"] = "all"

    out_base = Path(output_file)
    out_base.parent.mkdir(parents=True, exist_ok=True)

    saved_paths = []
    for plant in sorted(work_df["plant"].dropna().unique().tolist()):
        plant_df = work_df[work_df["plant"] == plant]
        agg = (
            plant_df.groupby("model", as_index=False)[metric]
            .mean()
            .sort_values(metric, ascending=False)
        )

        plt.figure(figsize=(12, 5))
        bars = plt.bar(agg["model"], agg[metric], color="#2f7f5f")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel(metric.upper())
        plt.xlabel("Model")
        plt.ylim(0, 1.0)
        plt.title(f"{title} - {plant.title()}")
        plt.grid(axis="y", linestyle="--", alpha=0.35)

        for bar in bars:
            height = bar.get_height()
            if pd.notna(height):
                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    height + 0.01,
                    f"{height:.3f}",
                    ha="center",
                    va="bottom",
                    fontsize=score_fontsize,
                    rotation=score_rotation,
                )

        out_path = out_base.with_name(f"{out_base.stem}_{plant}{out_base.suffix}")
        plt.tight_layout()
        plt.savefig(out_path, dpi=300)
        plt.close()
        saved_paths.append(out_path)

    return saved_paths


def main():
    parser = argparse.ArgumentParser(description="Plot metric figure from plant metrics summary files.")
    parser.add_argument(
        "--metrics-file",
        default=None,
        help="Single metrics_summary.csv path, e.g. results_plant/<model>/metrics_summary.csv",
    )
    parser.add_argument(
        "--results-root",
        default="results_plant",
        help="Root folder to scan for */metrics_summary.csv when --metrics-file is not given",
    )
    parser.add_argument(
        "--output-file",
        default="figures/results_plant_accuracy.png",
        help="Where to save the figure",
    )
    parser.add_argument(
        "--metric",
        default="accuracy",
        choices=["accuracy", "precision", "recall", "f1"],
        help="Metric column to plot",
    )
    parser.add_argument(
        "--style",
        default="bars",
        choices=["bars", "points"],
        help="Plot style: grouped bars or points",
    )
    parser.add_argument(
        "--score-fontsize",
        type=int,
        default=8,
        help="Font size for score labels shown on bars",
    )
    parser.add_argument(
        "--score-rotation",
        type=float,
        default=0,
        help="Rotation (degrees) for score labels; use 0 for horizontal text",
    )
    parser.add_argument(
        "--separate-per-plant",
        action="store_true",
        help="Generate one figure per plant instead of a single grouped figure",
    )
    parser.add_argument("--title", default="Plant Model Accuracy", help="Plot title")

    args = parser.parse_args()

    df = collect_metrics(metrics_file=args.metrics_file, results_root=args.results_root)
    if args.separate_per_plant:
        output_paths = plot_metric_per_plant(
            df,
            metric=args.metric,
            output_file=args.output_file,
            title=args.title,
            score_fontsize=args.score_fontsize,
            score_rotation=args.score_rotation,
        )
        for path in output_paths:
            print(f"Saved figure: {path}")
    else:
        output_path = plot_metric_figure(
            df,
            metric=args.metric,
            output_file=args.output_file,
            title=args.title,
            style=args.style,
            score_fontsize=args.score_fontsize,
            score_rotation=args.score_rotation,
        )

        print(f"Saved figure: {output_path}")


if __name__ == "__main__":
    main()
