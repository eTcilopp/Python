"""Создайте собственный класс-исключение, который должен проверять
содержимое списка на отсутствие элементов типа строка и булево.
Проверить работу исключения на реальном примере. Необходимо запрашивать
у пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.
"""


class MyExceptionError(Exception):
    pass

    @staticmethod
    def validate(el):

        if el == '':
            return False, el

        # Проверка на Boolean
        if el == 'True' or el == 'False':
            return False, el

        # Проверка на словарь, tuple и список
        if el[0] == '[' or el[0] == '(' or el[0] == '{':
            return True, (eval(el))

        # Проверка на число
        try:
            _ = float(el)
            return True, eval(el)
        except ValueError as err:
            return False, el


print('Вводите элементы списка. Нажимайте [Enter] после ввода каждого элемента.')
print('Нажмите [Enter] без ввод элемента, чтобы завершить ввод')
element = None
my_list = []
while element != "":
    try:
        element = input()
        validation = MyExceptionError.validate(element)
        if validation[0]:
            my_list.append(validation[1])
        elif validation[1] == "":
            break
        else:
            raise MyExceptionError
    except MyExceptionError:
        print('Введенный элемент списка относится к категории запрещенных')

print(f'Итоговый список, сотоящий из разрешенных элементов:\n{my_list}')
