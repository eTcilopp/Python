"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор

"""

my_list = [66, 6, 8, 4, 6, 7, 1, 3, 2, 7, 500]

new_list = [el for i, el in enumerate(my_list) if el > my_list[max(i-1, 0)] or i == 0]

print(new_list)

# Ниже - вариант решения, при котором первый элемент отбрасывается, т.е. у него нет предыдущего элемента
# и его не с чем сравнивать

new_list2 = [el for i, el in enumerate(my_list) if el > my_list[max(i-1, 0)]]

print(new_list2)

