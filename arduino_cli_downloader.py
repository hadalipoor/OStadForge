import subprocess
import requests
import os
import sys
import platform

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

def install_arduino_cli(binary_content, os_type):
    """Install arduino-cli binary and add it to the system PATH."""
    install_path = "/usr/local/bin" if os_type != "Windows" else os.environ['USERPROFILE'] + "\\ArduinoCLI"
    if not os.path.exists(install_path):
        os.makedirs(install_path)
    binary_path = os.path.join(install_path, "arduino-cli")
    
    with open(binary_path, 'wb') as binary_file:
        binary_file.write(binary_content)

    if os_type != "Windows":
        os.chmod(binary_path, 0o755)  # Make it executable

    # Adding to PATH
    if os_type == "Windows":
        subprocess.run(['setx', 'PATH', f"%PATH%;{install_path}"], shell=True)
    else:
        profile_script = os.path.expanduser("~/.bashrc")
        with open(profile_script, "a") as bashrc:
            bashrc.write(f'\nexport PATH="$PATH:{install_path}"\n')

    return True
