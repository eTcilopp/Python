"""
2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""

def user_info (param_1, param_2, param_3, param_4, param_5, param_6):
    return f'Имя пользователя: {param_1}, его фамилия: {param_2}, год рождения: {param_3}. Город проживания - {param_4}.\nСвязаться можно по электронной почте {param_5} или по телефону {param_6}. '


name = input('Введите имя пользователя ')
last_name = input('Введите фамилию пользователя ')
yob = input('Введите год рождения пользователя ')
city = input('Введите город, в котором живет пользователь ')
email = input('Введите адрес электронной почты пользователя ')
phone = input('Введите номер телефона пользователя ')

print(user_info(param_1=name, param_2=last_name, param_3=yob, param_4=city, param_5=email, param_6=phone))