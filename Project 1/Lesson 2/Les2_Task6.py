amnt = int (input("Введите количество товаров: "))

tuple_list = []
val_1_list = set()
val_2_list = set()
val_3_list = set()
val_4_list = set()
n=1

while n<=amnt:
    words = input(f"Введите информацию по товару {n}: наименование, цену, количество и единицу измерения через запятую: ")
    m = words.split(",")
    val_1 = m[0]
    val_2 = int(m[1])
    val_3 = int(m[2])
    val_4 = m[3]
    my_dict = {'наименование:': val_1, 'цена': val_2, 'количество': val_3, 'ед': val_4}
    my_tuple = tuple([n, my_dict])
    tuple_list.append (my_tuple)
    val_1_list.add(val_1)
    val_2_list.add(val_2)
    val_3_list.add(val_3)
    val_4_list.add(val_4)
    n=n+1
print(tuple_list)

val_1 = list(val_1_list)
val_2 = list(val_2_list)
val_3 = list(val_3_list)
val_4 = list(val_4_list)

final_dict = {'наименование:': val_1, 'цена': val_2, 'количество': val_3, 'ед': val_4}
print (final_dict)
