"""
family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

f_member = dict()
f_member["name"] = "Jane"
f_member["surname"] = "Doe"
f_member["hobbies"] = ["running", "sky diving", "singing"]
f_member["age"] = 35
f_member["children"] = [{"name": "Alice", "age": 6}, {"name": "Bob", "age": 8}]

print(f_member)
children = f_member.get("children", [])
for child in children:
    if child.get("name", "") == "Bob":
        print("Ребёнок с именем Bob есть")
        surname = f_member.get("surname", "Nosurname")
        print(surname)


players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

player_rest = [player for player in players_dict.values() if player.get("status") == "Rest"]
print(player_rest)
player_train = [player for player in players_dict.values() if player.get("status") == "Training"]
print(player_train)
player_travel = [player for player in players_dict.values() if player.get("status") == "Travel"]
print(player_travel)
"""


