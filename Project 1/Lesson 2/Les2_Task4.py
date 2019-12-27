sent = input ("Введите слова: ")

m = sent.split(" ")
print(m)
n = 1
for el in m:
    if (len(m[m.index(el)]))<=10:
        print(f"{n} {el}")
    else:
        print(f"{n} {el[:10]}")
    n= n+1