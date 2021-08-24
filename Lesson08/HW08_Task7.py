"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'

    def __add__(self, other):
        return f'Сумма c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c1 = ComplexNum(2, 3)
c2 = ComplexNum(4, 5)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)


