# AI-Powered Document Analyzer (Flask)

This is a simple, production-ready Flask microservice designed to analyze scanned documents such as passports, visas, and IDs. It allows users to upload image files, extract text using OCR, and leverage a Large Language Model (LLM) to understand and summarize the document contents.

## Features

- Upload scanned image files (`.jpg`, `.png`, etc.)
- Extract text using EasyOCR
- Classify and summarize documents using OpenAI GPT
- Redis caching to avoid reprocessing the same document
- REST API endpoint: `/analyze`
- Docker and Docker Compose support
- Unit testing with Python's `unittest`

## Tech Stack

- Python 3.11+
- Flask
- EasyOCR
- OpenAI API
- Redis
- Docker

## Project Structure

.
├── app.py                # Flask app entry point
├── ocr.py                # OCR logic
├── llm.py                # LLM call and formatting
├── cache.py              # Redis cache logic
├── utils.py              # Logging and helper functions
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build config
├── docker-compose.yml    # Compose config for Flask + Redis
├── tests/                # Unit tests
└── README.md             # Project readme

Getting Started (Local Development)

1. Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows use .\venv\Scripts\activate
pip install -r requirements.txt

2. Start Redis

You can either install Redis locally or run it using Docker:

docker run -p 6379:6379 redis

3. Run the Flask App

python app.py

Then go to: http://localhost:5000

4. Test the API Endpoint

You can use curl or Postman to test the /analyze endpoint:

curl -X POST -F "file=@passport.jpg" http://localhost:5000/analyze

Running with Docker

If you'd prefer to run everything in containers:

docker compose up --build

Flask will run at: http://localhost:5000
Redis will run at: localhost:6379

Running Tests

python -m unittest discover tests

Environment Variables

Store your API keys or configuration in a .env file or pass them into the environment:

OPENAI_API_KEY=your-openai-key

Example Output from the LLM

{
  "document_type": "passport",
  "name": "John Doe",
  "country": "USA",
  "expiry_date": "2027-04-15"
}

Next Steps / Roadmap



Contact

Created by Youngsuk Oh. If you have any questions, feedback, or ideas, feel free to reach out or open an issue.