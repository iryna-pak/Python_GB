"""
1.  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__() ),
    который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
    (двух матриц). Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
    складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for row in self.matrix:
            for el in row:
                my_str += f'{el:>10}'
            my_str += '\n'
        return my_str

    def __add__(self, other):
        add = []
        if len(self.matrix) != len(other.matrix):
            print('Please check matrixes dimensions')
            return
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print('Please check matrixes dimensions')
                return None
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(row)

        return Matrix(add)


my_m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'my_m1 = {my_m1}')
my_m2 = Matrix([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(f'my_m2 = {my_m2}')
print(f'my_m1 + my_m2 = {my_m1 + my_m2}')

"""
2.  Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
    этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
    для костюма (2*H + 0.3).
    Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
    Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
    проекта, проверить на практике работу декоратора @property .
"""

from abc import ABC, abstractmethod


class Stuff(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f'There is a new coat with size {self.param}')

    @property
    def get_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f'There is a new suit with height {self.param}')

    @property
    def get_consumption(self):
        return round(self.param * 2 + 0.3, 2)


my_coat = Coat(48)
print(f'Tissue consumption for my coat is: {my_coat.get_consumption}')
my_suit = Suit(1.78)
print(f'Tissue consumption for my suit is: {my_suit.get_consumption}')
print(f'The total issue consumption is: {my_coat.get_consumption + my_suit.get_consumption}')

print(Stuff.__dict__)

"""
3.
    Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
    вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
    (не целочисленное) деление клеток, соответственно.
    В методе деления должно осуществляться округление значения до целого числа.
    Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
    клеток.
    Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
    клеток больше нуля, иначе выводить соответствующее сообщение.
    Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
    ячеек этих двух клеток.
    Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
    количества ячеек этих двух клеток.
    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    Данный метод позволяет организовать ячейки по рядам.
    Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
    аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n**.
    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
    Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('num should be > 0')
            self.num = int(num)
        except TypeError:
            self.num = 1
            print('Check num value')
        except ValueError:
            print('Check num value')
            self.num = 1

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Subtraction is impossible')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)

cell_1 = Cell(12)
cell_2 = Cell(15)
# print(cell_1.make_order(4))
# print()
# print(cell_2.make_order(5))

cell_3 = cell_2-cell_1
print(cell_3)
print(cell_3.make_order(5))

# print(Cell.__dict__)