min_salary: float = 50000.0
step = 1.15

for i in range(1, 23):
    print(min_salary * (step ** i))