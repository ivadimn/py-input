# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
#  Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака

bit_and = 5 & 6
bit_or = 5 | 6
bit_xor = 5 ^ 6

bit_left = 5 << 2
bit_right = 5 >> 2

print(f"Побитовое AND 5 & 6 = {bin(bit_and)}")
print(f"Побитовое OR 5 | 6 = {bin(bit_or)}")
print(f"Побитовое  XOR 5 ^ 6 = {bin(bit_xor)}")
print(f"Побитовый сдвиг влево 5 << 2 = {bin(bit_left)}")
print(f"Побитовый сдвиг вправо 5 >> 2 = {bin(bit_right)}")
