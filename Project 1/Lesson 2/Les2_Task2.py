my_list = list (input("Введите элементы списка: "))
print (my_list)
n=0
while n+1<len(my_list):
    my_list.insert(n,my_list[n+1])
    my_list.pop(n+2)
    n=n+2

print (my_list)