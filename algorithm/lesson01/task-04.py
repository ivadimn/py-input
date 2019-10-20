# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

char1 = ord(input("Введите 1-й символ : ").lower())
char2 = ord(input("Введите 2-й символ : ").lower())
a = ord("a")
pos_char1 = char1 - a + 1
pos_char2 = char2 - a + 1
count_chars = char2 - char1 - 1
print(f"Позиция буквы {chr(char1)} в алфавите - {pos_char1}")
print(f"Позиция буквы {chr(char2)} в алфавите - {pos_char2}")
print(f"Между буквами {chr(char1)} и {chr(char2)} - {count_chars} букв")


