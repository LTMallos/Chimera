import json

class TranslatorCore:
    def __init__(self):
        # Load component match rules
        with open("component_map.json", "r") as f:
            self.component_map = json.load(f)

    def translate_ios_to_android(self, ios_data):
        android_equiv = {}
        for key, value in ios_data.items():
            android_equiv[key] = self.component_map.get("ios_to_android", {}).get(value, f"(?) {value}")
        return android_equiv

    def translate_android_to_ios(self, android_data):
        ios_equiv = {}
        for key, value in android_data.items():
            ios_equiv[key] = self.component_map.get("android_to_ios", {}).get(value, f"(?) {value}")
        return ios_equiv

    def display_translation(self, data, target="android"):
        translated = self.translate_ios_to_android(data) if target == "android" else self.translate_android_to_ios(data)
        print(f"\n=== Translated Components ({'iOS → Android' if target == 'android' else 'Android → iOS'}) ===")
        for key, val in translated.items():
            print(f"{key}: {val}")
