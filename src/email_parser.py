from collections import defaultdict
import tkinter as tk
from tkinter import filedialog
from email.parser import BytesParser
from email import policy

def load_and_parse_eml():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select .eml file",
        filetypes=[("EML files", "*.eml")]
    )

    if file_path:
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)

        header_dict = defaultdict(list)
        for key, value in msg.items():
            header_dict[key].append(value)

        return header_dict
    else:
        print("File was not selected!")
        return None

header_dict = load_and_parse_eml()

if header_dict:
    for key, value in header_dict.items():
        print(f"{key}: {value}")