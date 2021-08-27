from sys import argv


script_name, productivity, rate_per_hour, bonus = argv
print("Name of script: ", script_name)
print('Productivity, hours: ', productivity)
print('Rate per hour: ', rate_per_hour)
print('Bonus: ', bonus)
print('Salary: ', int(productivity) * int(rate_per_hour) + int(bonus))

"""
2.  Представлен список чисел.
    Необходимо вывести элементы исходного списка,
    значения которых больше предыдущего элемента.

    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
    Для его формирования используйте генератор.
"""

from itertools import count, cycle

my_list = ["ABC", "www"]
counter = 1
for i in cycle(my_list):
    print(i)
    counter += 1
    if counter > 10:
        break
# start_from = 1
# for elem in count(start_from):
#     print(elem)
#
# list = [1, 2, 3]


# def task_2():
#     my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#     print(f'Исходный список: {my_list}')
#
#     result_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index-1]]
#
#     print(f'Результат: {result_list}')
#
#
# if __name__ == "__main__":
#     task_2()

"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""

result = [element for element in range(20, 241) if element % 20 == 0 or element % 21 == 0]
print(result)

"""
4.  Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке
    их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
    Результат: [23, 1, 3, 10, 4, 11]
"""

from random import randint

source_list = [randint(0, 10) for i in range(20)]
print(f'Исходный список: {source_list}')

result = [el for el in source_list if source_list.count(el) == 1]
print(f'В списке не повторяются числа: {result}')

"""
5.  Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы).
    Необходимо получить результат вычисления произведения всех элементов списка.

    Подсказка: использовать функцию reduce().
    [1, 2, 3, 4] (((1+2)+3)+4)+5)+6...
"""
a = lambda x, y, z: x+y+z
b = a([1, 2, 3], [2, 3, 4], [4, 6, 7])
print(b)
from functools import reduce

sourse_list = [el for el in range(100, 1001, 2)]
# print(sourse_list)

# result = reduce(lambda x, y: x*y, sourse_list)
# print(result)

"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
"""
from itertools import count, cycle
import sys

start_from = 10
iterable = "ABCDEF"
iterations_count = 0

# def integer_generator(start_from):
#     for el in count(start_from):
#         if el > start_from+10000:
#             break
#         yield el

# for el in integer_generator(15):
#     print(el)

# gen = integer_generator(10)
# print(sys.getsizeof(gen))
# print(sys.getsizeof(list(gen)))

for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 3:
        print(el)
    else:
        break

"""
7.  Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
    for el in fact(n).
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
    начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce
from itertools import count
from math import factorial


def fact(n):
    result = 1
    for i in count(1):
        if i <= n:

            print(i)
            # result = factorial(i)
            # result = reduce(lambda x, y: x*y, range(1, i+1))
            yield result
        else:
            break

for el in fact(10):
    pass
    # print(el)