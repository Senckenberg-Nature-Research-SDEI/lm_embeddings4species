python src/data_preparation/harvester_gbif.py \
  --root-key 797 \
  --out data/lepidoptera_taxa_with_old_names_all.csv \
  --log-file logs/gbif_lepidoptera_harvester_all.log \
  --log-level INFO

python src/data_preparation/harvester_gbif.py \
  --root-key 1470 \
  --out data/coleoptera_taxa_with_current_names_all.csv \
  --log-file logs/gbif_coleoptera_harvester_all.log \
  --log-level INFO