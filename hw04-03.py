"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.

"""
solution_list = [el for el in range(20, 240) if not el % 21 or not el % 22]
print(solution_list)

