"""
Урок 1. Знакомство с Python
Практическое задание

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

"""
print()
print("Задача 1")
print()


time_sec = ""
while not time_sec.isnumeric() or int(time_sec) < 0:
    time_sec = input('Введите время в секундах ')

time_sec = int(time_sec)
hours = time_sec // 3600
minutes = time_sec % 3600 // 60
seconds = time_sec % 3600 % 60

print(f'{hours}:{minutes}:{seconds}')

"""
 2. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
print()
print("Задача 2")
print()


user_input = ""
while not user_input.isnumeric() or int(user_input) > 9:
    user_input = input('Введите число n ')

n = str(user_input)
summary = int(n) + int(n * 2) + int(n * 3)

print(f'{n} + {n * 2} + {n * 3} = {summary}')
"""
 3. Пользователь вводит целое положительное число.
 Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
"""
print()
print("Задача 3")
print()

user_input = ""
while not user_input.isnumeric() or int(user_input) < 0:
    user_input = input('Введите целое положительное число ')

max_digit = 0
user_input = str(user_input)
length = len(user_input)

while length > 0:
    length -= 1
    digit = int(user_input[length])
    if digit > max_digit:
        max_digit = digit
print(f'Самая большая цифра в числе {user_input} равна {max_digit}')

"""
4. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль -
выручка больше издержек или убыток - издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчете на одного сотрудника.
"""
print()
print("Задача 4")
print()

income = ""
expenses = ""

while not income.isnumeric():
    income = input('Введите значение выручки за период ')
income = int(income)

while not expenses.isnumeric():
    expenses = input('Введите значение издержек за период ')
expenses = int(expenses)

profit = abs(income - expenses)
profitability = ""

if(income > expenses ):
    result = "прибыль " + str(profit) + " ед"
    profitability ="Рентабельность выручки " + str(int(profit / income * 10000)/100) + " %"
elif (income < expenses):
    result = "убыток " + str(profit) + " ед"
else:
    result = "фирма работает \"в ноль\""

print(f'Результат работы фирмы: {result}. {profitability}')

if(income > expenses ):
    staff_qty = ""
    while not staff_qty.isnumeric() or int(staff_qty) <= 0:
        staff_qty = input('Введите численность сотрудников фирмы ')
    staff_qty = int(staff_qty)
    profit_per_person = profit / staff_qty
    print("Прибыль фирмы в расчете на одного сотрудника %.2f ед." % profit_per_person)

"""
Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на
10% относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно
натуральное число - номер дня.
"""
print()
print("Задача 5")
print()

a = ""
while not a.isnumeric() or int(a) <= 0:
    a = input('Введите результат первого дня, км: ')
a = float(a)
b = ""
while not b.isnumeric() or int(b) <= 0:
    b = input('Введите желаемый общий пробег, км: ')
b = float(b)

day = 1
day_run = a
total_run = a
while total_run <= b:
    day += 1
    day_run *= 1.1
    total_run += day_run

print(f'Результат спортсмена составит не менее {b} км на день № {day}')