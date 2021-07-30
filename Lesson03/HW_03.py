# 1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
print('\n************* Task №1 **************')


def my_division(*args):
    try:
        arg_1 = int(input("Enter first number: "))
        arg_2 = int(input("Enter second number: "))
        division = arg_1 / arg_2
    except ZeroDivisionError:
        return "Wrong number! The dividend cannot be zero."
    except ValueError:
        return "Only numbers are allowed to enter!"
    return division


print(f"Result:  {my_division()}")

# 2.Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

print('\n************* Task №2 **************')


def my_user(**kwargs):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    year_of_birth = input("Enter year of birth: ")
    city_of_residence = input("Enter city of residence: ")
    email = input("Enter email: ")
    telephone_number = input("Enter telephone number: ")
    return name, surname, year_of_birth, city_of_residence, email, telephone_number


print(f"Check the data you entered: {my_user()}")
"""
!!!!!!!!!!!!!!!!!!!!Комментарий Преподавателя!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Вот тут как раз функция должна была принимать все значения name, surname... как именнованные аргументы. 
Поэтому лучше задание значений для переменных построить вне функции. А в функцию уже передать их значения с 
указанием их имени.
"""

# 3.Реализовать функцию my_func(),кот-ая прини-т три позиционных аргумента и возвращает сумму наибольших двухаргументов.
print('\n************* Task №3 - Version №1 **************')


def my_func_sum(*args):
    sum1 = args[0] + args[1]
    sum2 = args[1] + args[2]
    sum3 = args[0] + args[2]
    if sum1 > sum2 and sum1 > sum3:
        return sum1
    elif sum2 > sum1 and sum2 > sum3:
        return sum2
    else:
        return sum3


task_done = False
while not task_done:
    try:
        print(f'Sum of biggest arguments - {my_func_sum(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))}')
        task_done = True
    except ValueError:
        print("Only numbers are allowed to enter!")


print('\n************* Task №3 - Version №2 **************')


def my_func_sum1(*args):
    if len(args) < 2:
        return 0
    max_value = max(args)
    pre_max_value = min(args)
    for i in range(len(args)):
        if args[i] > pre_max_value and args[i] != max_value:
            pre_max_value = args[i]
    return pre_max_value + max_value


task_done = False
while not task_done:
    try:
        print(f'Sum of biggest arguments - {my_func_sum1(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))}')
        task_done = True
    except ValueError:
        print("Only numbers are allowed to enter!")
"""        
!!!!!!!!!!!!!!!!!!!!Комментарий Преподавателя!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Очень здорово, что вы организовали 2 варианта решения задачи!
Мне нравится больше второй, первый довольно топорный и не такой универсальный как второй.
Можно было сначала найти максимум из текущего списка. Этот максимум удалить и найти второй максимум из оставшегося 
списка. Я на уроке еще демонстрировала сортировку. Отсортирвали, взяли срез (необходимое количество элементов) и 
нашли сумму элементов среза.
"""
# 4.	Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
print('\n************* Task №4 **************')


def my_func(x, y):
    return x ** y


print(f'Result - {my_func(int(input("Enter first number: ")), int(input("Enter second number: ")))}')

# 5.	Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.
print('\n************* Task №5 **************')


def my_summ():
        summ = 0
        to_quit = False
        while not to_quit:
            res = 0
            enter = input("Enter numbers or Q to exit: ").split()
            for el in range(len(enter)):

                if enter[el].isnumeric():
                    res = res + int(enter[el])
                else:
                    to_quit = True
                    break
            summ = summ + res
            print(f'Current sum is {summ}')
        print(f'Your total sum is {summ}')


my_summ()

# 6.	Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
print('\n************* Task №6 **************')


def int_func(word):
    return word.capitalize()


print(int_func(input("Enter word in lower case: ")))

# 7.	Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
print('\n************* Task №7 **************')


def int_func1():
    phrase = input("Enter your words in lower Latin case: ").split()
    title_phrase = ""
    for i in range(len(phrase)):
        title_phrase += int_func(phrase[i]) + ' '
    return title_phrase


print(int_func1())

"""
!!!!!!!!!!!!!!!!!!!!Комментарий Преподователя!!!!!!!!!!!!!!!!!!!!!!
Задача 6 (у вас 7)
Помните функцию, противоположную split (разделение по разделителю).
Есть и "соединитель" с соединителем=) И эта функция join.
Вот такую запись:

for i in range(len(phrase)):
title_phrase += int_func(phrase[i]) + ' '

Можно с помощью join сделать:

" ".join(phrase)

Сначала мы пишем строковый соединитель, вызываем функцию join через точку и в круглых скобках указываем список 
элементов строкового типа данных, который нужно преобразовать в одну строку.
"""