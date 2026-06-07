python src/data_preparation/make_balanced_dataset.py \
  --input_csv data/only_synonyms_coleop.csv \
  --output_csv data/balanced_synonym_coleop_dataset.csv \
  --legacy_col oldSpeciesCanonicalName \
  --accepted_col species \
  --taxon_id_col key

python src/data_preparation/make_balanced_dataset.py \
  --input_csv data/only_synonyms_lepo.csv \
  --output_csv data/balanced_synonym_lepidoptera_dataset.csv \
  --legacy_col oldSpeciesCanonicalName \
  --accepted_col species \
  --taxon_id_col key