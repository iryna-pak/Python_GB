"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translate_dict = {"One": "Один",
                  "Two": "Два",
                  "Three": "Три",
                  "Four": "Четыре",
                  "Five": "Пять",
                  "Six": "Шесть",
                  "Seven": "Семь"}

with open("File4") as file_read, open("File4_1", "w") as file_write:
    for line in file_read.readlines():
        text_number, number = line.rstrip().split(' - ')
        file_write.write(f'{translate_dict[text_number]} - {number}\n')