# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
size = int(input('Введите кол-во чисел: '))
number = int(input('Введите число для проверки: '))

my_list = list()
for i in range(size):
    my_list.append(randint(0,100))

print(*my_list)
min_dist = float('inf')
nearest = my_list[0]

for item in my_list:
    if abs(number-item)<min_dist:
        min_dist = abs(number-item)
        nearest = item

print(f'Ближайщее число к {number} будет {nearest}')
