"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.

"""
from itertools import count

from itertools import cycle


# Задача 1

first_el = 2  # - указывается первый элемент, генерируемый генератором

for el in count(first_el):
    if el <= 15: # ограничиваем цикл 15ю итерациями
        print(el)
    else:
        break
# Задача 2

mylist = [1, 2, 3, 'a', 'b', 'c']

limit = 15 # задаем предельное значение числа итераций
cycles = 0 # счетчик итераций
for el in cycle(mylist):
    if cycles < limit:
        print(el)
        cycles += 1
    else:
        break



