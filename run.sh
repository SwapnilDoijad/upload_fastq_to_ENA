# How to Register a Study and Sample
    # 1. Log into the Webin Portal
        # Go to: https://www.ebi.ac.uk/ena/submit/webin/
        # Log in with your Webin account credentials (Webin-xxxxx).
    # 2. Register a Study (https://www.ebi.ac.uk/ena/submit/webin/)
        # Click on "Register Study"
        # Fill in:
            # Release date
            # Study name
            # Short descriptive study title
            # Abstract
            # Submit and note the study accession, you will get something like: 
                # Project	PRJEB94019	6576cdb0-94bf-48c3-981f-189fdcad4a6a
                # Submission	ERA33634919	SUBMISSION-17-07-2025-12:58:10:319
    # 3. Register a Sample (https://www.ebi.ac.uk/ena/submit/webin/)
        # Click on "Register Sample"
        # Download spreadsheet and fill in relevant info

## run
python3 create_manifest.py \
    -f test_data \
    -s PRJEB12345 \
    -i "Illumina NovaSeq 6000"

# python3 ena_upload.py \
#   -f test_data \
#   -u Webin-71043 \
#   -p Veolab_2025#
