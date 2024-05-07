import requests

API_URL = "https://api-inference.huggingface.co/models/dima806/chest_xray_pneumonia_detection"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("person3_bacteria_10.jpeg")
print(output)