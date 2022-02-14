import re

"""
text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

result = re.match("wo", text)
print(result)

result = re.search("wo", text)
print("Функция search: {0}".format(result))
index = text.index(" ", result.start())
print(text[result.start():index])

result = re.findall("wo", text)
print("Функция findall: {0}".format(result))


result = re.sub("wo", "ЗАМЕНА", text)
print("Функция sub: {0}".format(result))
"""

text = "\wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?"

result = re.findall(r"\\wwood\+\?,", text)
print("Функция findall: {0}".format(result))


