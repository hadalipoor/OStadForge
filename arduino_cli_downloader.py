import subprocess
import requests
import os
import sys
import platform
import zipfile
import tarfile

def is_tool_installed(name):
    """Check if tool is installed by attempting to call it."""
    try:
        subprocess.run([name, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def download_arduino_cli():
    """Download the arduino-cli binary for the correct OS."""
    os_type = platform.system()
    os_arch = '64bit' if platform.machine().endswith('64') else '32bit'
    base_url = "https://downloads.arduino.cc/arduino-cli/arduino-cli_latest"

    if os_type == "Windows":
        url = f"{base_url}_Windows_{os_arch}.zip"
    elif os_type == "Linux":
        url = f"{base_url}_Linux_{os_arch}.tar.gz"
    elif os_type == "Darwin":  # macOS
        url = f"{base_url}_macOS_{os_arch}.tar.gz"
    else:
        return False, "Unsupported operating system."

    try:
        response = requests.get(url)
        response.raise_for_status()
        return True, response.content
    except requests.RequestException as e:
        return False, str(e)

def extract_files(file_content, file_path, os_type):
    """Extract files from zip or tar.gz based on OS."""
    if os_type == "Windows":
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(file_path))
    else:
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(file_path))
    os.remove(file_path)  # Remove the archive after extraction

def install_arduino_cli(binary_content, os_type):
    """Install arduino-cli binary and add it to the system PATH."""
    install_path = "/usr/local/bin" if os_type != "Windows" else os.environ['USERPROFILE'] + "\\ArduinoCLI"
    if not os.path.exists(install_path):
        os.makedirs(install_path)
    binary_path = os.path.join(install_path, f"arduino-cli{'_latest.zip' if os_type == 'Windows' else '_latest.tar.gz'}")
    
    # Write the binary content to a zip or tar.gz file
    with open(binary_path, 'wb') as binary_file:
        binary_file.write(binary_content)

    # Extract the archive
    extract_files(binary_content, binary_path, os_type)

    executable_path = os.path.join(install_path, "arduino-cli")
    if os_type != "Windows":
        os.chmod(executable_path, 0o755)  # Make it executable

    # Adding to PATH
    if os_type == "Windows":
        subprocess.run(['setx', 'PATH', f"%PATH%;{install_path}"], shell=True)
    else:
        profile_script = os.path.expanduser("~/.bashrc")
        with open(profile_script, "a") as bashrc:
            bashrc.write(f'\nexport PATH="$PATH:{install_path}"\n')

    return True, executable_path
