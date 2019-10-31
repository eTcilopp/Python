"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
...
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом первой
строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self,
                 height,
                 width,
                 row_list):
        self.height = height
        self.width = width
        self.matrix = row_list

    def __str__(self):
        self.matrix_string = ""
        for i in range(self.height):
            for j in range(self.width):
                self.matrix_string += str(self.matrix[i][j])
                self.matrix_string += '\t'
            self.matrix_string += '\n'
        return self.matrix_string

    def __add__(self, other):
        if self.width != other.width or self.height != other.height:
            return f'Операция не определена'
        self.sum_matrix = []
        for i in range(self.height):
            self.sum_matrix_line = []
            for j in range(self.width):
                self.sum_matrix_line.append(self.matrix[i][j] + other.matrix[i][j])
            self.sum_matrix.append(self.sum_matrix_line)
        return Matrix(self.height, self.width, self.sum_matrix)


m = Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
