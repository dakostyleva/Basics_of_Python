'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def numbers(x, y):
    div = x / y
    print(f"Результат деления: {round(div, 2)}")


while True:
    try:
        numbers(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
        break
    except ValueError:
        print("Ошибка! Необходимо ввести целые числа, попробуйте еще раз.")
    except ZeroDivisionError:
        print("Ошибка! На ноль делить нельзя, попробуйте еще раз.")
