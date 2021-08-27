"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("File5", "w") as file_w:
     input_numbers = input("Введите числа через пробел: ")
     print(input_numbers, file=file_w)

with open("File5") as file:
     content_list = file.read().rstrip().split()
     print(content_list)
     numbers_list = [int(number) for number in content_list if number.isdigit()]
     print(numbers_list)
     print(sum(numbers_list))