def are_both_odd(A, B):
    return (A % 2 != 0) and (B % 2 != 0)

def get_wind_class(speed):
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif speed >= 19:
        return "hurricane [4]"


user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if username in user_database:
        if user_database[username] == password:
            return True
        else:
            return False
    else:
        return False


def check_h(n):
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = ((n * 3) + 1) / 2
        if n == 1:
            return True
    return False

def print_ladder(n):
    for i in range(1, n + 1):
        print("*" * i)

print(check_h(25))


