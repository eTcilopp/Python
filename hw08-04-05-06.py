"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""
import time


class WarehouseError(Exception):
    pass


class ReceivingError(WarehouseError):
    pass


class DispatchError(WarehouseError):
    pass


class TransitError(WarehouseError):
    pass


class OverCapacityError(WarehouseError):
    pass


class Warehouse:
    def __init__(self, name, capacity):
        self.warehouse_id = str(time.time())  #генерируется уникальный идентификатор склада
        self.name = name # user-friendly идентификатор склада
        self.capacity = capacity # максимальная емкость склада
        self.current_load = 0
        self.journal = [] # журнас приходов и расходов со склада

    def __add__(self, other):
        try:
            if other.current_location == self.name:
                raise ReceivingError
            if other.warehouse_id is not None:
                raise TransitError
            if (self.current_load + other.space_requirements) > self.capacity:
                raise OverCapacityError
            self.capacity -= other.space_requirements
            self.current_load += other.space_requirements
            self.journal.append({'operation_type': 'Receive',
                                 'product_type': other.type,
                                 'manufacturer': other.manufacturer,
                                 'time_stamp': time.time()})
            other.current_location = self.name
            other.warehouse_id = self.warehouse_id
        except ReceivingError:
            print('Товар уже находится на данном складе')
        except TransitError:
            print('Товар должет быть сначала списан с другого склада')
        except OverCapacityError:
            print('Склад переполнен. Товар не может быть принят')

    def __sub__(self, other):
        try:
            if other.current_location != self.name:
                raise DispatchError
            self.capacity += other.space_requirements
            self.current_load -= other.space_requirements
            self.journal.append({'operation_type': 'Dispatch',
                                 'product_type': other.type,
                                 'manufacturer': other.manufacturer,
                                 'time_stamp': time.time()})
            other.current_location = 'In Transit'
            other.warehouse_id = None
        except DispatchError:
            print('Данный товар отсутствует на складе')

    def inventory_report(self):  # Подготовка отчета об остатках
        report = []
        for transaction in self.journal:
            unique_identifier = transaction['product_type'] + transaction['manufacturer']
            unique_identifier = f"{transaction['product_type']} {transaction['manufacturer']}"
            operation = 1 if transaction['operation_type'] == 'Receive' else -1
            report.append((unique_identifier, operation, transaction['product_type'], transaction['manufacturer']))

        identifier_list = list(set([el[0] for el in report]))

        final_report = {}

        for equipment in identifier_list:
            current_stock = 0
            for transaction in report:
                if equipment == transaction[0]:
                    current_stock += transaction[1]
            if current_stock != 0:
                final_report[equipment] = current_stock
        return final_report


class Equipment:
    def __init__(self, manufacturer, model, space_requirements):
        self.manufacturer = manufacturer
        self.model = model
        self.space_requirements = space_requirements
        self.current_location = 'In Transit'
        self.warehouse_id = None


class Printer(Equipment):
    def __init__(self, manufacturer, model, space_requirements=1):
        super().__init__(manufacturer, model, space_requirements)
        self.type = 'Printer'


class Computer(Equipment):
    def __init__(self, manufacturer, model, space_requirements=1):
        super().__init__(manufacturer, model, space_requirements)
        self.type = 'Computer'


class Scanner(Equipment):
    def __init__(self, manufacturer, model, space_requirements=1):
        super().__init__(manufacturer, model, space_requirements)
        self.type = 'Scanner'


w1 = Warehouse('Regional', 1000)
p1 = Printer('HP', 'LX12')
p2 = Printer('Canon', "CZ321")
w1 + p1
w1 + p2
w2 = Warehouse('Local', 200)
w1 - p2
w1 + p2
print(w1.inventory_report())
print(w2.inventory_report())
