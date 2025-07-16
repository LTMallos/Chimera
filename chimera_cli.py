from ipa_parser import IPAParser
from apk_parser import APKParser
from translator_core import TranslatorCore
import os

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("""
  ██████╗██╗  ██╗██╗███╗   ███╗███████╗██████╗  █████╗ 
 ██╔════╝██║  ██║██║████╗ ████║██╔════╝██╔══██╗██╔══██╗
 ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝███████║
 ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██║██╝  ██╔══██║
 ╚██████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║ ██║ ██║  ██║
  ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝ ╚═╝ ╚═╝  ╚═╝
          >> Chimera CLI — dev tool <<
    """)

def main():
    clear()
    banner()
    translator = TranslatorCore()

    while True:
        print("\n1. Load and analyze IPA")
        print("2. Load and analyze APK")
        print("3. Quit")
        choice = input("\nEnter choice: ")

        if choice == "1":
            path = input("Enter .ipa file path: ").strip()
            if not os.path.isfile(path):
                print("❌ File not found!")
                continue
            ipa = IPAParser(path)
            ipa.extract_ipa()
            info = ipa.parse_info_plist()
            ipa.display_basic_info()
            translator.display_translation({
                "main_button": info.get("UIElement", "UIButton")  # Dummy example
            }, target="android")

        elif choice == "2":
            path = input("Enter .apk file path: ").strip()
            if not os.path.isfile(path):
                print("❌ File not found!")
                continue
            apk = APKParser(path)
            apk.display_basic_info()
            translator.display_translation({
                "main_button": "Button"
            }, target="ios")

        elif choice == "3":
            print("Goodbye, Chimera dev.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
