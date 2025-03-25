from flask import Flask, request, jsonify
from ocr import extract_text
from llm import analyze_document
from logger import get_logger
from cache import get_file_hash, cache_exists, load_cache, save_cache

app = Flask(__name__)
logger = get_logger("flask-app")

@app.route('/')
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        logger.warning("No file uploaded")
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_hash = get_file_hash(file)
    logger.info(f"File hash: {file_hash}")

    if cache_exists(file_hash):
        logger.info("Cache hit!")
        return jsonify(load_cache(file_hash))

    logger.info("Cache miss — running OCR and LLM")
    try:
        text = extract_text(file)
        result = analyze_document(text)

        save_cache(file_hash, result)
        logger.info("Result cached")
        return jsonify(result)

    except Exception as e:
        logger.exception("Error during processing")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)