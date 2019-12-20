"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

with open("My_file_7.txt") as firms:
    content = firms.readlines()
    # print (content)

new_list = [el.split(' ') for el in content]
# print (new_list)

avrg_list = []
for el in new_list:
    result = int(el[2]) - int(el[3][:-1])
    if result > 0:
        avrg_list.append(result)
# print(avrg_list)
avrg = sum(avrg_list) / len(avrg_list)
print(f'Средняя прибыль составила {int(avrg)} рублей.')

profits_dict = {}

for el in new_list:
    result = int(el[2]) - int(el[3][:-1])
    profits_dict.update({el[0]: result})

# print (profits_dict)
avrg_dict = {"average_profit": int(avrg)}

final_list = []
final_list.append(profits_dict)
final_list.append(avrg_dict)

print(final_list)

import json

with open("my_file.json", "w") as jsonfile:
    json.dump(final_list, jsonfile)
