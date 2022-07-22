import csv
from enum import IntEnum


class Status(IntEnum):
    IN_PROGRESS = 0
    FINISHED = 1


class Question:

    def __init__(self, question: str, answer: str, exlpanation: str):
        self.question = question
        self.answer = answer.lower()
        self.explanation = exlpanation

class Questions:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __iter__(self):
        file = open(self.file_path, "r", newline="")
        self.questions = csv.reader(file)
        return self.questions

    def __next__(self):
        row = next(self.questions)
        if row is None:
            raise StopIteration()
        else:
            return Question(*row)



class Game:

    def __init__(self, file_path: str, max_errors: int) ->None:
        self.file_path = file_path
        self.max_errors = max_errors
        self.__status = Status.IN_PROGRESS
        self.errors = 0
        self.questions = []
        self.__index = -1
        self.__read_questions()

    def __read_questions(self):
        with open(self.file_path, "r", newline="") as file:
            data = csv.reader(file)
            for row in data:
                self.questions.append(Question(*row))


    @property
    def status(self):
        return self.__status

    def next_question(self) -> Question | None:
        self.__index += 1
        if self.__index < len(self.questions):
            question = self.questions[self.__index]
            return question
        return None

    def get_status(self):
        return self.status

    def set_answer(self, answer: str):
        if self.questions[self.__index].answer != answer.lower():
            self.errors += 1
            if self.errors == self.max_errors:
                self.__status = Status.FINISHED


print("Ответьте пожалуйста на вопросы, вы можете сделать 2 ошибки!!")
g = Game("questions.csv", 2)
while q := g.next_question():
    print("Вопрос: {0}".format(q.question))
    answer = input("Ваш ответ (yes / no): ")
    g.set_answer(answer)
    if g.status == Status.FINISHED:
        print("Сожалеем, вы сделали {0} ошибок и проиграли!!".format(g.errors))
        break
else:
    print("Поздравляем вы выиграли!!!")
