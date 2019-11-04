"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

"""


class C_Number:
    def __init__(self, i, j):
        self.i = int(i)
        self.j = int(j)

    def __add__(self, other):
        return C_Number(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return C_Number(self.i - other.i, self.j - other.j)

    def __str__(self):
        return f"{self.i}{'+' if self.j > 0 else '-'}{abs(self.j) if abs(self.j) != 1 else ''}j"


z1 = C_Number(10, 10)
z2 = C_Number(5, 2)
z3 = z1 / z2
print(z3)
