"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

with open("My_file_6.txt") as subjects:
    content = subjects.readlines()
new_list = [el.split(' ') for el in content]

my_dict = {}
for el in new_list:
    a = el[0]
    if (el[1] == '-'):
        b = 0
    else:
        b = el[1][:-3]
    if el[2] == '-':
        c = 0
    else:
        c = el[2][:-4]
    if el[3] == '-' or el[3] == '-\n':
        d = 0
    else:
        d = el[3][:-6]
    sum = int(b) + int(c) + int(d)
    my_dict.update({a: sum})

print(my_dict)

# my_dict = dict(key_1='val_1', key_2='val_2')
