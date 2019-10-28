"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Время перехода между
режимами должно составлять 7 и 2 секунды. Проверить работу примера, создав экземпляр и
вызвав описанный метод
"""

import time


class TrafficLight:
    __color = ''

    def running(self):
        now_time = time.time()
        color_code = now_time % 18 # Весь цикл составляет 7(Красный)+2(Желтый)+7(Зеленый)+2(Желтый) = 18 минут

        if color_code < 7:
            self.__color = 'Red'
        elif 9 <= color_code < 16:
            self.__color = 'Green'
        else:
            self.__color = 'Yellow'

        print(self.__color)

