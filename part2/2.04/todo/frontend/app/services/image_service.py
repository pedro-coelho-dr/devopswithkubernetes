import os
import time
import requests

IMAGE_CACHE_PATH = "/usr/src/app/data/image.jpg"
IMAGE_CACHE_DIR = os.path.dirname(IMAGE_CACHE_PATH)
IMAGE_REFRESH_INTERVAL = 60

def get_cached_image():
    os.makedirs(IMAGE_CACHE_DIR, exist_ok=True)

    if os.path.exists(IMAGE_CACHE_PATH):
        image_age = time.time() - os.path.getmtime(IMAGE_CACHE_PATH)
        if image_age <= IMAGE_REFRESH_INTERVAL:
            return IMAGE_CACHE_PATH
    fetch_new_image()
    return IMAGE_CACHE_PATH

def fetch_new_image():
    response = requests.get("https://picsum.photos/600", stream=True)
    with open(IMAGE_CACHE_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)
