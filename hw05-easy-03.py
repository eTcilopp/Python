"""
Задача-3:
Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

"""

import os

import shutil


from itertools import count


# Определяем имя текущего файла
current_filename = os.path.realpath(__file__)

base, extension = os.path.splitext(current_filename)

# Генерируем имена файлов, опредеяем, есть ли уже такой файл, выполняем копирование, если нет.
for el in count(0):
    new_file_name = f'{base}-Copy {str(el)}{extension}'
    if not os.path.exists(new_file_name):
        try:
            shutil.copy(current_filename, new_file_name)
            print('Копирование выполнено успешно')
            break
        except IOError as e:
            print('При копировании файла произошла ошибка')



