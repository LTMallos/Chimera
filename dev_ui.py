import tkinter as tk
from tkinter import filedialog, messagebox
from ipa_parser import IPAParser
from apk_parser import APKParser
from translator_core import TranslatorCore
import os

class ChimeraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chimera GUI — Cross-Platform Dev Tool")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        self.translator = TranslatorCore()
        self.file_type = None

        self.title_label = tk.Label(root, text="🧬 Chimera Dev GUI", font=("Helvetica", 22), fg="white", bg="#1e1e1e")
        self.title_label.pack(pady=20)

        self.load_button = tk.Button(root, text="📂 Load .ipa or .apk", font=("Helvetica", 14), command=self.load_file, bg="#444", fg="white")
        self.load_button.pack(pady=10)

        self.text_box = tk.Text(root, width=80, height=20, bg="#2e2e2e", fg="lime", insertbackground="white")
        self.text_box.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("IPA and APK files", "*.ipa *.apk")])
        if not file_path:
            return

        ext = os.path.splitext(file_path)[-1].lower()
        try:
            if ext == ".ipa":
                self.handle_ipa(file_path)
            elif ext == ".apk":
                self.handle_apk(file_path)
            else:
                messagebox.showerror("Invalid File", "Please select a valid .ipa or .apk file.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_ipa(self, path):
        ipa = IPAParser(path)
        ipa.extract_ipa()
        info = ipa.parse_info_plist()
        translation = self.translator.translate_ios_to_android({
            "login_button": info.get("UIElement", "UIButton")
        })
        self.display_output("IPA", info, translation)

    def handle_apk(self, path):
        apk = APKParser(path)
        apk.extract_apk()
        apk.parse_manifest()
        info = apk.manifest_data
        translation = self.translator.translate_android_to_ios({
            "login_button": "Button"
        })
        self.display_output("APK", info, translation)

    def display_output(self, filetype, info, translation):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, f"=== [{filetype} Metadata] ===\n")
        for k, v in info.items():
            self.text_box.insert(tk.END, f"{k}: {v}\n")

        self.text_box.insert(tk.END, "\n=== [Translation] ===\n")
        for k, v in translation.items():
            self.text_box.insert(tk.END, f"{k}: {v}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChimeraGUI(root)
    root.mainloop()
