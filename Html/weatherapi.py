import requests

req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=e2405fa3b312d3a3398dad552d59f23f")
text = req.text
print(text)