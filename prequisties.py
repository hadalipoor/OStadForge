import platform
import arduino_cli_downloader
import download_libraries
import install_esp32


def initialize_arduino_cli():
    installed, arduino_cli_path = install_esp32.is_arduino_cli_installed()
    if installed:
        print("Arduino CLI is already installed.")
        return True, arduino_cli_path

    print("Downloading Arduino CLI...")
    success, result = arduino_cli_downloader.download_arduino_cli()
    if not success:
        print("Download failed:", result)
        return False, arduino_cli_path

    print("Installing Arduino CLI...")
    os_type = platform.system()
    success, arduino_cli_path = arduino_cli_downloader.install_arduino_cli(result, os_type)
    if not success:
        print("Installation failed.")
        return False, arduino_cli_path

    print("Arduino CLI installed successfully.")
    return True, arduino_cli_path

def initialize():
    print("Initializing Arduino-CLI ...")
    success, arduino_cli_path = initialize_arduino_cli()
    if not success:
        print("Initializing Arduino-CLI failed.")
        return False
    
    if install_esp32.add_esp32_board_url(arduino_cli_path) and install_esp32.install_esp32_board(arduino_cli_path):
        print("ESP32 board setup completed successfully.")
    else:
        print("ESP32 board setup failed.")

    print("Downloading Prerequisites Libraries ...")
    success = download_libraries.download_libraries()
    if not success:
        print("Download Prerequisites failed.")
        return False

    return True