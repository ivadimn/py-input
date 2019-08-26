import re
# 1. чтение изфайла
print("----------------- Анализируемый текст ")
with open("text.txt", "r") as f:
    text = f.read()
print(text)
print("-------------------------------------------------")

# 2. разбивание на предложения
print("----------------Предложения")
sentences = re.split("[!\?\.]\s+", text)
for s in sentences:
    print(s)
print("-------------------------------------------------")

# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
def sort_col(li):
    return li[1]


words = re.findall("\w{4,}", text)
words_set = set(words)
word_str = " ".join(words)

list_frequent = []
for word in words_set:
    wl = re.findall(word, word_str)
    list_frequent.append((word, len(wl)))

list_frequent = sorted(list_frequent, key=sort_col)
print("------------------- 10 самых часто встречающихся слов из 4 и более букв")
print(list(reversed(list_frequent[-10:])))
print("----------------------------------------------------------------------------------")

# 4. Отберите все ссылки.
links = re.findall("[\w\./]+/\w+", text)
print("---------------------Ссылки на ресурсы")
print(links)

# 5 Ссылки на страницы какого домена встречаются чаще всего
print("-----------------------------------------------------------")
domen_frequent = []
domens = [domen[:domen.find("/")] for domen in links]
domens_set = set(domens)
domens_str = " ".join(domens)
for domen in domens_set:
    domen_frequent.append((domen, len(re.findall(domen, domens_str))))

print("Самый часто встречающийся ресурс : ", max(domen_frequent, key=sort_col))

#6 Замените все ссылки на текст «Ссылка отобразится после регистрации».
print("------------------------ Текст после замены ссылок")
changed_text = re.sub("[\w\./]+/\w+", "Ссылка отобразится после регистрации", text)
print(changed_text)