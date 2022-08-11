from game import Game
from player import AiResolve
from dot import Dot
from commons import ShotResult

if __name__ == "__main__":
    ship_lens = [3, 2, 2, 1, 1, 1, 1]
    game = Game(ship_lens)
    game.start()

    """air = AiResolve(Dot(5, 5), 6)
    for direct, dots in air.directs.items():
        print("{0} - {1}".format(direct, [str(dot) for dot in dots]))
        print()
        print("_" * 30)
    print(list(air.directs.keys())[0])
    print("*" * 20)
    
    result = ShotResult.WOUNDED
    while True:
        dot = air.next_dir(result)
        print(dot)
        r = input("Result: ")
        if r == "p":
            result = ShotResult.PAST
        elif r == "w":
            result = ShotResult.WOUNDED
        else:
            break
"""








