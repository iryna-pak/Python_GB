"""
4.	Реализуйте базовый класс Car.
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
 turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""
"""
КОММЕНТАРИЙ УЧИТЕЛЯ
Задача 4. Вот тут я тоже не вижу смысла переопределять конструктор. Если вы уберете строчки переопределения констуктора 
из дочернего класса, то у вас все будет прекрасно работать.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return "go"

    def stop(self):
        return "stop"

    def turn_left(self):
        return "turn left"

    def turn_right(self):
        return "turn right"

    def show_speed(self):
        return "speed is normal"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "over speed."
        else:
            return "normal speed"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "over speed."
        else:
            return "normal speed"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


sportCar = SportCar(100, 'grey', 'Toyota', False)
townCar = TownCar(30, 'blue', 'Acura', False)
workCar = WorkCar(80, 'white', 'BMW', True)
policeCar = PoliceCar(120, 'black',  'Mercedes', True)

print(f"{sportCar.name} {sportCar.go()}")
print(f"{townCar.name} {townCar.stop()}")
print(f"When {workCar.name} {workCar.go()} then {policeCar.name} {policeCar.stop()}")
print(f"{sportCar.name} is {sportCar.color}")
print(f"{policeCar.name} is {policeCar.color}")
print(f"Is {policeCar.name} a police car? {policeCar.is_police}")
print(f"Is {townCar.name}  a police car? {townCar.is_police}")
print(f"{townCar.name} {townCar.turn_right()} then {workCar.name} {workCar.turn_left()}")
print(f"{townCar.name} - {townCar.show_speed()}")
print(f"{workCar.name} - {workCar.show_speed()}")


