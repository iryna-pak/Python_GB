"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.
"""


class DivisionNull(Exception):
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider


while True:
    try:
        dividend = int(input("Введите делимое:  "))
        divider = int(input("Введите делитель:  "))
        if divider == 0:
            raise DivisionNull(dividend, divider)
        print(dividend / divider)
    except DivisionNull:
        print("Нельзя делить на ноль")
    except ValueError:
        print("Нельзя буквенные симфолы")


# raise DivisionNull() достаточно сделать так. коммент учителя

