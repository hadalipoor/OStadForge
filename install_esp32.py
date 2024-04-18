import subprocess
import sys
import os
import platform

def run_command(command):
    """Run a command using subprocess and return the output and error."""
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        return True, result.stdout
    except Exception as e:
        return False, e.__str__()

def is_arduino_cli_installed():
    """Check if Arduino CLI is installed by checking its version."""
    success, _ = run_command(["arduino-cli", "version"])
    if not success:
        os_type = platform.system()
        install_path = "/usr/local/bin" if os_type != "Windows" else os.environ['USERPROFILE'] + "\\ArduinoCLI"
        arduino_cli_path = install_path + "\\arduino-cli"
        success, _ = run_command([arduino_cli_path, "version"])
        return success, arduino_cli_path
    return success, "arduino-cli"

def check_esp32_installed(arduino_cli_path):
    """Check if ESP32 board is already installed."""
    success, output = run_command([arduino_cli_path, "core", "list"])
    if success and "esp32:esp32" in output:
        print("ESP32 board is already installed.")
        return True
    return False

def add_esp32_board_url(arduino_cli_path):
    """Add the ESP32 board manager URL to the Arduino CLI configuration, and install if not already installed."""
    # Check if ESP32 board is already installed
    if check_esp32_installed(arduino_cli_path):
        return True
    
    # Initialize the configuration if needed
    success, output = run_command([arduino_cli_path, "config", "init"])
    if not success:
        print(output)
        return False
    
    # Add the ESP32 board manager URL
    url = "https://dl.espressif.com/dl/package_esp32_index.json"
    success, output = run_command([arduino_cli_path, "config", "add", "board_manager.additional_urls", url])
    if not success:
        print("Failed to add ESP32 board URL:", output)
        return False

    print("Added ESP32 board URL successfully. Proceeding to installation...")
    
    # Install the ESP32 board
    return install_esp32_board(arduino_cli_path)

def install_esp32_board(arduino_cli_path):
    """Install the ESP32 board definitions using Arduino CLI."""
    # Check if ESP32 board is already installed
    if check_esp32_installed(arduino_cli_path):
        return True

    # Update the core index
    success, output = run_command([arduino_cli_path, "core", "update-index"])
    if not success:
        print("Failed to update core index:", output)
        return False
    
    # Install the ESP32 board
    success, output = run_command([arduino_cli_path, "core", "install", "esp32:esp32"])
    if success:
        print("ESP32 board installed successfully.")
    else:
        print("Failed to install ESP32 board:", output)
    return success
