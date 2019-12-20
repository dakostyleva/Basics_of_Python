"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

with open("Input_File.txt") as inputfile:
    content = inputfile.readlines()
    print(content)

new_list_1 = [el.replace('One', 'Один') for el in content]
new_list_2 = [el.replace('Two', 'Два') for el in new_list_1]
new_list_3 = [el.replace('Three', 'Три') for el in new_list_2]
new_list_4 = [el.replace('Four', 'Четыре') for el in new_list_3]
print(new_list_4)

with open("Output_file", 'w') as outputfile:
    outputfile.writelines(new_list_4)
