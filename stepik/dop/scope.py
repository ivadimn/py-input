def fib():
   a, b = 0, 1
   yield a
   yield b

   while True:
      a, b = b, a + b
      yield b

index = 0
for num in fib():
   print(num)
   if index == 0
      continue
   if index == 10:
      break