# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) передаётся параметром.


import cProfile

#здесь сумма считается с использованием формулы суммы геометрической прогрессии
def calc_summa(n: int):
    b1 = 1
    q = -0.5
    return b1 * (1 - q ** n) / (1 - q)
#timeit через терминал
#1. python -m timeit -n 1000 -s "import task01" "task01.calc_summa(10)"
#1000 loops, best of 5: 215 nsec per loop

#2. python -m timeit -n 1000 -s "import task01" "task01.calc_summa(1000)"
#1000 loops, best of 5: 215 nsec per loop

#3. python -m timeit -n 1000 -s "import task01" "task01.calc_summa(100000)"
#1000 loops, best of 5: 226 nsec per loop

#4. python -m timeit -n 1000 -s "import task01" "task01.calc_summa(10000000)"
#1000 loops, best of 5: 327 nsec per loop
#время выпорлнения практически не зависит от длины последовательности
#увеличивается на 112 nsec, ксли длину увеличить в 1 000 0000  раз

#cProfile
#cProfile.run("calc_summa(10)")
#4 function calls in 0.000 seconds

#   Ordered by: standard name

 #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #      1    0.000    0.000    0.000    0.000 task1_01.py:10(calc_summa)
 #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run("calc_summa(1000)")
#cProfile.run("calc_summa(100000)")
#cProfile.run("calc_summa(10000000)")
#  тот же результат что и при n = 10

#Вывод данная реализация расчёта суммы последовательности
# не зависит от длины последовательности

