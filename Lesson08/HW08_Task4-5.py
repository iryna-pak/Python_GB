"""
4-5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
 определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
 других данных, можно использовать любую подходящую структуру, например словарь.
"""


class Storage:
    def __init__(self):
        self._dict = {}

    # добавляю в словарь обьект по его названию, в значении будет список экземпляров этого оборудования
    def add(self, Officeequipment):
        self._dict.setdefault(Officeequipment.group_name(), []).append(Officeequipment)

    # извлекаю из значения обьект по названию группы
    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Officeequipment:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.year}'


class Printer(Officeequipment):
    def __init__(self, name, price, year, series):
        super().__init__(name, price, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.price} {self.year}'


class Scanner(Officeequipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)


class Copier(Officeequipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)


storage = Storage()
scanner = Scanner('hp', '1111', 2005)
storage.add(scanner)
scanner = Scanner('hp', '2222', 2006)
storage.add(scanner)
printer = Printer('HP', 3333, 2018, 'S-256')
storage.add(printer)
print(storage._dict)
storage.extract('Scanner')
print(storage._dict)
