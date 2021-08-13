"""
2.	Реализовать класс Road (дорога).

●	определить атрибуты: length (длина), width (ширина);
●	значения атрибутов должны передаваться при создании экземпляра класса;
●	атрибуты сделать защищёнными;
●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в
1 см*число см толщины полотна;
●	проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _length = None
    _width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):  # конструктор класса Road
        self._length = length
        self._width = width

    def mass(self):
        self.weigth = 25
        self.tickness = 5
        mass = self._length * self._width * self.weigth * self.tickness  # масса асфальта
        return f"Необходимая масса асфальта для покрытия всей дороги: {mass}"


road = Road(20, 5000)
print(road.mass())