"""
for i in range(1, 10):
	for j in range(1, 10):
		print(i * j, end = "\t")
	print()	


oper = input("Введите операцию: ")
while oper != "+" and oper != "-" and oper != "*" and oper != "/":
	print("Ошибка: такой операции не существует. Попробуйте ещё раз.")
	oper = input("Введите операцию: ")
count = int(input("Сколько операндов? "))
print("Введите операнд", 1, ": ", end = "")
result = int(input())
output = str(result)
for i in range(2, count + 1):
	print("Введите операнд", i, ": ", end = "")
	n = int(input())
	if oper == "+":
		result += n
	elif oper == "-":
		result -= n
	elif oper == "*":
		result *= n
	elif oper == "/":
		result /= n
	output += " " + oper + " " + str(n)	
output += " = " + str(result)
print(output)


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)

gcd(4782, 698)
"""

print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
print("Уравнение прямой, проходящей через эти точки:")
if x_diff == 0:
	print("x =", x1)
elif y_diff == 0:
	print("y =", y1)
else:
	k = y_diff / x_diff
	b = y2 - k * x2
	print("y = ", k, " * x + ", b)



