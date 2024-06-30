import requests
import os
import re

if __name__ == "__main__":

    urls = {
        "https://phongpublicaccount.blob.core.windows.net/phong-school-app/augmented.pth": "augmented.pth",
        "https://phongpublicaccount.blob.core.windows.net/phong-school-app/model_brand.pt": "model_brand.pt",
        "https://phongpublicaccount.blob.core.windows.net/phong-school-app/model_object.pt": "model_object.pt",
        "https://phongpublicaccount.blob.core.windows.net/phong-school-app/standard.pth": "standard.pth",
    }
    local_directory = "weights/"
    for url,file_name in urls.items():
        print(f"Downloading {file_name} from {url}")
        # Ensure the local directory exists
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)
        # Full local path to save the file
        local_path = os.path.join(local_directory, file_name)
        # Download the blob
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded the blob to {local_path}")
        else:
            print(f"Failed to download the blob. Status code: {response.status_code}")
