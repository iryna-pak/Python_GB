"""
1.  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def devision(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except TypeError:
        return "Неверные входные данные!"


print(devision(3, 4))
print(devision(13, 0))
print(devision(65, 5))
print(devision("65", 5))


"""
2.  Реализовать функцию, принимающую несколько параметров,
    описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
"""


def person_profile(**kwargs):
    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, E-mail: {kwargs['email']}"


print(person_profile(name="Aleksandra", tel="322-233-322", surname="Shapovalova",
                     birth_year=1993, city="Moscow", email="aleksandra.shapovalova@phystech.edu"))

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return sum(my_list[:2])


print(my_func(100, 10, 9))

"""
4.  Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y.
    Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

my_func_pow = lambda x, y: x**y


def my_func(x: int, y: int) -> float:
    if y > 0:
        return
    elif y == 0:
        return 1
    elif x <= 0:
        return
    else:
        # return 1/x*my_func(x, y+1)  # c помощью рекурсии

        x_pow_y = 1
        while y < 0:
            x_pow_y *= 1/x
            y += 1
        return x_pow_y


result = my_func_pow(2, -3)
print(result)
result = my_func(-2, -3)
print(result if result else "Неверные входные данные!")

"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_calc(input_string):
    input_list = input_string.split()
    my_sum = 0
    for el in input_list:
        if el:
            try:
                if el == "N":
                    return my_sum, False
                else:
                    my_sum += float(el)
            except ValueError:
                continue
    return my_sum, True


continue_flag = True
result_sum = 0
while continue_flag:
    input_string = input("Введите числа через пробел. Для остановки введите N: ")
    current_sum, continue_flag = sum_calc(input_string)
    result_sum += current_sum
    print("Промежуточная сумма: ", result_sum)
print("Результирующая сумма: ", result_sum)

"""
6.  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
    Каждое слово состоит из латинских букв в нижнем регистре.
    Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
    Необходимо использовать написанную ранее функцию int_func().
"""


int_func = lambda word: word.title()

input_string = input("Введите строку: ")
result_string_list = []
input_words = input_string.split()
for element in input_words:
    result_string_list.append(int_func(element))

print(" ".join(result_string_list))
