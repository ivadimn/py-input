import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')

# Вроде все прекрасно, но в пайтоне есть суровый GIL - Global Interpreter Lock - https://goo.gl/MTokAe
# GIL велик и ужасен - это механизм блокировки выполнения потоков, пока один выполняется.
# Что, почему, зачем, Карл?! Зачем стрелять себе в ногу?
#
# Все дело в том, что сам пайтон - процесс в операционной системе. И ОС может приостанавливать выполнение
# самого процесса пайтона. А когда происходит двойное засыпание/просыпание,
# то возникает проблема доступа к одним и тем участкам памяти. Поэтому разработчики CPython,
# (а у нас именно эта реализация) решили сделать GIL.
#
# Поэтому нельзя получить выгоду в производительности программы в т.н. CPU-bounded алгоритмах
# (это те, которым требуется процессорное время и не нужны операции ввода/вывода)

# Хорошая новость в том, что пайтон отпускает GIL перед системными вызовами. Чтение из файла, к примеру,
# может занимать длительное время и совершенно не требует GIL — можно дать шанс другим потокам поработать.
# ...
# Профит! там где есть операции ввода/ввывода: чтение с диска, обменд данными по сети, етс.
# Хорошая новость: любая программа должна обмениваться данными с внешним миром :)

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            #_ = worm ** 10000  # фиксируем время ожидания поклевки
            time.sleep(0.01)
            fish = random.choice(FISH)
            if fish is not None:
                self.catch[fish] += 1


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 6)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)',)
        return result
    return surrogate


@time_track
def run_in_one_thread(fishers):
    for fisher in fishers:
        fisher.run()


@time_track
def run_in_threads(fishers):
    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()


humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
fishers = [Fisher(name=name, worms=100) for name in humans]

run_in_one_thread(fishers)
run_in_threads(fishers)

# Про обьяснение механизма GIL очень рекомендую посмотреть видео с Moscow Python Meetup:
# Григорий Петров. "GIL в Python: зачем он нужен и как с этим жить"
# http://www.moscowpython.ru/meetup/14/gil-and-python-why/
