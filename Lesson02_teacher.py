"""
1.  Создать список и заполнить его элементами различных типов данных.
    Реализовать скрипт проверки типа данных каждого элемента.
    Использовать функцию type() для проверки типа.
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [1, 'a', (1, 2, 3), {'Jun': 6, 'Jul': 7, 'Aug': 8}, [1, 2, 3], set([1, 2, 3])]

for element in my_list:
    print(type(element))

"""
2.  Для списка реализовать обмен значений соседних элементов, т.е.
    Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
    При нечетном количестве элементов последний сохранить на своем месте.
    Для заполнения списка элементов необходимо использовать функцию input().
"""

# input_list = input("Введите через пробел элементы списка: ")
# input_list = input_list.split()
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for index in range(0, len(input_list)-1, 2):
#     input_list[index], input_list[index+1] = input_list[index+1], input_list[index]
#
# print(input_list)

result_list = []
for element in input_list[::2]:
    index = input_list.index(element)
    if index+1 == len(input_list):
        result_list.append(element)
    else:
        first_element, second_element = input_list[index], input_list[index+1]
        result_list.extend([second_element, first_element])

print(result_list)

if __name__ == "__main__":
    pass

"""
3.  Пользователь вводит месяц в виде целого числа от 1 до 12.
    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
    Напишите решения через list и через dict.
"""
try:
    number_of_month = int(input("Введите номер месяца числом от 1 до 12: "))
except ValueError:
    print("Неверно введен номер месяца")
else:
    # winter = [12, 1, 2]
    # spring = [3, 4, 5]
    # summer = [6, 7, 8]
    # autumn = [9, 10, 11]
    #
    # if number_of_month in winter:
    #     print('Зима')
    # elif number_of_month in spring:
    #     print('Весна')
    # elif number_of_month in summer:
    #     print('Лето')
    # elif number_of_month in autumn:
    #     print('Осень')
    # else:
    #     print('Время года не определено')

    seasons_dict = {}
    seasons_dict = seasons_dict.fromkeys([12, 1, 2], 'Зима')
    seasons_dict.update({}.fromkeys([3, 4, 5], 'Весна'))
    seasons_dict.update({}.fromkeys([6, 7, 8], 'Лето'))
    seasons_dict.update({}.fromkeys([9, 10, 11], 'Осень'))

    # print(seasons_dict)

    # for season_month_number, season in seasons_dict.items():
    #     if number_of_month == season_month_number:
    #         print(season)
    #         break
    # else:
    #     print('Время года не определено')

    print(seasons_dict[number_of_month])

"""
4.  Пользователь вводит строку из нескольких слов, разделённых пробелами.
    Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
    Если в слово длинное, выводить только первые 10 букв в слове.
"""

input_string = input("Введите строку из нескольких слов: ")
input_words = input_string.split()

for index, word in enumerate(input_words, 1):
    print(index, word[:10])

"""
5.  Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
    У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
    с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""

my_rating_list = [7, 5, 3, 3, 2]
my_rating_list_copy = my_rating_list.copy()

new_rating = int(input("Введите новый элемент рейтинга: "))
try:
    if new_rating > my_rating_list[0]:
        my_rating_list_copy.insert(0, new_rating)
    elif new_rating < my_rating_list[-1]:
        my_rating_list_copy.append(new_rating)
    else:
        for rating in my_rating_list:
            if new_rating == rating:
                rating_index = my_rating_list.index(rating)
                rating_count = my_rating_list.count(rating)
                new_rang_index = rating_index + rating_count
                my_rating_list_copy.insert(new_rang_index, new_rating)
                break
            elif new_rating > rating:
                my_rating_list_copy.insert(my_rating_list.index(rating), new_rating)
                break
            else:
                continue
except IndexError:
    print("Неверные входные данные!")

print(my_rating_list_copy)

"""
6.  * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
    Каждый кортеж хранит информацию об отдельном товаре.
    В кортеже должно быть два элемента — номер товара и словарь с параметрами
    (характеристиками товара: название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
    Пример готовой структуры:
    [
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
    ]
"""

my_struct = []
while True:
    check_inputs = input("Продолжить ввод y/n: ")
    if check_inputs == 'y':
        my_dict = dict({'название': input("Введите название товара: "), 'цена': input("Введите цену товара: "),
                        'количество': input('Введите количество товара: '), 'eд': input("Введите единицу измерения: ")})
        my_struct.append((len(my_struct)+1, my_dict))
    elif check_inputs == 'n':
        break
    else:
        check_inputs = input("Продолжить ввод y/n: ")
print(my_struct)

"""
6.  * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
    Каждый кортеж хранит информацию об отдельном товаре.
    В кортеже должно быть два элемента — номер товара и словарь с параметрами
    (характеристиками товара: название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

    Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
     например название, а значение — список значений-характеристик, например список названий товаров.
    Пример:
    {
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
    }
"""

my_struct_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "упак."})
]

my_result_dict = {}

for structure in my_struct_list:
    struct_number, struct_info_dict = structure
    for key, value in struct_info_dict.items():
        value_list = my_result_dict.get(key, [])
        if value not in value_list:
            value_list.append(value)
        my_result_dict[key] = value_list

print(my_result_dict)