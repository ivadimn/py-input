words = [["собака", "сущ"],
         ["ела", "глагол"],
         ["колбасу", "сущ"],
         ["вечером", "наречие"]]

list_word = []
nelist_word = []

for n in words:
    list_word.append(n[0])
    nelist_word.append(n[1])

class Word:
    text = 'Собака'
    part = 'Сущ'

    def __init__(self, text, part):
        self.text = text
        self.part = part

class Sentence:
    content = [0, 2]
    show = None
    show_parts = None

    def show(self):
        content = self.content
        print(list_word[content[0]] +' '+ list_word[content[1]], '- Вывели слова из массива')
        print(nelist_word[content[0]] +' '+ nelist_word[content[1]], '- Вывели части речи из массива')

result = Word('Капуста', 'сущ')
print(result.text, result.part, '- проверили что экземпляр класса отрабатывает новые значения')
print('*' * 72)

woi = Sentence()
woi.show()














