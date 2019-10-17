"""
1.Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.

"""

def divide(arg_1, arg_2):
    try:
        result = int(arg_1) / int(arg_2)
    except ZeroDivisionError as e:
        return 'Попытка делить на 0'
    except ValueError as e:
        return 'Один из аргументов не является числом'
    return f'Результат деления {numerator} на {denominator} равен {result:.2f}'

numerator = input("Введите числитель ")
denominator = input("Введите знаменатель ")


print(f'{divide(numerator, denominator)}')


