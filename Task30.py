# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите 1й элемент прогрессии: '))
n_1 = int(input('Введите разность прогрессии: '))
d = int(input('Введите кол-во элементов прогрессии: '))

list_prog = []
for i in range(d):
    list_prog.append(a1 + n_1*i)
print(list_prog)