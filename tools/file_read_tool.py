# tools/file_read_tool.py

import fitz  # PyMuPDF

def read_pdf_content(file_path: str) -> str:
    """A simple tool to read the text content of a PDF file."""
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        # Return an error message if the PDF is empty or unreadable
        return text if text.strip() else "Error: No readable text found in the PDF."
    except Exception as e:
        return f"Error reading PDF file: {e}"