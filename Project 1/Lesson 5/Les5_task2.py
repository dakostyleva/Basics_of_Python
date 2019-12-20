"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open("My_file_2.txt", 'r') as my_file:
    content = my_file.readlines()
    print(content)

par = len(content)
print(f"В файле {par} строк(и)")

i = 0
while i < par:
    h = list(content[i])
    words = h.count(' ') + 1
    print(f"В строке {i + 1} - {words} слов(а)")
    i = i + 1
