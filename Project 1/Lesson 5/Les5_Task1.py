"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

user_input = input("Введите слова: ")
lines = user_input.split(" ")

with open("My_first_file.txt", "w") as my_file:
    for el in lines:
        my_file.write(el + "\n")
