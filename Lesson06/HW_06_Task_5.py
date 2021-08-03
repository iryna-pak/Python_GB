"""
5.	Реализовать класс Stationery (канцелярская принадлежность).
●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title}. Отрисовка ручкой"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title}. Отрисовка карандашом"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title}. Отрисовка маркером"


pen = Pen("Шариковая ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

print(pen.draw())
print(pencil.draw())
print(handle.draw())


