import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

"""
pattern = r"\b\w{4}[\s\.,]"
words = re.findall(pattern, text)
print(words)
"""


text = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"
pattern = r"\b[АВЕКМНОРСТУХ]{1,2}\d{3}[АВЕКМНОРСТУХ]{,2}\d{2,3}"
numbers = re.findall(pattern, text)
print(numbers)