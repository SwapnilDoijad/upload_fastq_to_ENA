import argparse
import os
from ftplib import FTP

def upload_files_to_ena(fastq_folder, webin_user, webin_password):
    ftp_server = 'ftp.webin.ebi.ac.uk'
    target_folder_name = "my_ena_data"  # Hardcoded folder name

    print(f"Connecting to ENA FTP server: {ftp_server}")
    try:
        ftp = FTP(ftp_server)
        ftp.login(user=webin_user, passwd=webin_password)
        print("Login successful.")
    except Exception as e:
        print(f"Failed to connect/login: {e}")
        return

    try:
        ftp.cwd(target_folder_name)
        print(f"Changed to existing folder: {target_folder_name}")
    except:
        try:
            ftp.mkd(target_folder_name)
            ftp.cwd(target_folder_name)
            print(f"Created and changed to folder: {target_folder_name}")
        except Exception as e:
            print(f"Failed to create or access target folder: {e}")
            ftp.quit()
            return

    if not os.path.isdir(fastq_folder):
        print(f"Error: The folder '{fastq_folder}' does not exist.")
        ftp.quit()
        return

    files = [f for f in os.listdir(fastq_folder) if os.path.isfile(os.path.join(fastq_folder, f))]
    print(f"Uploading {len(files)} file(s) from '{fastq_folder}' to ENA...")

    for file in files:
        local_path = os.path.join(fastq_folder, file)
        try:
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {file}', f)
            print(f"Uploaded: {file}")
        except Exception as e:
            print(f"Failed to upload {file}: {e}")

    ftp.quit()
    print("ENA FTP session closed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload FASTQ files to ENA FTP server.")
    parser.add_argument('-f', '--fastq-folder', required=True, help="Path to folder containing FASTQ files.")
    parser.add_argument('-u', '--webin-user', required=True, help="ENA Webin username (e.g., Webin-12345).")
    parser.add_argument('-p', '--webin-password', required=True, help="ENA Webin password.")

    args = parser.parse_args()

    upload_files_to_ena(
        fastq_folder=args.fastq_folder,
        webin_user=args.webin_user,
        webin_password=args.webin_password
    )
