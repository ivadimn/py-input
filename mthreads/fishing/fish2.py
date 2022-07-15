import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')


# Определим функцию, эмулирующую рыбалку
def fishing(name, worms):
    catch = defaultdict(int)
    for worm in range(worms):
        print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
        _ = 3 ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}: Тьфу, сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1
    print(f'Итого рыбак {name} поймал:', flush=True)
    for fish, count in catch.items():
        print(f'    {fish} - {count}', flush=True)

# А теперь создадим второго рыбака, пошедшего на рыбалку ОДНОВРЕМЕННО с первым
thread = Thread(target=fishing, kwargs=dict(name='Вася', worms=10))
thread.start()

fishing(name='Коля', worms=10)

thread.join()