from logger import get_logger
import easyocr
import tempfile

reader = easyocr.Reader(['en'])
logger = get_logger("ocr")

def extract_text(file):
    logger.info("Running OCR")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        file.save(tmp.name)
        result = reader.readtext(tmp.name, detail=0)
        text = ' '.join(result)
        logger.info(f"OCR result: {text[:100]}...")
        return text