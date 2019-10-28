"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
surname , position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
дохода с учетом премии ( get_full_profit) . Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).

"""


class Worker:
    dict_bonuses = [
        {"profit": 30000, "bonus": 20},
        {"profit": 40000, "bonus": 25},
        {"profit": 50000, "bonus": 30},
        {"profit": 60000, "bonus": 50}
    ]

    def __init__(self, name, surname, position, __profit):
        self.name = name
        self.surname = surname
        self.position = position
        self.__profit = __profit
        for record in self.dict_bonuses:
            if record['profit'] == self.__profit:
                self.bonus = record['bonus']
                break
            self.bonus = 0


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return self._Worker__profit * (1 + self.bonus / 100)
