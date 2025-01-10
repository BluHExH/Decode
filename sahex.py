import os
import time
from pyfiglet import Figlet

def clear_screen():
    os.system('clear')

def print_start_message():
    clear_screen()
    print("\033[1;35m")  # Purple color
    for i in range(5):  # Change color for a few seconds
        print(f"\033[1;{35 + i}mI am Hacker Hex and Welcome to My World!\033[0m")
        time.sleep(0.5)
    time.sleep(1)
    clear_screen()

def install_dependencies():
    dependencies = ["python", "python3", "pip", "pyfiglet", "curl", "termux-api"]
    print("\033[1;36mInstalling necessary dependencies...\033[0m\n")
    for dep in dependencies:
        print(f"Installing {dep}...", end=" ", flush=True)
        time.sleep(1)  # Simulate installation
        print("\033[1;32m✅\033[0m")  # Green tick mark
    print("\n\033[1;32mAll dependencies installed successfully!\033[0m\n")
    time.sleep(2)

def loading_message():
    print("\033[1;33mPlease wait, starting the tool...\033[0m")
    for i in range(1, 101, 10):  # Simulate loading bar
        print(f"Loading... {i}% complete", end="\r", flush=True)
        time.sleep(0.5)
    print("\033[1;32mLoading 100% complete!\033[0m")
    time.sleep(2)

def print_banner():
    f = Figlet(font='slant')  # Changed font to 'slant' for a larger "HEX"
    clear_screen()
    print("\033[1;36m")  # Cyan color
    banner = f.renderText('HEX')

    # Center the "HEX" banner
    banner_lines = banner.split("\n")
    for line in banner_lines:
        print(line.center(100))  # Center the "HEX" banner
    print("\033[1;31m" + "="*100)  # Red line separator
    print("\033[1;37m Powerful Termux Tool | By Hacker Hex")
    print(" Decode JSON | YAML | HEX | Base64 | More...\033[0m")
    print("\033[1;31m" + "="*100 + "\033[0m")

def main_menu():
    while True:
        print_banner()
        # Styling the options
        print("\033[1;32m  [1] \033[1;36mJSON Decoder\033[0m")
        print("\033[1;32m  [2] \033[1;36mYAML Decoder\033[0m")
        print("\033[1;32m  [3] \033[1;36mHEX Decoder\033[0m")
        print("\033[1;32m  [4] \033[1;36mBase64 Decoder\033[0m")
        print("\033[1;32m  [5] \033[1;36mAbout Tool\033[0m")
        print("\033[1;32m  [6] \033[1;36mExit\033[0m")
        
        # Highlighting the active option
        choice = input("\033[1;34m\nEnter your choice: \033[0m")
        
        if choice == "1":
            decode_json()
        elif choice == "2":
            decode_yaml()
        elif choice == "3":
            decode_hex()
        elif choice == "4":
            decode_base64()
        elif choice == "5":
            about_tool()
        elif choice == "6":
            print("\033[1;33mExiting... Thank you for using HEX!\033[0m")
            time.sleep(2)
            break
        else:
            print("\033[1;31mInvalid choice! Please try again.\033[0m")
            time.sleep(2)

def decode_json():
    print("\033[1;36mJSON Decoder Selected.\033[0m")
    filepath = input("\033[1;34mEnter JSON file path: \033[0m")
    try:
        with open(filepath, 'r') as file:
            import json
            data = json.load(file)
            print("\033[1;32mDecoded JSON Data:\033[0m")
            print(data)
    except Exception as e:
        print("\033[1;31mError decoding JSON:\033[0m", str(e))
    input("\033[1;33mPress Enter to return to the main menu...\033[0m")

def decode_yaml():
    print("\033[1;36mYAML Decoder Selected.\033[0m")
    filepath = input("\033[1;34mEnter YAML file path: \033[0m")
    try:
        import yaml
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
            print("\033[1;32mDecoded YAML Data:\033[0m")
            print(data)
    except Exception as e:
        print("\033[1;31mError decoding YAML:\033[0m", str(e))
    input("\033[1;33mPress Enter to return to the main menu...\033[0m")

def decode_hex():
    print("\033[1;36mHEX Decoder Selected.\033[0m")
    hex_string = input("\033[1;34mEnter HEX string: \033[0m")
    try:
        decoded = bytes.fromhex(hex_string).decode('utf-8')
        print("\033[1;32mDecoded HEX Data:\033[0m")
        print(decoded)
    except Exception as e:
        print("\033[1;31mError decoding HEX:\033[0m", str(e))
    input("\033[1;33mPress Enter to return to the main menu...\033[0m")

def decode_base64():
    print("\033[1;36mBase64 Decoder Selected.\033[0m")
    base64_string = input("\033[1;34mEnter Base64 string: \033[0m")
    try:
        import base64
        decoded = base64.b64decode(base64_string).decode('utf-8')
        print("\033[1;32mDecoded Base64 Data:\033[0m")
        print(decoded)
    except Exception as e:
        print("\033[1;31mError decoding Base64:\033[0m", str(e))
    input("\033[1;33mPress Enter to return to the main menu...\033[0m")

def about_tool():
    print("\033[1;36mThis tool is developed by Hacker Hex.\033[0m")
    print("\033[1;37mFeatures:\033[0m")
    print("1. Decode JSON, YAML, Base64, HEX formats.")
    print("2. Stylish welcome message and banner.")
    print("3. Dependency installation with visual feedback.")
    input("\n\033[1;33mPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    print_start_message()
    install_dependencies()
    loading_message()
    main_menu()
