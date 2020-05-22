# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) передаётся параметром.


import cProfile

#здесь сумма последовательности считается сложением её членов
def calc_summa(n: int):
    q = -0.5
    summa = 0
    for i in range(0, n):
        summa += q ** i
    return summa

#timeit через терминал
#1. python -m timeit -n 1000 -s "import task1_02" "task1_02.calc_summa(10)"
#1000 loops, best of 5: 1.05 usec per loop

#2.python -m timeit -n 1000 -s "import task1_02" "task1_02.calc_summa(1000)"
# 1000 loops, best of 5: 114 usec per loop

#3.python -m timeit -n 1000 -s "import task1_02" "task1_02.calc_summa(100000)"
# 1000 loops, best of 5: 12.4 msec per loop
# в такой реализации время расчёта суммы растёт пропорционально росту
# количества членов последовательности

#cProfile
#cProfile.run("calc_summa(10)")
#4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task1_02.py:8(calc_summa)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run("calc_summa(1000)")
#тот же результат что и при 10

#cProfile.run("calc_summa(100000)")
# 4 function calls in 0.014 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#        1    0.014    0.014    0.014    0.014 task1_02.py:8(calc_summa)
#        1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#здесь время выросло до 14 msec

#cProfile.run("calc_summa(10000000)")
# 4 function calls in 1.263 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.263    1.263 <string>:1(<module>)
#        1    1.263    1.263    1.263    1.263 task1_02.py:8(calc_summa)
#        1    0.000    0.000    1.263    1.263 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#здесь время ещё выросло почти в 100 раз
# здесь вывол такой же - в такой реализации время расчёта суммы растёт пропорционально росту
# количества членов последовательности
