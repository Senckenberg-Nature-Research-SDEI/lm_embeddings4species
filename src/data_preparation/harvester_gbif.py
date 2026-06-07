# pip install requests pandas tqdm

import argparse
import time
import logging
from pathlib import Path

import requests
import pandas as pd
from tqdm import tqdm
import random
SEED = 42

GBIF_BASE = "https://api.gbif.org/v1"
LEPIDOPTERA_KEY = 797
COLEOPTERA_KEY = 1470

random.seed(SEED)
def setup_logger(log_file, log_level):
    logger = logging.getLogger("gbif_harvester")
    logger.setLevel(getattr(logging, log_level))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def paged_get(url, logger, params=None, sleep=0.1):
    params = params or {}
    limit = 1000
    offset = 0
    results = []

    logger.info("Fetching: %s | params=%s", url, params)

    while offset <= limit:  # safety limit to prevent infinite loops
        query = dict(params, limit=limit, offset=offset)

        try:
            r = requests.get(url, params=query, timeout=60)
            r.raise_for_status()
            data = r.json()
        except requests.RequestException as e:
            logger.error("Request failed: %s | params=%s | error=%s", url, query, e)
            raise

        batch = data.get("results", [])
        results.extend(batch)

        logger.debug("Retrieved %s records at offset %s", len(batch), offset)

        if data.get("endOfRecords", True):
            break

        offset += limit
        time.sleep(sleep)
        print("offset:", offset)
    logger.info("Finished: %s | total=%s", url, len(results))
    return results


def get_children(parent_key, logger):
    return paged_get(
        f"{GBIF_BASE}/species/{parent_key}/children",
        logger=logger,
    )


def get_synonyms(taxon_key, logger):
    return paged_get(
        f"{GBIF_BASE}/species/{taxon_key}/synonyms",
        logger=logger,
    )


def get_all_descendants(root_key, logger):
    all_taxa = []
    stack = [root_key]

    logger.info("Starting traversal from root taxon key: %s", root_key)

    while stack:
        parent_key = stack.pop()
        children = get_children(parent_key, logger)
        if len(children) > 100:
            children = random.sample(children, 100)

        logger.info(
            "Randomly selected %s/%s children for taxon %s",
            len(children),
            min(len(get_children(parent_key, logger)), 100),
            parent_key,
)
        logger.info("Taxon key %s has %s children", parent_key, len(children))

        for child in children:
            all_taxa.append(child)

            if child.get("numDescendants", 0) > 0:
                stack.append(child["key"])
        
    logger.info("Total descendant taxa found: %s", len(all_taxa))
    return all_taxa

def extract_old_species_names(synonyms):
    old_names = []

    for s in synonyms:
        if s.get("rank") != "SPECIES":
            continue

        canonical = s.get("canonicalName")
        if not canonical:
            continue

        old_names.append({
            "oldCanonicalName": canonical,
            "oldScientificName": s.get("scientificName"),
            "oldKey": s.get("key"),
            "oldTaxonomicStatus": s.get("taxonomicStatus"),
            "oldNomenclaturalStatus": "; ".join(s.get("nomenclaturalStatus", [])),
            "oldAuthorship": s.get("authorship"),
            "oldPublishedIn": s.get("publishedIn"),
        })

    return old_names

def main():
    parser = argparse.ArgumentParser(
        description="Download Coleoptera taxa with old species names from GBIF."
    )
    parser.add_argument("--root-key", type=int, default=COLEOPTERA_KEY)
    parser.add_argument("--out", default="coleoptera_taxa_with_old_names.csv")
    parser.add_argument("--log-file", default="gbif_coleoptera_harvester.log")
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )

    args = parser.parse_args()

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)

    logger = setup_logger(args.log_file, args.log_level)

    logger.info("Output file: %s", args.out)
    logger.info("Log file: %s", args.log_file)
    logger.info("Root taxon key: %s", args.root_key)

    taxa = get_all_descendants(args.root_key, logger)

    rows = []

    for taxon in tqdm(taxa, desc="Processing taxa"):
        key = taxon["key"]
        rank = taxon.get("rank")

        # Only species can have old species names
        if rank != "SPECIES":
            continue

        synonyms = get_synonyms(key, logger)
        old_species_infos = extract_old_species_names(synonyms)

        logger.debug(
            "%s | old species names: %s",
            taxon.get("scientificName"),
            old_species_infos,
        )

        for old_info in old_species_infos:
            rows.append({
                "key": key,
                "scientificName": taxon.get("scientificName"),
                "canonicalName": taxon.get("canonicalName"),
                "rank": rank,
                "taxonomicStatus": taxon.get("taxonomicStatus"),
                "kingdom": taxon.get("kingdom"),
                "phylum": taxon.get("phylum"),
                "class": taxon.get("class"),
                "order": taxon.get("order"),
                "family": taxon.get("family"),
                "genus": taxon.get("genus"),
                "species": taxon.get("species"),
                "numDescendants": taxon.get("numDescendants"),

                # Old species-name synonym details
                "oldSpeciesCanonicalName": old_info.get("oldCanonicalName"),
                "oldSpeciesScientificName": old_info.get("oldScientificName"),
                "oldSpeciesKey": old_info.get("oldKey"),
                "oldSpeciesTaxonomicStatus": old_info.get("oldTaxonomicStatus"),
                "oldSpeciesNomenclaturalStatus": old_info.get("oldNomenclaturalStatus"),
                "oldSpeciesAuthorship": old_info.get("oldAuthorship"),
                "oldSpeciesPublishedIn": old_info.get("oldPublishedIn"),
            })

    df = pd.DataFrame(rows)
    df.to_csv(args.out, index=False)

    logger.info("Saved CSV: %s", args.out)
    logger.info("Rows written: %s", len(df))


if __name__ == "__main__":
    main()