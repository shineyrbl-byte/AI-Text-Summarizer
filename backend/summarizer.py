import os
import requests

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_summary(text, length="medium"):

    text = " ".join(text.split())
    text = text[:2000]

    if length == "short":
        max_len = 60
        min_len = 30
    elif length == "long":
        max_len = 200
        min_len = 100
    else:
        max_len = 130
        min_len = 70

    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_len,
            "min_length": min_len,
            "do_sample": False
        }
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result[0]["summary_text"]