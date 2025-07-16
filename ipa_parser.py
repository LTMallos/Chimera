import zipfile
import plistlib
import os

class IPAParser:
    def __init__(self, ipa_path):
        self.ipa_path = ipa_path
        self.extract_path = "extracted_ipa"
        self.info_plist_data = {}

    def extract_ipa(self):
        try:
            with zipfile.ZipFile(self.ipa_path, 'r') as ipa_file:
                ipa_file.extractall(self.extract_path)
            print(f"[+] IPA extracted to '{self.extract_path}'")
        except zipfile.BadZipFile:
            raise Exception("This file is not a valid IPA (bad ZIP format).")
        except Exception as e:
            raise Exception(f"Extraction failed: {e}")

    def find_info_plist(self):
        for root, dirs, files in os.walk(self.extract_path):
            for file in files:
                if file == "Info.plist":
                    return os.path.join(root, file)
        return None

    def parse_info_plist(self):
        plist_path = self.find_info_plist()
        if not plist_path:
            raise Exception("Info.plist not found!")

        with open(plist_path, 'rb') as plist_file:
            self.info_plist_data = plistlib.load(plist_file)
        return self.info_plist_data

    def display_basic_info(self):
        if not self.info_plist_data:
            self.parse_info_plist()

        print("\n=== App Metadata ===")
        print("🧬 App Name:", self.info_plist_data.get("CFBundleName"))
        print("📦 Bundle ID:", self.info_plist_data.get("CFBundleIdentifier"))
        print("🧩 Version:", self.info_plist_data.get("CFBundleShortVersionString"))
        print("🔢 Build:", self.info_plist_data.get("CFBundleVersion"))
