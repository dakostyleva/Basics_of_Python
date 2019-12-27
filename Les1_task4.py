a = int(input("Введите целое положительное число: "))

max = 0

while int(a)>0:
    a = a*0.1
    c = int(a)
    d=int((a-c)*10)
    if d>max:
        max = d

print(f"Самая большая цифра в загаданном числе: {max}.")


