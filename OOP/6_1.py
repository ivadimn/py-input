from my_class import Word
from my_class import Sentence

my_dict = {'сущ': 'существительное', 'гл': 'глагол', 'прил': 'прилгательное', 'пред': 'предлог'}

class Noun(Word, Sentence):
    _grammar = 'сущ'

    def __init__(self):
        return

    def part(self, _grammar):
        self.part = my_dict[_grammar]
        return


nouns = Noun()


print(nouns.part('гл'))


# class Verb (Word, Sentence):
#     __grammar = 'гл'
#
# sent = Verb ([2, 3, 1])
# words = []
# words.append(Noun("собака"))
# words.append(Verb("ела"))
# words.append(Noun("колбасу"))
# words.append(Noun("кот"))
# sent.show ([1,2])

