"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
    практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название
    предмета и общее количество занятий по нему. Вывести словарь на экран.
"""
result_dict = {}
with open("File6") as file:
    for line in file:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '-']
        result_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})

print(result_dict)