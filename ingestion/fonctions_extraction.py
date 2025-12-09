import fitz # PyMuPDF

def extract_text_pdf(path):
    doc = fitz.open(path)
    pages_text = []
    for page in doc:
        text = page.get_text("text")
        pages_text.append(text)
    doc.close()
    return pages_text


