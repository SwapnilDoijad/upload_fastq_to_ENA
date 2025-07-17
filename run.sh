python3 scripts/create_manifest.py \
    -f test_data \
    -s PRJEB12345 \
    -i "Illumina NovaSeq 6000"

python3 scripts/ena_upload.py \
  -f test_data \
  -u Webin-71043 \
  -p Veolab_2025#
