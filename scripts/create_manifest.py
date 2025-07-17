import os
import argparse

def generate_manifest(fastq_folder, study_accession, instrument_model):
    output_manifest = "ena_upload.manifest"
    files = sorted(f for f in os.listdir(fastq_folder) if f.endswith(".fastq.gz") or f.endswith(".fq.gz"))

    # Group files by sample name prefix
    paired_samples = {}
    for file in files:
        base = file.split("_")[0]  # assumes sample1_1.fastq.gz, sample1_2.fastq.gz
        if base not in paired_samples:
            paired_samples[base] = []
        paired_samples[base].append(file)

    with open(output_manifest, "w") as out:
        out.write(f"STUDY\t{study_accession}\n\n")

        for idx, (sample_name, sample_files) in enumerate(paired_samples.items(), start=1):
            sample_files = sorted(sample_files)
            sample_accession = f"SAMEA_FAKE_{idx}"  # replace with real SAMEA accessions if you have them

            out.write(f"SAMPLE\t{sample_accession}\n")
            out.write(f"NAME\trun_{sample_name}\n")
            out.write(f"PLATFORM\tILLUMINA\n")
            out.write(f"INSTRUMENT_MODEL\t{instrument_model}\n")
            for fq in sample_files:
                out.write(f"FASTQ\t{fq}\n")
            out.write("\n")

    print(f"Manifest written to '{output_manifest}' with {len(paired_samples)} sample(s).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate ENA Webin-CLI manifest file from FASTQ files.")
    parser.add_argument('-f', '--fastq-folder', required=True, help="Path to folder with FASTQ files.")
    parser.add_argument('-s', '--study-accession', required=True, help="ENA Study accession (e.g., PRJEB12345).")
    parser.add_argument('-i', '--instrument-model', required=True, help="Sequencing instrument model (e.g., Illumina NovaSeq 6000).")

    args = parser.parse_args()

    generate_manifest(
        fastq_folder=args.fastq_folder,
        study_accession=args.study_accession,
        instrument_model=args.instrument_model
    )
