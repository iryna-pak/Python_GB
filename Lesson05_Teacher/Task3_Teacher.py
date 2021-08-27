"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
"""
# sum = 0
#
# with open("File3") as file:
#     lines = file.readlines()
#     for line in lines:
#         surname, salary = line.split()
#         sum += int(salary)
#         if int(salary) < 20000:
#             print("Имеет оклад менее 20 тыс.: ", surname)
#
#     print("Среднеяя величина дохода сотрудников:", sum/len(lines))

print('\nЧасть 3')
with open("File3") as f_obj:
    content = f_obj.readlines()
    content = list(map(lambda n: n.rstrip(), content))
# print(content)
content = list(map(lambda n: n.split(), content))
min_20 = [n[0] for n in content if int(n[1]) < 20000]
# print('Сотрудники с зарплатой меньше 20 тыс.:', ', '.join(min_20))
# print(list(zip(*content)))
# print(list(zip(*content))[1])
# Эту схему как-то можно довести, чтобы получались в списке int, а не  str? В этой же строке, без нового цикла
# И я просто нашёл такой вариант получения элементов подсписков в интернете и не знаю что означает звёздочка
# И почему, интересно, не работает вот такая конструкция:
print(content[::][1])
# oklad = [int(n[1]) for n in content]
# print(f'Средняя зарплата: {(sum(oklad)/len(oklad)):.2f}')