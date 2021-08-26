"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
 определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
 данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
 для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Недостаточно техники на складе!")
        except KeyError:
            print("Нет такого типа оргтехники на складе!")
    return wrapper


class Storage:
    """
    equipment_units имеет следующую структуру
    equipment_units = {
    "equipment_type": {
    "name": {
    "model": {
    "count": ""
    }
    }
    }
    }
    """
    equipment_units = {}    # формирование пустого словаря для хранения оргтехники на складе

    @classmethod    # чтобы не делать как экзмепляр класса, делаем методом класса, чтобы иметь достутп к словарю
    # equipment_units по ссылке cls
    @validate   # декоратор валидации (прописан заранее функцией validate) для проверки есть ли такие ключи по которым
    # хотят добавить товар
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]["count"] += unit_count

    @classmethod
    @validate   # декоратор валидации для проверки есть ли такие ключи по которым хотят забрать товар
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]["count"]
        if current_count < unit_count:  # и есть ли достаточное количсетво товара
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]["count"] -= unit_count

    @staticmethod
    def get_all_equipment():
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in [int, float]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Неверный формат входных данных!")
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):  # проверка есть ли уже в словаре такое имя, модель и обновление списка оргтехники
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model["count"] += self.__count
                # если уже есть какое оборудование под ключами имя и модель, добавляем
            else:
                equipment_storage_info_by_name[self.model] = {"count": self.__count}
        else:
            equipment_storage_info[self.name] = {
                self.model: {"count": self.__count}
            }

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, "Printer", count)
        self.colors = colors


class Notebook(Equipment):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(name, model, "Notebook", count)
        self.ram = ram
        self.system_type = system_type


my_printer_1 = Printer("Hp", "XS5050", 2000, ['red', "blue", "green"])
my_printer_2 = Printer("Canon", "TS304", 500, ['black'])
my_printer_3 = Printer("Xerox", "B210", 1700, ['red', "blue", "green"])
my_printer_4 = Printer("Xerox", "B210", 1300, ['red', "blue", "green"])
my_printer_5 = Printer("Xerox", "B211", 200, ['red', "blue", "green"])

my_notebook_1 = Notebook("Lenovo", "ThinkPad X1", 2300, 8, 'Windows')
my_notebook_2 = Notebook("Mac", "MacBookAir", 3200, 8, 'MacOS')

Storage.storage_to(unit_type="Printer", unit_name="HP", unit_model="XS5050", unit_count=100)
Storage.get_all_equipment()

Storage.storage_from(unit_type="Notebook", unit_name="Lenovo", unit_model="ThinkPad X1", unit_count=400)
Storage.get_all_equipment()