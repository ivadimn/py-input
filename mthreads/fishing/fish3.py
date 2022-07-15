# Как создать и запустить поток
import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')

# При простой передаче функции в поток результат выполнения функции
# можно получить только через изменяемый обьект в параметрах:
def fishing(name, worms, catch):
    for worm in range(worms):
        print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
        _ = 3 ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}: Тьфу, сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1


vasya_catch = defaultdict(int)
thread = Thread(target=fishing, kwargs=dict(name='Вася', worms=10, catch=vasya_catch))
thread.start()

kolya_catch = defaultdict(int)
fishing(name='Коля', worms=10, catch=kolya_catch)

thread.join()
for name, catch in (('Вася', vasya_catch), ('Вася', kolya_catch)):
    print(f'Итого рыбак {name} поймал:')
    for fish, count in catch.items():
        print(f'    {fish} - {count}')