import logging
import os

def get_logger(name="app", log_file="logs/app.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Ensure logs/ directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # File handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s - %(message)s')

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger