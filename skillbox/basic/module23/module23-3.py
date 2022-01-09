text = input("Введите чего-нибудь: ")
try:
    out_file = open("result.txt", "x")
    try:
        out_file.write(text)
    except ValueError:
        print("Ошибка преобразования данных.")
    except TypeError:
        print("Значение не может быть записано в файл.")
    finally:
        out_file.close()
    print(type(out_file))
except FileExistsError:
    print("Выходной файл уже создан.")
else:
    print("Всё прошло без ошибок!!")
