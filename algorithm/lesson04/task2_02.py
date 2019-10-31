#Нахождение простых чисел без использования алгоритма решето Эратосфена

import cProfile

def prime(n : int) -> int:
    primes = [2]

    def isPrime(n):
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    num = 3
    while len(primes) < n:
        if isPrime(num):
            primes.append(num)
        num += 1
    return primes[n - 1]

#timeit
#1. python -m timeit -n 1000 -s "import task2_02" "task2_02.prime(10)"
# 1000 loops, best of 5: 7.71 usec per loop

#2.python -m timeit -n 1000 -s "import task2_02" "task2_02.prime(20)"
# 1000 loops, best of 5: 30 usec per loop

#3. python -m timeit -n 1000 -s "import task2_02" "task2_02.prime(100)"
# 1000 loops, best of 5: 916 usec per loop

#4. python -m timeit -n 1000 -s "import task2_02" "task2_02.prime(200)"
# 1000 loops, best of 5: 4.51 msec per loop

#здесь время работы алгоритма растёт быстрее чеи в решете Эратосфена


#cProfile.run("prime(10)")
#68 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task2_02.py:5(prime)
#       27    0.000    0.000    0.000    0.000 task2_02.py:8(isPrime)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run("prime(20)")
#162 function calls in 0.000 seconds
#по времени тоже что и на 10

#cProfile.run("prime(100)")
#1182 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 task2_02.py:5(prime)
#      539    0.001    0.000    0.001    0.000 task2_02.py:8(isPrime)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run("prime(200)")
#2646 function calls in 0.005 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#        1    0.000    0.000    0.005    0.005 task2_02.py:5(prime)
#     1221    0.005    0.000    0.005    0.000 task2_02.py:8(isPrime)
#        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#     1222    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      199    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#вывод алгоритм решето Эратосфена работает быстрее текщего и сскорость роста времени работы
# алгорпитма решето Эратосфена медленней при увеличении числа N
#
