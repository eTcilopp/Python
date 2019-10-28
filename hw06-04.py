"""
Опишите несколько классов: TownCar , SportCar , WorkCar , PoliceCar . У каждого класса
должны быть следующие атрибуты: speed , color , name , is_police (булево). А также несколько
методов: go , stop , turn(direction) , которые должны сообщать, что машина поехала,
остановилась, повернула (куда).

"""


class Car:
    car_speed = 0
    car_azimuth = 0  # Ввел дополнительную переменную для отслеживания направления движения
    car_color = 'White'
    car_name = 'Tesla'
    car_is_police = False

    def go(self):
        self.car_speed += 10  # Скорость увеличивается на 10 при каждом вызове метода go
        print('Машина поехала')

    def stop(self):
        self.car_speed = 0   # Машина остановилась, значит, скорость равна нулю
        print('Машина остановилась')

    def turn(self, direction):
        dict_translate = {'left': ('налево', -90), 'right': ('направо', 90)}
        self.car_azimuth += dict_translate.get(direction)[1]
        self.car_azimuth %= 360  # Возможно, намудрил, однако, так не нужно переключать раскладку каждый раз
        print(f'Машина повернула. Направление поворота: {dict_translate.get(direction)[0]}.')


class TownCar(Car):

    def __init__(self, **kwargs):  # Использовал kwargs, чтобы при создании объекта можно было задавать или не задавать параметры
        self.__dict__.update(car_type='Town Car')
        self.__dict__.update(kwargs)


class SportCar(Car):

    def __init__(self, **kwargs):
        self.__dict__.update(car_type='Sport Car')
        self.__dict__.update(kwargs)


class WorkCar(Car):
    def __init__(self, **kwargs):
        self.__dict__.update(car_type='Work Car')
        self.__dict__.update(kwargs)


class PoliceCar(Car):
    def __init__(self, **kwargs):
        self.__dict__.update(car_type='Police Car')
        self.__dict__.update(car_is_police=True)
        self.__dict__.update(kwargs)
