python src/data_preparation/harvester_gbif.py \
  --root-key 5376565 \
  --out data/lepidium_taxa_with_current_names_all.csv \
  --log-file logs/gbif_lepidium_harvester_all.log \
  --log-level INFO

python src/data_preparation/harvester_gbif.py \
  --root-key 1234567 \
  --out data/coleus_taxa_with_current_names_all.csv \
  --log-file logs/gbif_coleus_harvester_all.log \
  --log-level INFO