import json

print('\n************* Task №1 **************')
# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

openFile = open("Task_1.txt", "w", encoding="utf-8")
while True:
    user_Input = input("Enter your text. Empty input will terminate the program:   ")
    if len(user_Input) > 0:
        user_Input += "\n"
        openFile.write(user_Input)
    else:
        print("Empty input.\nExit.\n")
        break
openFile.close()

openFile = open("Task_1.txt", "r", encoding="utf-8")
content = openFile.readlines()
print(f"Эта запись находится в файле Task_1.txt - {content}")
openFile.close()

print('\n************* Task №2 **************')
# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.
openFile1 = open("Task_2.txt", "w", encoding="utf-8")
openFile1.write("Мороз и солнце, день чудесный!\n")
openFile1.write("Зима! Крестьянин, торжествуя,\n")
openFile1.write("Наладил санок быстрый бег.\n")
openFile1.write("Ему кричат: 'Какого __я?!\n")
openFile1.write("Ещё нигде не выпал снег!!'\n")
openFile1.close()

openFile1 = open("Task_2.txt", "r", encoding="utf-8")

allStrings = openFile1.readlines()
print(f"Count strings: {len(allStrings)}.")
"""
КОММЕНТАРИЙ УЧИТЕЛЯ!
Задача 2. Возможно (я не настаиваю) метод enumerate облегчил бы создание вот этой записи

for i in range(len(allStrings)):
print(f"String {i} contains {len(allStrings[i].split())} words")
"""
for i in range(len(allStrings)):
    print(f"String {i} contains {len(allStrings[i].split())} words")

openFile1.close()

print('\n************* Task №3 **************')
# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

openFile2 = open("Task_3.txt", "r", encoding="utf-8")
employee = openFile2.read().split('\n')
print(employee)

salary = []
average = []

for i in employee:
    i = i.split()
    if int(i[1]) < 20000:
        salary.append(i[0])
    average.append(int(i[1]))

print(f"Сотрудники с зарплатой меньше 20000: {salary}.\nСредний доход равен {sum(average)/len(average):.2f}")
openFile2.close()


print('\n************* Task №4 **************')
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
newList = []

with open('Task_4.txt', 'r') as file_obj1:
    for i in file_obj1:
        q = i.split(" - ")
        newList.append(translate[q[0]] + " - " + q[1])
    print(newList)


with open('Task_4_new.txt', 'w', encoding="utf-8") as file_obj2:
    file_obj2.write(str(newList))
print(newList)

print('\n************* Task №5 **************')
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('Task_5.txt', 'w+') as file_obj:
    user = input('Введите цифры через пробел:  ')
    file_obj.write(user)
    numm = user.split()

    print(f"Сумма введённых цифр равна {sum(map(int, numm))}")      # map - функция преобразования. Конвертация в числа

print('\n************* Task №6 **************')
# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                        Физика:   30(л)   —   10(лаб)
#                                        Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

result = {}
with open('Task_6.txt', 'r') as file_obj:
    for i in file_obj:
        subject, lecture, practice, laboratory = i.split()
        result[subject] = int(lecture) + int(practice) + int(laboratory)
    print(f'Общая сумма часов по предмету:\n{result}')

print('\n************* Task №7 **************')
# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
profit = {}
average_profit = {}
profitable_companies = 0
total_profit = 0
result = []

with open('Task_7.txt', 'r') as file:
    for i in file:
        firma, sobst, procceds, costs = i.split()
        profit[firma] = int(procceds) - int(costs)
        if profit[firma] >= 0:
            print(f"{firma} - {profit[firma]}")
            total_profit += (profit[firma])
            profitable_companies += 1
    print(f"Общая прибыль {total_profit}\n")
    average_profit["average_profit"] = round(total_profit / profitable_companies)
    result = [profit, average_profit]
    print(f"Словари с прибылью и с средней прибылью - {result}\n")

with open("Task_7_json.json", 'w') as json_file:
    json.dump(result, json_file)

    json_str = json.dumps(result)
    print(f"Содержимое json файла: \n {json_str}")



