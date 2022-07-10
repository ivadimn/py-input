import json
from enum import Enum

class Gender(Enum):
    MALE = "муж."
    FEMALE = "жен."

class Edu:

    def __init__(self, university: str, year_finish: int, speciality: str):
        self.university = university
        self.year_finish = year_finish
        self.speciality = speciality

class Person:

    def __init__(self, name: str, surname: str, age: int, gender: Gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.edu_list = []

