class Word:

    def __init__(self, text):
        self.text = text


class Sentence:

    def show(self, w_list):
        sentence = ""
        for index in self.content:
            sentence += w_list[index].text + " "
        print(sentence)

    def show_parts(self, w_list):
        parts = set()
        for index in self.content:
            parts.add(w_list[index].part())
        print(parts)

    def __init__(self, content):
        self.content = content


# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.


class Noun(Word):
    __grammar = "сущ"

    def part(self):
        return "Существительное"


class Verb(Word):
    __grammar = "гл"

    def part(self):
        return "Глагол"


class Conjunction(Word):
    __grammar = "союз"

    def part(self):
        return "Союз"

# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.


words = [Noun("Собака"), Verb("ела"), Noun("колбасу"), Conjunction("и"), Verb("запивала"), Noun("молоком")]
sentenc = Sentence([0, 1, 3, 5])
sentenc.show(words)
sentenc.show_parts(words)

