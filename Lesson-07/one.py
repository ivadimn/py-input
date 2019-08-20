fruit1 = ['apple', 'orange', 'pineapple', 'banana']
fruit2 = ['apple', 'pineapple', 'banana', 'mango']


fruit3 = [fruit for fruit in fruit1 if fruit in fruit2]
print(fruit3)