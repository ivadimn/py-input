#
#  Циклические конструкции
#

# Цикл while
step = 0
max_steps = 5

while step < max_steps:
    print(f"I'm working on ... {max_steps - step} remaining")
    step += 1

# Цикл for in
persons = ['Jim', 'Adam', 'Kate', 'Peter']
digs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
digs1 = [1, 2, 3, 4, 5]

print(digs1[-10:])

for person in persons:
    print(f"Hello, {person}")
