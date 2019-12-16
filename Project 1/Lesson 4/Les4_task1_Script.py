from sys import argv

script_name, hours, rate, bonus = argv


def salary(hours, rate, bonus):
    sal = int(hours) * int(rate) + int(bonus)
    print(sal)
