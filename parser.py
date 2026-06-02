from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_resume(file):

    filename = file.filename.lower()

    # PDF
    if filename.endswith(".pdf"):

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text

    # DOCX
    elif filename.endswith(".docx"):

        doc = Document(file)

        text = ""

        for para in doc.paragraphs:

            text += para.text + " "

        return text

    # TXT
    elif filename.endswith(".txt"):

        return file.read().decode("utf-8")

    # IMAGE FILES
    elif filename.endswith(
        (".jpg", ".jpeg", ".png")
    ):

        image = Image.open(file)

        text = pytesseract.image_to_string(image)

        return text

    return ""