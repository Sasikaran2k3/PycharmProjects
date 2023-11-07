import requests

API_URL = "https://api-inference.huggingface.co/models/suno/bark-small"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


audio_bytes = query({
    "inputs": "The answer to the universe is 42",
})

print(audio_bytes)
