# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) передаётся параметром.


import cProfile

#здесь сумма последовательности считается сложением её членов
#с использованием других арифметических операций чем в варианте 2
def calc_summa(n: int):
    b = 1
    q = -0.5
    summa = 1
    for i in range(1, n):
        summa += b * q
        b *= q
    return summa


#timeit через терминал
#1. python -m timeit -n 1000 -s "import task1_03" "task1_03.calc_summa(10)"
# 1000 loops, best of 5: 597 nsec per loop

#2. python -m timeit -n 1000 -s "import task1_03" "task1_03.calc_summa(1000)"
# 1000 loops, best of 5: 42.1 usec per loop

#3. python -m timeit -n 1000 -s "import task1_03" "task1_03.calc_summa(100000)"
# 1000 loops, best of 5: 4.37 msec per loop

#python -m timeit -n 1000 -s "import task1_03" "task1_03.calc_summa(10000000)"
# 1000 loops, best of 5: 436 msec per loop
# в такой реализации время расчёта суммы растёт пропорционально росту
# количества членов последовательности
# эта реализация работает быстрее чем вариант 2

#cProfile
#cProfile.run("calc_summa(10)")
#4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task1_03.py:9(calc_summa)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run("calc_summa(1000)")
#тот же результат что и при 10

#cProfile.run("calc_summa(100000)")
# 4 function calls in 0.006 seconds

#Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#        1    0.006    0.006    0.006    0.006 task1_03.py:9(calc_summa)
#        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# на 100000 работает быстрее чем вариант 2

#cProfile.run("calc_summa(10000000)")
#4 function calls in 0.487 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.486    0.486 <string>:1(<module>)
#        1    0.486    0.486    0.486    0.486 task1_03.py:9(calc_summa)
#        1    0.000    0.000    0.487    0.487 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#общий вывод:
#алгоритмы вычисления суммы последовательности где используестя простое сложение её членов
#работаю медленные чем алгоритм использующий  формулу суммы геометрической прогрессии
#при этом алгоритмах где используется сложение время выполнения растёт пропорционально
#количеству членов порследовательности
#алгоритм где используется возведение в степень (task1_02) медленнее чем
#task1_03 где используется умножение


