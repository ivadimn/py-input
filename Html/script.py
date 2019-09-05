import requests

req = requests.get("http://localhost:5000")
text = req.text
print(text)