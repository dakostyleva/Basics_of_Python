'''6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.'''

from itertools import count, cycle

num = int(input('Введите целое число от 0 до 99: '))
for el in count(num):
    if el > 100:
        break
    else:
        print(el)

my_list = ['New week:', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
с = 1
for el in cycle(my_list):
    if с > 80:
        break
    print(el)
    с += 1
