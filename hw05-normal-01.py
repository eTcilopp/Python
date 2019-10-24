"""
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

"""
import os

import hw05_easy_00


def goto_folder():
    print('Подпрограмма перехода в другую директорию')
    folder_name = input('Введите имя директории для перехода ')
    try:
        os.chdir(folder_name)
        print(f'Успешно выполнен переход в директорию {folder_name}')
        print(f'Текущая директория {os.getcwd()}')
    except FileNotFoundError as e:
        print(f'Не удалось выполнить переход в директорию {folder_name}')


def view_folder_content():
    print('Подпрограмма просмотра содержимого текущей директории')
    # Определяем текущую директорию
    path = os.getcwd()

    print(f'Текущая директория: {path}')

    print('Поддиректории в текущей директории:')
    hw05_easy_00.folder_list(path)

    print('Файлы в текущей директории:')
    files = [el for el in os.listdir(path) if os.path.isfile(el)]
    if len(files) > 1:
        for file in files:
            print(file)
    else:
        print('В текущей директории файлов не обнаружено')


def remove_folder():
    print('Подпрограмма удаления директории')
    folder_name = [None]
    folder_name[0] = input('Введите название удаляемой директории ')
    hw05_easy_00.delete_folder(folder_name)


def create_folder():
    print('Подпрограмма создания директории')
    folder_name = [None]
    folder_name[0] = input('Введите название создаваемой директории ')
    hw05_easy_00.create_new_folder(folder_name)


menu = {
    '1': ('Перейти в папку', goto_folder),
    '2': ('Просмотреть содержимое текущей папки', view_folder_content),
    '3': ('Удалить папку', remove_folder),
    '4': ('Создать папку', create_folder),
}

while True:
    print('МЕНЮ:')
    for el in menu:
        print(el, menu[el][0])

    print()
    selected = input('Выберите действие ')

    try:
        menu[selected][1]()
        _ = input('Нажмите Enter для продолжения')
    except KeyError as e:
        print('Выбрано несуществующее действие')
    except ValueError as e:
        print('Введено не число')

