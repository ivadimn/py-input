def numbers(start: int, step: int = 1):
    number = start
    while True:
        yield number
        number += step

def cycle(array: list):
    index = 0
    while True:
        yield array[index]
        index += 1
        if index >= len(array):
            index = 0


import time


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper

def pow_2():
   return 10000000 ** 2

time_len = decorator_time(pow_2)
tm = 0
for i in range(100):
    tm += time_len()

print("Среднее вренмя {0}".format(tm / 100))