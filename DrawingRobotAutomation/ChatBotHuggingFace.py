import requests

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response


output = query({
    "inputs": "what is ethical hacking? give reply in 10 lines",
})
if output.status_code == 200:
    print(output.json())