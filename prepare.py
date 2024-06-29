import requests
import os
import re

DRIVE_LINK = "https://drive.google.com/file/d/13S-KMWrQAHwoaeeMaqxFhht-PwoGUW1T/view?usp=drive_link"

def extract_file_id(drive_link):
    # Example drive link: https://drive.google.com/file/d/13S-KMWrQAHwoaeeMaqxFhht-PwoGUW1T/view?usp=drive_link
    pattern = r"/d/([a-zA-Z0-9_-]+)"
    match = re.search(pattern, drive_link)
    if match:
        return match.group(1)
    else:
        return None

def download_file_from_google_drive(file_id, destination):
    URL = "https://drive.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    total_size = int(response.headers.get('content-length', 0))

    # Extract original filename from content disposition header if available
    content_disposition = response.headers.get('content-disposition')
    if content_disposition:
        # Extract filename using regex
        filename = re.findall('filename="(.+)"', content_disposition)
        if filename:
            destination = os.path.join(os.path.dirname(destination), filename[0])

    # Download the file and show progress
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Extract the file ID
file_id = extract_file_id(DRIVE_LINK)

# Function to download the file with its original name
def download_file_with_original_name(file_id, output_folder):
    # Download the file from Google Drive
    output_path = os.path.join(output_folder, '')  
    download_file_from_google_drive(file_id, output_path)

    # Get the filename from the output path
    filename = os.path.basename(output_path)

    return os.path.join(output_folder, filename)

# Folder where the file will be saved
output_folder = "weights/"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Download the file with its original name
downloaded_file_path = download_file_with_original_name(file_id, output_folder)

print(f"Download completed. File saved to: {downloaded_file_path}")