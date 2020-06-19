'''
date: 17.06.2020 / Version 1
author: AndreiM
https://github.com/AndreiMgbrains20/python/
lesson-7 / Python @GeekBrains
HomeWork 7.1 (hw-7.1.py, ..., hw-7.3.py)


1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.

'''

try:
    class Matrix:
        def __init__(self, a):
            self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
            lst = []
            for i in a:
                lst.append([j for j in i])
            self.a = lst

        def __str__(self):
            self.c = str(self.b)
            return self.c

        def __add__(self, other):
            n_line = len(self.a)
            n_column = len(other.a[0])
            for i in range(n_line):
                for j in range(n_column):
                    self.a[i][j] = self.a[i][j] + other.a[i][j]
                res = self.a
            return Matrix(res)


    matrix_1 = Matrix([[0, 1, 0, 2], [1, 0, 0, 1.2]])
    matrix_2 = Matrix([[2, 0, -1, 2], [-1, -2, 0, 1]])
    print('Результат сложения двух матриц 2x4: ')
    print(matrix_1 + matrix_2)

    matrix_1 = Matrix([[-1, 3, 2], [1, 0, 2], [1, 0, 0]])
    matrix_2 = Matrix([[2, 1, 5], [-2, 5, -1], [1, 2, 1]])
    print('Результат сложения двух матриц 3x3: ')
    print(matrix_1 + matrix_2)

    matrix_1 = Matrix([[-1, 3], [1, 2], [1, 0]])
    matrix_2 = Matrix([[1, 5], [5, -1], [2, 1]])
    print('Результат сложения двух матриц 3x2: ')
    print(matrix_1 + matrix_2)

except IndexError:
    print(f'Error. Матрицы должы быть одного порядка!')