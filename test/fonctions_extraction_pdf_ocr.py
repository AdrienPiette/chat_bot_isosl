import fitz # PyMuPDF
import pytesseract   # OCR
from PIL import Image
import io

# path = "C:/dev/chat_bot_isosl/data/pdf/Gestion des Lits.pdf" par exemple

def extract_text_pdf(path):
    doc = fitz.open(path)
    pages_text = []
    for page in doc:
        text = page.get_text("text")
        pages_text.append(text)
    doc.close()
    return pages_text

# path tesseract : "C:\Program Files\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_pdf_pages_text_with_ocr(path):
    doc = fitz.open(path)
    pages_text = []

    for page in doc:
        # 1) Texte numérique classique
        digital_text = page.get_text("text")

        # 2) Rendu de la page en image (bitmap)
        pix = page.get_pixmap()          # image brute
        img_bytes = pix.tobytes("png")   # on convertit en PNG en mémoire
        img = Image.open(io.BytesIO(img_bytes))

        # 3) OCR sur l'image
        ocr_text = pytesseract.image_to_string(img, lang="fra")  # ou "eng", ou "fra+eng" si mix

        # 4) Combiner les deux
        combined = digital_text + "\n\n[OCR_SCREENSHOTS]\n" + ocr_text

        pages_text.append(combined)

    doc.close()
    return pages_text



def extract_pdf_pages_structured(path):
    doc = fitz.open(path)
    pages = []

    page_number = 1

    for page in doc:
        # 1) Texte numérique classique
        digital_text = page.get_text("text")

        # 2) Rendu image -> OCR
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_bytes))
        ocr_text = pytesseract.image_to_string(img, lang="fra")

        # 3) On stocke séparément ce qui vient du PDF et ce qui vient de l'OCR
        page_data = {
            "page_number": page_number,
            "digital": digital_text,
            "ocr": ocr_text,
        }

        pages.append(page_data)
        page_number += 1

    doc.close()
    return pages

def pages_to_markdown_simple(pages, title):
    """
    Construit une chaîne Markdown simple à partir d'une liste de pages structurées.

    pages : liste de dicts avec "page_number", "digital", "ocr"
    title : titre global du document
    """
    lines = []

    # Titre principal
    lines.append("# " + title)
    lines.append("")  # ligne vide

    for page in pages:
        num = page["page_number"]
        digital = page["digital"]
        ocr = page["ocr"]

        # Titre de page
        lines.append("## Page " + str(num))
        lines.append("")
        lines.append(digital.strip())
        lines.append("")

        # Si tu veux garder l'OCR brut mais séparé
        if ocr.strip():
            lines.append("### OCR brut")
            lines.append("")
            lines.append(ocr.strip())
            lines.append("")

    # On rejoint toutes les lignes par des sauts de ligne
    markdown = "\n".join(lines)
    return markdown
