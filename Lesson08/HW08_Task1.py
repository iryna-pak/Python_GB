"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
 года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def extract(cls, dd_mm_yy):
        my_date = []
        for i in dd_mm_yy.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(dd, mm, yy):
        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if 2021 >= yy >= 0:
                    return f'Дата указана корректно'
                else:
                    return f'Неверно указан год'
            else:
                return f'Такого месяца не существует'
        else:
            return f'Такого дня не существует'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.dd_mm_yy)}'


data = Data('10 - 8 - 2021')
print(data)
print(Data.valid(1, 1, 2022))
print(data.valid(1, 13, 2011))
print(Data.valid(10, 8, 2021))
print(Data.valid(0, 11, 2000))
print(Data.extract('11 - 11 - 2011'))
print(data.extract('11 - 11 - 2020'))

