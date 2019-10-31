# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


# Функция создния новых директорий (для решения задачи 1)
def create_new_folder(directory):
    try:
        for dir_name in directory:
            os.mkdir(dir_name)
        print('Создание произведено успешно')
    except IOError as e:
        print('При создании директорий произошла ошибка')


# Функция удаления директорий (для решения задачи 1)

def delete_folder(directory):
    try:
        for dir_name in directory:
            if os.path.exists(dir_name):
                os.rmdir(dir_name)
        print('Удаление произведено успешно')
    except IOError as e:
        print('При удалении директорий произошла ошибка')


# Функция, отображающая перечень директорий (для решения задачи 2)

def folder_list(folder_path):
    folders = [el for el in os.listdir(folder_path) if os.path.isdir(el)]
    if len(folders) > 1:
        for folder in folders:
            print(folder)
    else:
        print('В текущей папке директорий не обнаружено')


if __name__ == "__main__":

    # Решение Задачи 1
    # Определяем папку, из коротой запущен данный скрипт
    path = os.path.dirname(os.path.realpath(__file__))

    # Генерируем имена директорий dir_1 - dir_9 вместе с путем
    dir_list = [os.path.join(path, 'dir_' + str(el)) for el in range(1, 10)]

    # Создаем новые директории
    create_new_folder(dir_list)

    _ = input('Нажмите Enter для продолжения ')

    # Решение задачи 2
    # Отображаем содержимое текущей директории
    folder_list(path)

    _ = input('Нажмите Enter для продолжения ')

    # Решение задачи 1 (продолжение)
    # Удаляем новые директории
    delete_folder(dir_list)


