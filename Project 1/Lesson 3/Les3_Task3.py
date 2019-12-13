'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''


def my_func(x, y, z):
    mylist = [x, y, z]
    mylist.remove(min(x, y, z))
    s = mylist[0] + mylist[1]
    return s


print(my_func(10, 15, 5))
