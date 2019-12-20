"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

new_list = []

import random

i = 0
while i < 16:
    number = random.randint(0, 101)
    new_list.append(number)
    i = i + 1
print(new_list)
sum = sum(new_list)
print(f"Сумма чисел равна {sum}")

with open("File_numbers", 'w') as num:
    for el in new_list:
        num.write(str(el) + " ")
    num.write('\nСумма чисел равна ' + str(sum))
