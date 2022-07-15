import random
from collections import defaultdict

import threading

FISH = (None, 'плотва', 'окунь', 'лещ')

###
# Другая проблема с блокировками: они могут быть взаимными.
# Один поток заблокировал ресурс A и ему нужен ресурс Б, а другой поток наобарот - заблокировал Б и ждет А.


def func_1(n):
    global a, b
    for i in range(n):
        print(f'{i}: func_1 wait lock_A', flush=True)
        with lock_A:
            print(f'{i}: func_1 take lock_A', flush=True)
            a += 1
            print(f'{i}: func_1 wait lock_B', flush=True)
            with lock_B:
                print(f'{i}: func_1 take lock_B', flush=True)
                b += 1


def func_2(n):
    global a, b
    for i in range(n):
        print(f'{i}: func_2 wait lock_B', flush=True)
        with lock_B:
            print(f'{i}: func_2 take lock_B', flush=True)
            b += 1
            print(f'{i}: func_2 wait lock_A', flush=True)
            with lock_A:
                print(f'{i}: func_2 take lock_A', flush=True)
                a += 1


a = 0
b = 0
lock_A = threading.RLock()
lock_B = threading.RLock()
N = 10

thread_1 = threading.Thread(target=func_1, args=(N,))
thread_2 = threading.Thread(target=func_2, args=(N,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(a, b)

# Это называется красиво: deadlock - тупик или безвыходное положение.
# Что делать, что бы избежать deadlock-ов?
#
# Вот рецепты, в порядке убывания значимости:
#  - стараться как можно меньше использовать общие обьекты (глобальные обьекты состояния)
#  - делать как можно меньше вложенных блокировок
#  - внимательно обращаться с существующими блокировками
# Вообще, эти рекомендации относятся ко всему асинхронному программированию,
# вот статья для медитации над этой темой: https://dev.by/news/pochemu-oni-ne-umeyut-pisat-mnogopotochnye-programmy


###
# Есть еще несколько способов синхронизировать потоки:
#
# Семафоры (Semaphore) - https://goo.gl/PZFKTu - очень похожи на Lock, но позволяют выполнять критичный код
# нескольким потокам
#
# Барьер (Barrier) - https://goo.gl/9f1MHk - позволяет нескольким потокам продолжить свое выполнение одновременно.
# Если в потоке есть barrier.wait() то поток приостанавливается, пока все остальные потоки не вызовут barrier.wait()
#
# События (Events) - https://goo.gl/ewCFgh - поток(и) могут ждать пока событие не будет установлено,
# а другой поток может устанавливать или сбрасывать это событие.
#
# Условные переменные (Condition) - https://goo.gl/mVF6rw - позволяют потоку ждать, пока другой поток
# подготовит данные и сообщит об этом
#
# Таймер (Timer) - https://goo.gl/TqZXXY - похож на простой Thread, но начинает выполнение через N секуднд
#
# Хорошая статья про примитивы синхронизации: Fredrik Lundh "Thread Synchronization Mechanisms in Python"
# перевод http://www.quizful.net/post/thread-synchronization-in-python

