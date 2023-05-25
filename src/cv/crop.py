import requests

url = "http://localhost:8000/upload-image"
files = {"image": open("dinho.jpg", "rb")}
response = requests.post(url, files=files)

print(response.json())