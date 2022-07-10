import json

tournaments = {
    "Aeroflot Open": 2010,
    "FIDE World Cup": 2018,
    "FIDE Crand Prix": 2016
}

class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return "Name: {0}, Year: {1}".format(self.name, self.year)

    def __repr__(self):
        return "Tournament('{0}', {1})".format(self.name, self.year)

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class ChessPlayer:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournaments)

t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE World Cup", 2010)
t3 = Tournament("FIDE Crand Prix", 2010)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default = lambda obj: obj.__dict__)
print(json_data)

decoded_player = ChessPlayer.from_json(json.loads(json_data))
print(decoded_player)
print(decoded_player.tournaments)
