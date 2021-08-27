"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("File") as file:
    file_lines = file.readlines()
    print("Количество строк в файле: ", len(file_lines))
    for line_number, line in enumerate(file_lines, 1):
        print(f"Количество слов в строке {line_number}:", len(line.split()))

# with open('File', 'r') as f_obj:
#     content = f_obj.readlines()
#     print(content)
#     print('Кол-во строк в файле:', len(content))
#     for i in range(0, len(content)):
#         #разбиваем кортеж на строки
#         print(len(content[i].split()))
#         print('Кол-во слов в строке ', i+1, 'равна',len(content[i].split()))