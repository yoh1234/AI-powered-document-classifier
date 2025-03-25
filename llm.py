from logger import get_logger
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY"),
logger = get_logger("llm")

def analyze_document(text):
    logger.info("Calling LLM...")
    prompt = f"""Extract structured info from this text:\n{text}"""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response['choices'][0]['message']['content']
    logger.info(f"LLM response: {content}")
    
    try:
        return eval(content)
    except:
        logger.warning("Failed to parse LLM response")
        return {"error": "LLM returned invalid output"}