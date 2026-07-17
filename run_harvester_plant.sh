#!/bin/bash

# Rosales
python src/data_preparation/harvester_gbif.py \
  --root-key 691 \
  --out data/rosales_taxa_with_current_names_all.csv \
  --log-file logs/gbif_rosales_harvester_all.log \
  --log-level INFO

# Fabales
python src/data_preparation/harvester_gbif.py \
  --root-key 1370 \
  --out data/fabales_taxa_with_current_names_all.csv \
  --log-file logs/gbif_fabales_harvester_all.log \
  --log-level INFO

# Lamiales
python src/data_preparation/harvester_gbif.py \
  --root-key 724 \
  --out data/lamiales_taxa_with_current_names_all.csv \
  --log-file logs/gbif_lamiales_harvester_all.log \
  --log-level INFO


# Poales
python src/data_preparation/harvester_gbif.py \
  --root-key 1369 \
  --out data/poales_taxa_with_current_names_all.csv \
  --log-file logs/gbif_poales_harvester_all.log \
  --log-level INFO
