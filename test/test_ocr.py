from chat_bot_isosl.test.fonctions_extraction_pdf_ocr import extract_text_pdf

pdf_path = "data/pdf/Gestion des Lits.pdf"

pages = extract_text_pdf(pdf_path) 

print(f"Number of pages extracted: {len(pages)}")
print("Content of the first page:")
print(pages[0])


from chat_bot_isosl.test.fonctions_extraction_pdf_ocr import extract_pdf_pages_text_with_ocr

pdf_path = "data/pdf/Gestion des Lits.pdf"

text = extract_pdf_pages_text_with_ocr(pdf_path)

print("Extracted text from image-based PDF:")
print(text)

from chat_bot_isosl.test.fonctions_extraction_pdf_ocr import extract_pdf_pages_structured

pdf_path = "data/pdf/Gestion des Lits.pdf"

pages = extract_pdf_pages_structured(pdf_path)

print("Nombre de pages :", len(pages))
print("---- Page 1 ----")
print("Numéro de page :", pages[0]["page_number"])
print("\n--- DIGITAL ---\n")
print(pages[0]["digital"][:800])  # 800 premiers caractères
print("\n--- OCR ---\n")
print(pages[0]["ocr"][:800])



# md génération script

from pathlib import Path

from chat_bot_isosl.test.fonctions_extraction_pdf_ocr import extract_pdf_pages_structured
from chat_bot_isosl.test.fonctions_extraction_pdf_ocr import pages_to_markdown_simple

# 1) Chemin du PDF source
pdf_path = "data/pdf/Gestion des Lits.pdf"

# 2) Extraction structuré (digital + ocr)
pages = extract_pdf_pages_structured(pdf_path)

# 3) Construire le markdown
title = "Gestion des lits - Brouillon OCR"
md_text = pages_to_markdown_simple(pages, title)

# 4) Sauvegarder dans un fichier .md
output_path = Path("data/docs_markdown/gestion_lits_ocr.md")
output_path.write_text(md_text, encoding="utf-8")

print("Markdown généré :", output_path)
