import re
# 1. чтение изфайла
with open("text.txt", "r") as f:
    text = f.read()
print(text)
print("-------------------------------------------------")

# 2. разбивание на предложения
sentences = re.split("[!\?\.]\s+", text)
for s in sentences:
    print(s)
print("-------------------------------------------------")

# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
words = re.findall("(\w{4,}|[\w\./]+/{1}\w+)", text)

print(words)