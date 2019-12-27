my_list = [20, 17, 14, 14, 10, 7, 7, 5, 4]
while len(my_list)<20:
    user_num = int(input("Введите число: "))
    for el in my_list:
        if user_num == el:
            my_list.insert(my_list.index(el)+1,user_num)
            break
        elif user_num > el:
            my_list.insert(my_list.index(el), user_num)
            break
    if user_num in my_list:
        print(my_list)
    else:
        my_list.append(user_num)
        print(my_list)

print ("Вы достигли максимального размера рейтинга чисел")