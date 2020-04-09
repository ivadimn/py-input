import requests

req = requests.get("http://api.github.com/users/ivadimn/repos")
print(req.text)