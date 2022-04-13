from abc import ABC


class Res(ABC):
    price_questions = []
    error_msgs = []


class ResRu(Res):
    pass