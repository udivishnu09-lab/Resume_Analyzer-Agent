import pdfplumber


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract all text from an uploaded PDF file.
    Returns the full text as a string.
    """
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text.strip():
            return "ERROR: Could not extract text from PDF. Make sure it is not a scanned image."

        return text.strip()

    except Exception as e:
        return f"ERROR reading PDF: {str(e)}"
