import json
import requests
import os
import zipfile
import shutil
from urllib.parse import urlparse
from pathlib import Path
import platform

def download_and_extract(url, extract_to):
    
    """Download a zip file and extract it to a specified directory."""
    response = requests.get(url)
    zip_path = extract_to / urlparse(url).path.split('/')[-1]
    with open(zip_path, 'wb') as file:
        file.write(response.content)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)

def download_libraries():
    url = "https://raw.githubusercontent.com/hadalipoor/OStadForge/main/prerequisties.json"
    response = requests.get(url)
    data = json.loads(response.text)

    # Determine the Arduino libraries directory based on the OS
    if platform.system() == "Windows":
        libraries_dir = Path(os.getenv('USERPROFILE'), 'Documents', 'Arduino', 'libraries')
    else:  # Assuming Linux/Mac
        libraries_dir = Path(os.getenv('HOME'), 'Arduino', 'libraries')

    # Ensure the directory exists
    libraries_dir.mkdir(parents=True, exist_ok=True)

    existing_libraries = {d.name.lower(): d for d in libraries_dir.iterdir() if d.is_dir()}
     
    # Download and extract each library only if not already present
    for library in data["libraries"]:
        lib_name = library["Name"].lower()  # Normalize the library name to lower case
        library_found = any(lib_name in folder_name for folder_name in existing_libraries)
        
        if library_found:
            print(f"Library {library['Name']} already exists, skipping download.")
            continue
        
        print(f"Downloading and extracting {library['Name']}...")
        download_and_extract(library["Link"], libraries_dir)

    return True