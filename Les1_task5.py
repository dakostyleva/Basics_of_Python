rev = int(input ("Введите сумму выручки компании: "))
costs = int(input ("Введите сумму расходов компании: "))

diff = rev - costs
if diff>0:
    print (f"Отлично! Вы получили прибыль в размере {diff} с рентабельностью %.2f процентов!" %(diff / rev *100))
    hc = int(input ("Введите количество сотрудников в компании: "))
    print("Прибыль на сотрудника составляет %.2f" %(diff/hc))
elif diff == 0:
    print ("Вы пока ничего не заработали")
else:
    print (f"К сожеланию, вы получили убыток в размере {diff} :(")

