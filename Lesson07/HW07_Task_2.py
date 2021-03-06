"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
 (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, width):
        self.width = width

    @property
    def consumption(self):
        return self.width / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на пальто {self.consumption:.2f}'


class Suit(Clothes):
    def __init__(self,height):
        self.height = height

    @property
    def consumption(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на костюм {self.consumption:.2f}'


coat = Coat(2)
suit = Suit(2)
print(coat)
print(suit)
print(f'Общий расход ткани: {coat.consumption + suit.consumption:.2f}')
