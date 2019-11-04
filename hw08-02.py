"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    pass


print('Программа деления одного числа на другое')
numerator = input('Введите делимое ')
divider = input('Введите делитель ')

try:
    if divider == '0':
        raise OwnError('На ноль делить нельзя')
    print(f'{numerator} / {divider} = {(float(numerator) / float(divider)):.3f}')
except OwnError as err:
    print(err)
except ValueError:
    print('Введено не число')
