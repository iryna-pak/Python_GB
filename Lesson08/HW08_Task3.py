"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
    Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
    работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
    Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NotNumberError(Exception):
    def __init__(self, my_list):
        self.my_list = my_list
#    pass


my_list = []
while True:
    try:
        value = input("Введите число списка, или 'stop' для выхода: ")
        if value == "stop":
            break
        if not value.isdigit():
            raise NotNumberError(value)
        my_list.append(int(value))
    except NotNumberError as e:
        print('Введены недопустимые символы!', e)
print(my_list)
