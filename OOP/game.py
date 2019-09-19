from player import Player
from hamsters import Hamster

hamsters_count = 4

class Game:
    map = """****\n****\n****\n****"""
    gameon = True
    happy_message = "WOW!!!!! You won!!!"

    def __init__(self):
        self.player = Player(self.map)
        self.hamsters = []
        for i in range(hamsters_count):
            self.hamsters.append(Hamster(i + 1, self.get_full_map()))

    def add_point(self, position, name, s):
        li = s.split("\n")
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return "\n".join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, "x", s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        print(s)

    def move_player(self, destination):
        """ destination = w, a, s, d"""
        if destination == "s":                # bottom
            if self.player.position[1] == len(self.map.split("\n")) - 1:
                return False
            self.player.position[1] += 1
        if destination == "w":                # top
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1
        if destination == "a":                # left
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1
        if destination == "d":                # right
            # здесь исправлено с self.player.position[1] на self.player.position[0]
            if self.player.position[0] == len(self.map.split("\n")[0]) - 1:
                return False
            self.player.position[0] += 1
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        # добавлено чтобы хомяк не накладывалься на игрока при создании
        s = self.add_point(self.player.position, "x", s)
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split("\n")[coords[1]][coords[0]]

    directions = {"w": "s", "s": "w", "a": "d", "d": "a"}

    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        # здесь добавлено сравнение с х
        if not hamster in ["*", "x"]:
            self.player.was_hit(int(hamster))
            if self.player.health <= 0:
                self.gameon = False
                print("game over ..... sorry!")
                return False
            print("player's health: ", self.player.health)
            killed = self.hamsters[int(hamster) - 1].on_shot()
            if not killed:
                print("wasn`t killed")
                self.move_player(self.directions[direction])
            else:
                print(self.hamsters[int(hamster) - 1].id, " was killed")

    def get_count_active_hamsters(self):
        count_active = 0
        for h in self.hamsters:
            if h.health > 0:
                count_active += 1
        return count_active

    def start(self):
        self.render_map()
        while self.gameon:
            # здесь заменено на подсчёт количества здоровых хомяков, если их нет то мы выиграли
            if self.get_count_active_hamsters() == 0:
                print(self.happy_message)
                return True
            command = input("Insert command : ")
            if command in ["a", "s", "d", "w"]:
                self.move_player(command)
                self.render_map()
            if command == "e":
                self.player.wait()
            if command == "q":
                self.gameon = False

game = Game()
game.start()

# Комментарии
"""
1. В этом блоке  метода move_player исправлено : 
    с self.player.position[1] == len(self.map.split("\n")[0]) - 1
    на self.player.position[0] == len(self.map.split("\n")[0]) - 1
if destination == "d":
    if self.player.position[0] == len(self.map.split("\n")[0]) - 1:
        return False
    self.player.position[0] += 1  # right
    
2. В класс Player добавлен конструктор
    def __init__(self, map):
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        self.position = [randint(0, map_width - 1), randint(0, map_height - 1)] # пока карта пустая можно вставлять куда угодно
устанавливает случайную позицию игрока пока карта не заполнена

3. в метод get_full_map() 
добавлено  s = self.add_point(self.player.position, "x", s) отрисовка позиции игрока 
чтобы на неё не наложился хомяк при создании   

4. в методе on_move()  
строка if not hamster  == "*": 
заменена на if not hamster in ["*", "x"]:

5. добавлен метод get_count_active_hamsters() для посчёта здоровых хомяков так как мы не удаляем хомяков из списка после их смерти
если их нет то мы выиграли, 
    """
