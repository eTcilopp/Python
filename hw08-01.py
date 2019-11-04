"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        self.date = date
        self.validated = self.validate(self.date)

    @staticmethod
    def validate(date):
        try:
            valLength = len(date) == 10
            valDD = 1 <= int(date[:2]) <= 31
            valMM = 1 <= int(date[3:5]) <= 12
            valYY = 0 <= int(date[6:])
            return valDD & valMM & valYY & valLength
        except ValueError:
            return False

    @classmethod
    def numbers(cls, date):
        if cls.validate(date):
            dd = int(date[:2])
            mm = int(date[3:5])
            yy = int(date[6:])
            return f'День: {dd}, месяц: {mm}, год: {yy}'
        else:
            return f'Дата не в формате ДД-ММ-ГГГГ'


a = Date.numbers('31-10-1974')
b = Date('01-11-2019')