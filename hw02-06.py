"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
] 
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров. 
Пример: 
{ “название”: [“компьютер”, “принтер”, “сканер”], “цена”: [20000, 6000, 2000], “количество”: [5, 2, 7], “ед”: [“шт.”] }
"""

data = [ (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}), (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}), (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}) ]


# Добавление нового товара
proceed = ''

while proceed != 'n':

    name = input('Введите название товара ')
    price = input('Введите цену товара ')
    price = int(price)
    qty = input('Введите количество товара ')
    qty = int(qty)
    unit = input('Введите единицу измерения товара ')

    # Определяем незанятый номер товара

    index = 0
    for i in data:
        if i[0] > index:
            index = i[0]
    index += 1

    # Создаем новый кортежа

    new_record =(index, {"название": name, "цена": price, "количество": qty, "ед": unit})

    # Добавление нового кортежа в список

    data.append(new_record)
    
    # запрашиваем пользователя, продолжать ли ввод данных
    proceed = input('Ввести данные о другом товаре? (ENTER  - прололжить N - завершить) ')
    
# СБОР АНАЛИТИКИ

# Формируем новый пустой словарь
a_dict = {}

# Получаем список всех ключей - характеристик товара
keys = (data[0][1]).keys()
#Формируем список свойств товаров и собираем из ключа и списка словарь, добавляя его в a_dict
for key in keys:
    a_list=[]
    for record in data:
        a_list.append((record[1]).get(key))
    a_dict[key] = a_list
print(f'Аналитический словарь\n{a_dict}')


# Работа с аналитикой - получение свойсв товара по ключу
answer = ''
while answer != "N":
    answer = input('Введите ключ? (N - завершить) ')
    print(a_dict.get(answer))
