import arduino_cli_downloader

def main():
    if arduino_cli_downloader.is_tool_installed("arduino-cli"):
        print("Arduino CLI is already installed.")
        return True

    print("Downloading Arduino CLI...")
    success, result = arduino_cli_downloader.download_arduino_cli()
    if not success:
        print("Download failed:", result)
        return False

    print("Installing Arduino CLI...")
    os_type = platform.system()
    success = arduino_cli_downloader.install_arduino_cli(result, os_type)
    if not success:
        print("Installation failed.")
        return False

    print("Arduino CLI installed successfully.")
    return True

# Example of how to use this script
if __name__ == "__main__":
    main()
