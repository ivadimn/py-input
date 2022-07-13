import random

class Gallows:

    def __init__(self) -> None:
        self.__word = None
        self.__attempts = 0
        self.__open_letters = []
        self.__input_letters = []

    @property
    def attempts(self):
        return self.__attempts

    @attempts.setter
    def attempts(self, attempts: int):
        self.__attempts = attempts

    @property
    def open_letters(self):
        return "".join(self.__open_letters)

    @property
    def input_letters(self):
        return ", ".join(self.__input_letters)

    @property
    def word(self):
        return self.__word

    def generate_word(self):
        with open("words.txt", "r", encoding="UTF-8") as f:
            words = f.readlines()
        index = random.randint(0, len(words) - 1)
        self.__word = words[index].rstrip()
        self.__open_letters.extend("_" * len(self.word))

    def set_letter(self, letter: str) -> None:
        letter = letter.lower()
        for i, ch in enumerate(self.__word):
            if letter == ch:
                self.__open_letters[i] = char
        self.__input_letters.append(char)
        self.attempts -= 1

    @property
    def is_win(self) -> bool:
        return "".join(self.__open_letters) == self.__word


g = Gallows()
g.generate_word()
g.attempts = 20
while g.attempts > 0:
    char = input("Введите букву: ")
    g.set_letter(char)
    print("Что уже угадали: {0}".format(g.open_letters))
    print("Осталось попыток: {0}".format(g.attempts))
    print("Уже введённые буквы: {0}".format(g.input_letters))
    print("-" * 40)
    if g.is_win:
        print("Поздравляем вы выиграли!!!!")
        print("Загаданное слово: {0}".format(g.word))
        break
else:
    print("Попытки закончились")
    print("Вы проиграли....")
    print("Загаданное слово: {0}".format(g.word))

