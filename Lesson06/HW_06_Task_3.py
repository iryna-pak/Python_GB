"""
3.	Реализовать базовый класс Worker (работник).
●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
 {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""
"""
КОММЕНТАРИЙ УЧИТЕЛЯ!!!
Задача 3. self.income в родительском классе просили сделать защищенным. У вас он публичный (но это не беда)
В дочернем классе имеет смысл переопределять конструктор, если вы дополняете логику родительского класса или 
переопределяете ее полностью:

def __init__(self, name, surname, position, wage, bonus):
super().__init__(name, surname, position, wage, bonus)

Вот если вы уберете эти строчки у вас так же прекрасно будет все работать. При создании экземпляра дочернего класса
 будет вызван родительский конструктор даже без этих строк.
Имеет смылс переопределять конструктор в дочернем классе, если у вас новая логика в конструкторе, хотите дополнить 
логику родительского класса в конструкторе или если в конструкторе родительского класса объявлены приватные атрибуты 
(а мы помним, что приватные атрибуты работают только внутри текущего класса, и не работают даже в дочерних) и вы хотите,
 чтобы и эти приватные атрибуты были в дочернем классе, тогда да.
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f'{sum(self.income.values())}'


pos_on = Position("Vasya", "Vasilkov", "director", 20000, 10000)
print(pos_on.get_full_name())
print(pos_on.get_total_income())
print(pos_on.name)
print(pos_on.surname)
print(pos_on.position)
print(pos_on.income)

