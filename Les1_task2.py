
user_answer = int(input("Введите количество секунд: "))

hours = user_answer // 3600
min = (user_answer % 3600) // 60
sec = user_answer % 60

if (int(hours*0.1)==0):
    if (int(min*0.1)==0):
        if (int(sec * 0.1) == 0):
            print(f"Время: 0{hours}:0{min}:0{sec}")
        else:
            print(f"Время: 0{hours}:0{min}:{sec}")
    else:
        if (int(sec * 0.1) == 0):
            print(f"Время: 0{hours}:{min}:0{sec}")
        else:
            print(f"Время: 0{hours}:{min}:{sec}")
else:
    if (int(min*0.1)==0):
        if (int(sec * 0.1) == 0):
            print(f"Время: {hours}:0{min}:0{sec}")
        else:
            print(f"Время: {hours}:0{min}:{sec}")
    else:
        if (int(sec * 0.1) == 0):
            print(f"Время: {hours}:{min}:0{sec}")
        else:
            print(f"Время: {hours}:{min}:{sec}")





