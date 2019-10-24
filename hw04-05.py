"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""
from functools import reduce


def my_range(start, end, step):
    return range(start, end + 1, step)


my_list = [el for el in my_range(100, 1000, 2)]

print(reduce(lambda x, y: x*y, my_list))

