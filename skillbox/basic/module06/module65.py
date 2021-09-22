total_word = int(input("Введите количество раз для вывода: "))
word_count = 0
while word_count < total_word:
    print("Я программист!")
    word_count += 1

total_count = int(input("Cколько раз напомнить: "))
count = 0
while count < total_count:
    print("Вы хотели не забыть о чём-то")
    count += 1

total_bags = int(input("Cколько всего мешков? "))
bag_count = 0
total_weight = 0
while bag_count < total_bags:
    weight = int(input("Сколько весит мешок? "))
    total_weight += weight
    bag_count += 1
print("Ощий вес мешков:", total_weight)