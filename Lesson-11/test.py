import re
# 1. чтение изфайла
print("----------------- Анализируемый текст ")
with open("text.txt", "r") as f:
    text = f.read()
print(text)
print("-------------------------------------------------")
# 4. Отберите все ссылки.
links = re.findall("([\w\./]+/\w+|[a-z0-9\.]{4,}\.{1}[ru|com|net|org]+)", text)
#links = re.findall("[\w\./]+/\w+", text)
print("---------------------Ссылки на ресурсы")
print(links)