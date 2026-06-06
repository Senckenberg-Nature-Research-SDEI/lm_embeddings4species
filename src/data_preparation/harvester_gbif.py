# pip install requests pandas

import argparse
import time
import requests
import pandas as pd
from tqdm import tqdm
GBIF_BASE = "https://api.gbif.org/v1"
LEPIDOPTERA_KEY = 797


def paged_get(url, params=None):
    params = params or {}
    limit = 1000
    offset = 0
    results = []
    print(f"Fetching data from: {url} with params: {params}")
    while offset <= limit:  # safety limit to prevent infinite loops
        query = dict(params, limit=limit, offset=offset)
        r = requests.get(url, params=query, timeout=60)
        r.raise_for_status()
        data = r.json()
        print(f"  Retrieved {len(data.get('results', []))} records (offset: {offset})")
        results.extend(data.get("results", []))

        if data.get("endOfRecords", True):
            break

        offset += limit
        time.sleep(0.1)
        print(f"  Next offset: {offset}")

    print(f"Finished fetching data. Total records: {len(results)}")
    return results


def get_children(parent_key):
    print(f"Fetching children of taxon key: {parent_key}")
    return paged_get(f"{GBIF_BASE}/species/{parent_key}/children")


def get_synonyms(taxon_key):
    return paged_get(f"{GBIF_BASE}/species/{taxon_key}/synonyms")


def get_all_descendants(root_key):
    all_taxa = []
    stack = [root_key]
    print(f"Starting traversal from root taxon key: {root_key}")
    while stack:
        parent_key = stack.pop()
        children = get_children(parent_key)
        print(f"Found {len(children)} children for taxon key {parent_key}")

        for child in children:
            all_taxa.append(child)
            print(f"  - {child.get('scientificName')} (key: {child['key']}, numDescendants: {child.get('numDescendants', 0)})")
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
    print(f"Starting with root taxon key: {args.root_key}")
    taxa = get_all_descendants(args.root_key)
    rows = []
    print(f"Total taxa found: {len(taxa)}")
    for i, taxon in enumerate(tqdm(taxa, start=1, desc="Processing taxa")):
        key = taxon["key"]
        print(f"{i}/{len(taxa)}: {taxon.get('scientificName')}")

        synonyms = get_synonyms(key)

        old_names = sorted({
            s.get("scientificName")
            for s in synonyms
            if s.get("scientificName")
        })
        print("  Old names:", old_names)

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
        # print("  Old names:", old_names)
    print("Finished processing all taxa. Saving to CSV...")
    df = pd.DataFrame(rows)
    df.to_csv(args.out, index=False)

    print("Saved:", args.out)
    print("Number of taxa:", len(df))


if __name__ == "__main__":
    main()