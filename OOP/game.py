from player import Player


class Game:
    def __init__(self):
        self.player = Player()

    def render_map(self):
        s = """****\n****"""
        li = s.split("\n")

        print(s)


game = Game()
print(game.player.default_damage)
game.render_map()
