#!/bin/bash

echo "📦 Cloning and running upload_fastq_to_ENA..."

# Clone the repo if not already cloned (optional — for external use)
# git clone https://github.com/SwapnilDoijad/upload_fastq_to_ENA.git
# cd upload_fastq_to_ENA

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the main script (example)
python upload_to_ena.py --help
