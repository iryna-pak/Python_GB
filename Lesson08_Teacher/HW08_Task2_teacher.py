"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.
"""


class ErrDivision(Exception): # Свой класс исключение наследуется от класса Исключение
    def __init__(self):
        self.txt = "My division by zero"


def division(divident, divisor):
    try:
        if divisor == 0:
            raise ErrDivision
        print(divident / divisor)
    except ErrDivision as err:
        print(err.txt)


division(5, 0)
division(5, 3)