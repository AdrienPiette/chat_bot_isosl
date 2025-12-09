from ingestion.fonctions_extraction import extract_text_pdf

pdf_path = "data/pdf/Gestion des Lits.pdf"

pages = extract_text_pdf(pdf_path) 

print(f"Number of pages extracted: {len(pages)}")
print("Content of the first page:")
print(pages[0])