#Первое домашнее задание первого урока
a = 10
b = -10
print(a, b)

name = input('Enter your name  ')
age = int(input('Enter your age   '))
print('Hallo', name, ', your age is', age)

#Второе домашнее задание первого урока


def time():
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    d = f'{h:02d}:{m:02d}:{s:02d}'
    return d


seconds = int(input('Enter the time in seconds  '))
print(time())

#Третье домашнее задание первого урока
str_number = input('Enter your number:  ')
sum_number = (int(str_number) + int(str_number + str_number) + int(str_number + str_number + str_number))
print('Total sum ', sum_number)


#Четвёртое дз первого урока
n = int(input('Введите целое положительное число: '))
ls = []
while n > 9:
    ls.append(n % 10)
    n //= 10
ls.append(n)
i = max(ls)
print('Максимальная цифра в Вашем числе', i)

#Пятое дз первого урока
proceeds = int(input('Введите выручку компании: '))
costs = int(input('Введите затраты компании: '))
if proceeds > costs:
    print(f'Компания отработала с прибылью в размере {proceeds - costs}. Рентабельность прибыли составила'
          f' {proceeds / costs:.2f}')
    employees = int(input('Введите количество сотрудников компании: '))
    print(f'Прибыль на одного сотрудника составила {(proceeds - costs) / employees:.2f}')
elif proceeds == costs:
    print('Компания отработала в ноль')
else:
    print(f'Компания отработала с убытком в размере {proceeds - costs}')

#Шестое дз первого урока
a = int(input('Введите количество км, которые пробежал спортсмен за первый день:  '))
b = int(input('Введите общее количество км, которые необходимо пробежать спортсмену:  '))
days = 1

while a < b:
    a = a * 0.1 + a
    days += 1
    print(f'{days}-й день спортсмен пробежал {a:.2f} километров')
print('Спортсмен достигнет необходимого километража на', days, 'день')

