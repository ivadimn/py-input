"""
menu = input("Доступное меню: ").split(";")
print("На данный момент в меню есть:", ", ".join(menu))


words = input("Введите слова через пробел: ").split()
max_len_word = words[0]
max_len = len(words[0])
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word
print("Самое длинное слово:", max_len_word, "его длина =", max_len)


spec_ch = tuple("@№$%^&*()")
exts = (".txt", )
file_name = input("Название файла: ")
if file_name.startswith(spec_ch):
    print("Ошибка: название начинается на один из специальных символов")
elif not file_name.endswith((".txt", ".docs")):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")


words = input("Введите строку: ").split()
words_cap = [word.capitalize()  for word in words]
print("Результат:", " ".join(words_cap))



def is_pwd_secure(pwd: str):
    is_cap_ch = False
    count_digits = 0
    for ch in pwd:
        if ch.isalpha() and ch.isupper():
            is_cap_ch = True
        elif ch.isdigit():
            count_digits += 1
    return is_cap_ch and count_digits >= 3


password = input("Придумайте пароль: ")
while not is_pwd_secure(password):
    print("Пароль ненадёжный. Попробуйте ещё раз.")
    password = input("Придумайте пароль: ")
print("Это надёжный пароль!")


def encode(text: str):
    index = 0
    encode = []
    while index < len(text):
        ch = text[index]
        count = 1
        index += 1
        while index < len(text) and text[index] == ch:
            count += 1
            index += 1
        encode.append(ch)
        encode.append(str(count))
    return "".join(encode)

text = input("Введите строку: ")
print("Закодированная строка:", encode(text))

def is_valid_oktet(oktet: str):
    is_valid = False
    if not oktet.isdigit():
        print(oktet, "- не целое число")
    else:
        oktet_num = int(oktet)
        if 0 <= oktet_num <= 255:
            is_valid = True
        else:
            print(oktet_num, "превышает 255")
    return is_valid


def is_valid_ip(o_list: list):
    is_valid = False
    if len(o_list) != 4:
        print("Адрес - это четыре числа, разделённые точками")
    else:
        for oktet in o_list:
            is_valid = is_valid_oktet(oktet)
    return is_valid


oktet_list = input("Введите IP: ").split(".")
if is_valid_ip(oktet_list):
    print("IP-адрес корректен")

def shift(l, k):
    l_new = list(l)
    len_list = len(l)
    for i in range(len_list):
        i_new = (i + k) % len_list
        l_new[i_new] = l[i]
    return "".join(l_new)


def get_shift(s1: str, s2: str):
    sh = -1
    if s1 != s2:
        for h in range(1, len(s1)):
            s2_shift = shift(s2, 1)
            if s2_shift == s1:
                sh = h
                break
            s2 = s2_shift
    else:
        sh = 0
    return sh

line1 = input("Первая строка: ")
line2 = input("Вторая строка: ")

sh = get_shift(line1, line2)
if sh > 0:
    print("Первая строка получается из второй со сдвигом", sh)
"""

def process_bad_word(word: str):
    new_word = []
    part_word = []
    for ch in word:
        if ch.isalnum():
            part_word.append(ch)
        else:
            part_word.reverse()
            new_word.append("".join(part_word))
            part_word.clear()
            new_word.append(ch)
    if len(part_word) > 0:
        part_word.reverse()
        new_word.append("".join(part_word))

    return "".join(new_word)


def generate_new_message(message: list):
    new_message = []
    for word in message:
        if word.isalnum():
            l = list(word)
            l.reverse()
            new_message.append("".join(l))
        else:
            new_message.append(process_bad_word(word))
    return " ".join(new_message)

message = input("Сообщение: ").split()
print("Новое сообщение:", generate_new_message(message))




"""
def generate_alphabet():
    ab = [chr(i_ch) for i_ch in range(33, 127)]
    return "".join(ab)

def shift(l, k):
    l_new = l.copy()
    len_list = len(l)
    for i in range(len_list):
        i_new = (i + k) % len_list
        l_new[i_new] = l[i]
    return l_new

def hack(msg: str, alphabet: str, key: int):
    hacked = []
    for ch in msg:
        if ch in alphabet:
            index = alphabet.find(ch)
            hacked_index = index - key
            if hacked_index < 0:
                hacked_index += len(alphabet)
            hacked.append(alphabet[hacked_index])
        else:
            hacked.append(ch)
    return "".join(hacked)

message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
alphabet =  generate_alphabet()
print(alphabet)
words = hack(message, alphabet, 1).split()
print("msg: ", words)
sh = 3
list_sentences = []
sent = []
for word in words:
    print(word)
    word = shift(list(word), sh)
    sent.append("".join(word))
    if "." in word or "!" in word:
        list_sentences.append(sent)
        sent = []
        sh += 1
print(list_sentences)
"""
