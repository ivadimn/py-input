# Асинхронное программирование порождает несколько проблем.
#
# Одна из них - доступ к совместным данным: если два потока меняют один и тот же обьект,
# то программа становится непредсказуемой. Эта проблема называется состояние гонки (race conditions)
# https://goo.gl/Dz9aJ3
import random
from collections import defaultdict

import threading

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(threading.Thread):

    def __init__(self, name, worms, fish_tank, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank

    def run(self):
        for worm in range(self.worms):
            fish = random.choice(FISH)
            if fish is not None:
                self.fish_tank[fish] += 1
                self.catched += 1


# Общий сачок для рыбы
global_fish_tank = defaultdict(int)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава',
          'Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава',
          'Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
fishers = [Fisher(name=name, worms=100000, fish_tank=global_fish_tank) for name in humans]

for fisher in fishers:
    fisher.start()
for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())

print(f'Итого рыбаки поймали {total_fish_from_fishers} шт., а с берега увидели {total_fish_in_tank} шт.')
