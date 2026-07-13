#!/bin/bash

# Rosales
python src/data_preparation/make_balanced_dataset.py \
  --input_csv data/rosales_taxa_with_current_names_all.csv \
  --output_csv data/balanced_synonym_rosales_dataset.csv \
  --legacy_col oldSpeciesCanonicalName \
  --accepted_col species \
  --taxon_id_col key

# Fabales
python src/data_preparation/make_balanced_dataset.py \
  --input_csv data/fabales_taxa_with_current_names_all.csv \
  --output_csv data/balanced_synonym_fabales_dataset.csv \
  --legacy_col oldSpeciesCanonicalName \
  --accepted_col species \
  --taxon_id_col key

# Lamiales
python src/data_preparation/make_balanced_dataset.py \
  --input_csv data/lamiales_taxa_with_current_names_all.csv \
  --output_csv data/balanced_synonym_lamiales_dataset.csv \
  --legacy_col oldSpeciesCanonicalName \
  --accepted_col species \
  --taxon_id_col key

# # Poales
# python src/data_preparation/make_balanced_dataset.py \
#   --input_csv data/poales_taxa_with_current_names_all.csv \
#   --output_csv data/balanced_synonym_poales_dataset.csv \
#   --legacy_col oldSpeciesCanonicalName \
#   --accepted_col species \
#   --taxon_id_col key

# # Coleus
# python src/data_preparation/make_balanced_dataset.py \
#   --input_csv data/coleus_taxa_with_current_names_all.csv \
#   --output_csv data/balanced_synonym_coleus_dataset.csv \
#   --legacy_col oldSpeciesCanonicalName \
#   --accepted_col species \
#   --taxon_id_col key