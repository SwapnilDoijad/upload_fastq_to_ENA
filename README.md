# 📤 Upload FastQ or Fast5 Files to ENA

A lightweight command-line tool for submitting FastQ or Fast5 files to the [European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena/). This script helps automate the process of creating submission manifests and uploading data using ENA's Webin service.

---

## 🔐 Prerequisites

Before using this tool, make sure you have:

- ✅ A **Webin ID** (e.g., `Webin-XXXXX`)
- ✅ A **Webin password**
- ✅ A registered **ENA Study ID** (e.g., `PRJEB12345`)
- ✅ One or more registered **ENA Sample IDs**

> 👉 Not registered yet? [How to Register a Study and Samples](#how-to-register-a-study-and-samples)

---

## ⚙️ Installation & Usage

### 1. Clone the repository

    git clone https://github.com/SwapnilDoijad/upload_fastq_to_ENA.git
    cd upload_fastq_to_ENA

### 2. Create the manifest file
    python3 scripts/create_manifest.py \
        -f my_data \
        -s project_id \
        -i "Illumina NovaSeq 6000"

### 3. Upload files to ENA
    python3 scripts/ena_upload.py \
        -f my_data \
        -u Webin-12345 \
        -p my_password

---
## 📝 How to Register a Study and Samples
  1. Log in to the ENA Webin Portal
    - Visit: https://www.ebi.ac.uk/ena/submit/webin/
    - Use your Webin credentials to log in.

  2. Register a Study
    - Click "Register Study"
    - Fill out the form with:
      - Release date
      - Study name and title
      - Abstract
      - Submit and note the Study Accession, e.g.:

  3. Register Samples
       - Click "Register Sample"
       - Download the sample spreadsheet template.
       - Fill in required metadata for each sample.
       - Upload via the portal to get Sample IDs (e.g., ERS1234567).

---
🧑‍💻 Author
Swapnil Doijad (swapnil.doijad@gmail.com)
GitHub: @SwapnilDoijad

🙋 Support
If you encounter bugs or have feature requests, please open an [issue](https://github.com/SwapnilDoijad/upload_fastq_to_ENA/issues).

---