# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не 
# больше заданного максимума)

import random
n = int(input('Input length of the array: '))
listn = [random.randint(0,10) for i in range(n)]
print(listn)

min_value = int(input('Input minimum: '))
max_value = int(input('Input maximum: '))

list_res = []
for i in range(n):
    if listn[i] >= min_value and listn[i] <= max_value:
        list_res.append(i)

print(list_res)

