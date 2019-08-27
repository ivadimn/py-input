import re
import collections

#1
file = open ('text.txt', 'r')
text = file.read()
#print(text)

#2
text2 = re.split('\.,\!,\?', text)
print (text2)


#3
text3 = re.findall('\W(\w{4})\W', text)
a = 0
print(text3)
dict1 = collections.Counter(text3).most_common(10)
print (dict1)


#4
pattern = re.compile('https?://[\S]+')
text4 = re.findall(pattern, text)
print(text4)

#5
text5 = re.findall('https://(\w+\.\w+)/', text)
print(text5)
dict2 = collections.Counter(text5).most_common(1)
print (dict2)

#6
text6 = re.sub('https?://[\S]+', 'Ссылка отобразится после регистрации', text)
print(text6)

    

        
 
