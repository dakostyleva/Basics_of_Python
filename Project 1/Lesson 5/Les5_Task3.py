"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников."""

with open("My_file_3.txt", 'r') as my_file:
    h = my_file.read()

my_list = h.split("\n")
new_list = [el.split(' ') for el in my_list]

sum = 0
for el in new_list:
    sum = sum + int(el[1])
    if int(el[1]) < 20000:
        print(f"У следующего сотрудника оклад менее 20000: {el[0]}")

print(f"Средний доход сотрудников составляет {int(sum / len(new_list))} руб.")
