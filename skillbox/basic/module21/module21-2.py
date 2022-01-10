"""
def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)

print(factorial(5))


def power(a, n):
    if n == 1:
        return a
    return a * power(a, n - 1)

float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))
"""

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(key, struct: dict):
    if key in struct:
        return struct[key]
    for val in struct.values():
        if isinstance(val, dict):
            result = find_key(key, val)
            if result:
                break
    else:
        result = None

    return result

key = input("Искомый ключ: ")
result = find_key(key, site)
if result:
    print("начение: {0}".format(result))
else:
    print("Такого ключа в структуре сайта нет.")