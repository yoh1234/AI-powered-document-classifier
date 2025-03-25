import os
import hashlib
import json
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL)

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_file_hash(file_obj):
    file_obj.seek(0)
    hasher = hashlib.sha256()
    while chunk := file_obj.read(8192):
        hasher.update(chunk)
    file_obj.seek(0)
    return hasher.hexdigest()

def cache_exists(hash_key):
    return os.path.exists(os.path.join(CACHE_DIR, f"{hash_key}.json"))

def load_cache(hash_key):
    with open(os.path.join(CACHE_DIR, f"{hash_key}.json"), "r") as f:
        return json.load(f)

def save_cache(hash_key, data):
    with open(os.path.join(CACHE_DIR, f"{hash_key}.json"), "w") as f:
        json.dump(data, f)