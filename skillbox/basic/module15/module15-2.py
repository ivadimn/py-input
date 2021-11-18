"""
nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)
maximum = minimum = nums_list[0]
for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)


numbers = []
count_numbers = int(input("Кол-во чисел в списке: "))
for i in range(count_numbers):
    print("Введите", i + 1, "число: ", end = "")
    number = int(input())
    numbers.append(number)
divizor = int(input("\nВведите делитель: "))
summ_index = 0
for i in range(len(numbers)):
    if numbers[i] % divizor == 0:
        summ_index += i
        print("Индекс числа", numbers[i], ":", i)
print("\nСумма индексов:", summ_index)
"""

scores_list = []
N = int(input('Кол-во собак: '))
for i in range(N):
    print('Количество очков', i + 1, "собаки: ", end = "")
    score = int(input())
    scores_list.append(score)
maximum = minimum = scores_list[0]
max_index = min_index = 0
for i in range(len(scores_list)):
    if maximum < scores_list[i]:
        maximum = scores_list[i]
        max_index = i
    if minimum > scores_list[i]:
        minimum = scores_list[i]
        min_index = i
scores_list[max_index], scores_list[min_index] = scores_list[min_index], scores_list[max_index]
print(scores_list)


