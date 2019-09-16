
words = []

# words = []
# for i in range(len(list)) :
#     words.append(list[i-1][0])
# print (words)
class Word:


    def __init__(self, text):
        print (text)
        words.append (text)
        # print(words)


my_words1 = Word("Шиншилла")
my_words2 = Word('Прыгает')
my_words3 = Word('Пушистый')
print (words[0])



class Sentence:
    content = []
    def __init__(self, content):
        return
        # print(content)
    def show (self, content):
        sentences = []
        for i in content:
            sentences.append (words[i])
        print ('Результат Show: ', sentences [0] + ' '  + sentences [1])
     #def show_parts (self, content):
     #    sentence_part = []
     #    for i in content:
     #        sentence_part.append (words[i][1])
     #    print ('Результат Show_parts: ', sentence_part [0] + ' '  + sentence_part [1])

sentence = Sentence([0,2])
sentence.show([0, 2])
#sentence.show_parts([0, 2])




