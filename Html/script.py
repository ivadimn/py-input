import requests
import re

# req = requests.get("http://localhost:5000")
# text = req.text
# print(text)

s = 'Текущий счёт,40817813206170024534,RUR,27.03.17,CRD_5F46FY,548673++++++1028    10502864\RUS\PUSHKINO\ZOOMAGAZIN 4            27.03.17 24.03.17      2176.50  RUR (Apple Pay-7666) MCC5995,0,"2176,5"'
ff = re.findall('"([0-9]+,[0-9]{1,2})"', s)
print(ff)