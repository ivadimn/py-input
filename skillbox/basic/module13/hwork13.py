def exponent(number):
   exp = 0
   while number >= 10 or number < 1:
       if number >= 10:
            number /= 10
            exp += 1
       elif number < 1:
           number *= 10
           exp -= 1
   return exp, number

x = float(input("Введите число больше 0: "))
exp, x  = exponent(x)
print("x =", x, "* 10 **", exp)