import zipfile
import os
import xml.etree.ElementTree as ET

class APKParser:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.extract_path = "extracted_apk"
        self.manifest_data = None

    def extract_apk(self):
        if not zipfile.is_zipfile(self.apk_path):
            raise Exception("Not a valid APK file.")

        with zipfile.ZipFile(self.apk_path, 'r') as apk:
            apk.extractall(self.extract_path)

        print(f"[+] APK extracted to '{self.extract_path}'")

    def parse_manifest(self):
        manifest_path = os.path.join(self.extract_path, 'AndroidManifest.xml')
        if not os.path.exists(manifest_path):
            raise Exception("AndroidManifest.xml not found!")

        try:
            tree = ET.parse(manifest_path)
            root = tree.getroot()
            self.manifest_data = root.attrib
        except Exception as e:
            raise Exception(f"Failed to parse AndroidManifest.xml: {e}")

    def display_basic_info(self):
        self.extract_apk()
        self.parse_manifest()

        print("\n=== APK Metadata ===")
        print("📦 Package ID:", self.manifest_data.get('package'))
        print("🔢 Version Code:", self.manifest_data.get('{http://schemas.android.com/apk/res/android}versionCode'))
        print("🧩 Version Name:", self.manifest_data.get('{http://schemas.android.com/apk/res/android}versionName'))
