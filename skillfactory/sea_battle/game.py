from board import Board, BoardBuilder
from player import User, Ai
from commons import Values, ShotResult


class Game:

    def __init__(self, ship_lens: list[int]):
        self.__ship_lens = ship_lens
        self.user_board = None
        self.ai_board = None
        self.user = None
        self.ai = None

    def start(self):
        print("Минуточку, подготовка к игре....")
        self.user_board = BoardBuilder().set_size(6).set_hidden(False) \
            .build(self.__ship_lens)
        self.ai_board = BoardBuilder().set_size(6).set_hidden(True) \
            .build(self.__ship_lens)
        self.user = User("User", self.user_board, self.ai_board)
        self.ai = Ai("Computer", self.ai_board, self.user_board)
        self.greet()
        self.loop()

    def show_boards(self) -> str:
        lines = list()
        user_str = "{0}{1}".format("user", " " * (20 - len("user")))
        ai_str = "{0}{1}".format("AI", " " * (20 - len("AI")))
        lines.append("{0}{1}".format(user_str, ai_str))
        for i in range(1, self.user_board.size + 4):
            lines.append("{0}{1}".format(self.__show(self.user_board, i),
                                         self.__show(self.ai_board, i)))
        return "\n".join(lines)

    def __show(self, board: Board, line: int) -> str:
        if line == 1:
            return "  |{0}|{1}".format("|".join([str(num + 1) for num in range(board.size)]), " " * 5)
        if line == 2:
            return "{0}{1}".format("-" * 15, " " * 5)
        if 3 <= line <= 8:
            x = line - 3
            vals = list()
            for y in range(board.size):
                val = board.value(x, y)
                if board.hidden and val == Values.SHIP:
                    val = Values.SPACE
                vals.append(val.value)
            return " {0}|{1}|{2}". \
                format(str(x + 1), "|".join(vals), " " * 5)
        if line > 8:
            return "{0}{1}".format("-" * 15, " " * 5)

    def greet(self) -> None:
        print("Добро пожаловать в игру 'Морской бой'")
        print("Игра проводится на поле размером 6х6 клеток.\n")
        print("Корабли:")
        print("\t1 - 3-х палубный")
        print("\t2 - 2-х палубных")
        print("\t4 - 1-на палубных\n")
        print("При осуществлении выстрела необходимо ввести через пробел")
        print("номер строки и номер колонки в диапазоне от 1 до 6.")
        print("Удачи...")

    def loop(self):
        players = [self.user, self.ai]
        curr_player = players.pop(0)
        print("Игровые доски:")
        print(self.show_boards())
        while self.user_board.is_live and self.ai_board.is_live:
            result = curr_player.move()
            if result == ShotResult.KILLED:
                print("Удачный ход - корабль убит!!!")
            elif result == ShotResult.WOUNDED:
                print("Удачный ход - корабль ранен!!!")
            else:
                print("Промах!")
                players.append(curr_player)
                curr_player = players.pop(0)
            print(self.show_boards())
            a = input("Для следующего хода нажмите Enter...")
            print("-" * 50)
            print("user - {0}, ai - {1}".format(self.user_board.is_live, self.ai_board.is_live))
        else:
            if self.user_board.is_live:
                print("Поздравляем вы выиграли!!!")
            else:
                print("Сожалеем, но вы проиграли")
