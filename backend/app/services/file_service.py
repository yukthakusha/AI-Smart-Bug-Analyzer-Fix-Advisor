from pathlib import Path
from PyPDF2 import PdfReader


def extract_text(file_path: str) -> str:

    extension = Path(file_path).suffix.lower()

    if extension in [".txt", ".log"]:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()

    elif extension == ".pdf":
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    else:
        raise ValueError("Unsupported file format.")