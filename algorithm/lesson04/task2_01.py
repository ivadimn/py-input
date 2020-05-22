#Нахождение простых чисел с помощью алгоритма решето Эратосфена

import cProfile

def sieve(n : int) -> int:
    primes = [2]
    i = 3
    while len(primes) < n:
        if (i > 10) and (i % 10 == 5):
            i += 2
            continue
        for j in primes:
            if j * j - 1 > i:
                primes.append(i)
                break
            if (i % j == 0):
                break
        else:
            primes.append(i)
        i += 2
    return primes[n-1]

#timeit terminal
#1. python -m timeit -n 1000 -s "import task2_01" "task2_01.sieve(10)"
# 1000 loops, best of 5: 3.56 usec per loop

#2.  python -m timeit -n 1000 -s "import task2_01" "task2_01.sieve(20)"
# 1000 loops, best of 5: 9.25 usec per loop

#3. python -m timeit -n 1000 -s "import task2_01" "task2_01.sieve(100)"
# 1000 loops, best of 5: 91.8 usec per loop

#4. python -m timeit -n 1000 -s "import task2_01" "task2_01.sieve(200)"
# 1000 loops, best of 5: 237 usec per loop

#cProfile
#cProfile.run("sieve(10)")
#28 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task2_01.py:5(sieve)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       15    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run("sieve(20)")
#результат по времени такой же как и на 10

#cProfile.run("sieve(100)")
#результат по времени такой же как и на 10

#cProfile.run("sieve(200)")
#815 function calls in 0.001 seconds

#    Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 task2_01.py:5(sieve)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      612    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      199    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Вывод:  время работы алгоритма растёт при увеличении числа N
# время растёт не линейно (по результатам timeit)
