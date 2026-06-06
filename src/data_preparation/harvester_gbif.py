# pip install requests pandas

import argparse
import time
import requests
import pandas as pd

GBIF_BASE = "https://api.gbif.org/v1"
LEPIDOPTERA_KEY = 797


def paged_get(url, params=None):
    params = params or {}
    limit = 1000
    offset = 0
    results = []

    while True:
        query = dict(params, limit=limit, offset=offset)
        r = requests.get(url, params=query, timeout=60)
        r.raise_for_status()
        data = r.json()

        results.extend(data.get("results", []))

        if data.get("endOfRecords", True):
            break

        offset += limit
        time.sleep(0.1)

    return results


def get_children(parent_key):
    return paged_get(f"{GBIF_BASE}/species/{parent_key}/children")


def get_synonyms(taxon_key):
    return paged_get(f"{GBIF_BASE}/species/{taxon_key}/synonyms")


def get_all_descendants(root_key):
    all_taxa = []
    stack = [root_key]

    while stack:
        parent_key = stack.pop()
        children = get_children(parent_key)

        for child in children:
            all_taxa.append(child)

            if child.get("numDescendants", 0) > 0:
                stack.append(child["key"])

    return all_taxa


def main():
    parser = argparse.ArgumentParser(
        description="Download all taxa under Lepidoptera with old scientific names/synonyms from GBIF."
    )
    parser.add_argument("--root-key", type=int, default=LEPIDOPTERA_KEY)
    parser.add_argument("--out", default="lepidoptera_taxa_with_old_names.csv")
    args = parser.parse_args()

    taxa = get_all_descendants(args.root_key)
    rows = []

    for i, taxon in enumerate(taxa, start=1):
        key = taxon["key"]
        print(f"{i}/{len(taxa)}: {taxon.get('scientificName')}")

        synonyms = get_synonyms(key)

        old_names = sorted({
            s.get("scientificName")
            for s in synonyms
            if s.get("scientificName")
        })

        rows.append({
            "key": key,
            "scientificName": taxon.get("scientificName"),
            "canonicalName": taxon.get("canonicalName"),
            "rank": taxon.get("rank"),
            "taxonomicStatus": taxon.get("taxonomicStatus"),
            "kingdom": taxon.get("kingdom"),
            "phylum": taxon.get("phylum"),
            "class": taxon.get("class"),
            "order": taxon.get("order"),
            "family": taxon.get("family"),
            "genus": taxon.get("genus"),
            "species": taxon.get("species"),
            "numDescendants": taxon.get("numDescendants"),
            "oldScientificNames_synonyms": "; ".join(old_names),
        })

    df = pd.DataFrame(rows)
    df.to_csv(args.out, index=False)

    print("Saved:", args.out)
    print("Number of taxa:", len(df))


if __name__ == "__main__":
    main()