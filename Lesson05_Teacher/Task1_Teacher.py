"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
input_str = input("Введите следующую строку: ")
with open("File", "a") as file:
    while input_str:
        file.write(input_str+'\n')
        input_str = input("Введите следующую строку: ")