import fitz
import glob
import os

pdf_files = glob.glob(r"c:\Users\boudk\source\repos\S5-University-TDs\**\*.pdf", recursive=True)

for pdf_path in pdf_files:
    txt_path = pdf_path + ".txt"
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted {pdf_path}")
    except Exception as e:
        print(f"Failed to extract {pdf_path}: {e}")
