"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
 уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self):
        self._dict = {}


class Officeequipment:
    def __init__(self, name):
        self.name = name


class Printer(Officeequipment):
    def __init__(self, name, make):
        super().__init__(name)
        self.make = make


class Scanner(Officeequipment):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year


class Copier(Officeequipment):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

