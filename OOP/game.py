from player import Player
from hamsters import Hamster

hamsters_count = 4

class Game:
    map = """****\n****\n****\n****"""

    def __init__(self):
        self.player = Player()
        self.hamsters = [Hamster(i + 1, len(self.map.split("\n")[0]) ,
                                 len(self.map.split("\n")) ) for i in range(hamsters_count)]

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
            if self.player.position[0] == len(self.map.split("\n")[0]) - 1:
                return False
            self.player.position[0] += 1
        self.on_move()

    def get_hamster_on_position(self, coords):
        s = self.map
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s.split("\n")[coords[1]][coords[0]]

    def on_move(self):
        print(self.player.position)

    def start(self):
        self.render_map()
        while True:
            command = input("Insert command : ")
            if command in ["a", "s", "d", "w"]:
                self.move_player(command)
                self.render_map()
            else:
                break

game = Game()
game.start()
