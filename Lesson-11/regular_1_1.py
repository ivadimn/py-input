import re

# Задание №1
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print(text)


# Задание №2

text2 = re.split("\.|!|\?", text)
print('Задание 2:', text2)


# Задание №3

text3 = re.findall("\w{4,}", text)
max_len10 = []
for i in text3:
    max_len10.append((i, text3.count(i)))
print('Задание 3:', sorted(list(set(max_len10)), key=lambda x: x[1])[-10:])


# Задание №4

link = re.compile("\w+\.?\w+\.ru?/?\w+\d?")
links = re.findall(link, text)
print('Задание 4:', links)

# Задание №5

domen = re.compile("\w+\.?\w+\.ru?")
max_domen = [(i, text.count(i)) for i in re.findall(domen, text)]
print('Задание 5 чаще всего встречается ссылка:', sorted(list(set(max_domen)), key=lambda x: x[1])[-1])

# Задание №6

print(re.sub(link, '"Ссылка отобразится после регистрации"', text))