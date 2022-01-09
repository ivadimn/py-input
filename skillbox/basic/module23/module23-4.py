"""
sym_count = 0
try:
    file = open("people.txt", "r")
    for line in file:
        length = len(line)
        if line.endswith("\n"):
            length -= 1
        if length < 3:
            raise BaseException("{0} слишком короткое имя".format(line))
        sym_count += length
    file.close()
except FileNotFoundError:
    print("Файл не найден ... ")
except BaseException:
    print("слишком короткое имя проброшено")
    raise
finally:
    print("Найденная сумма символов = {0}".format(sym_count))


def is_palindrom(word: str):
    if not word.isalpha():
        raise ValueError("В слове {0} встретились цифры ....".format(word))
    else:
        return True

def write_error_log(error : str):
    log_file = open("errors.log", "a")
    log_file.write("{}\n".format(error))
    log_file.close()

try:
    file = open("words.txt", "r")
    for word in file:
        if word.endswith("\n"):
            word = word[:-1]
        try:
            is_palindrom(word)
        except ValueError as ve:
            print(ve.args)
            write_error_log("В слове {0} встретились цифры ....".format(word))
    file.close()
except FileNotFoundError:
    print("Файл не найден....")
finally:
    print("Файл обработан!")

"""

lst = [23, 56, 100]
print(" ".join(lst))