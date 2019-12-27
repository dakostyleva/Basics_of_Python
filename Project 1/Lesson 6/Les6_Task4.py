'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.'''

from random import randint


class Car:

    def __init__(self):
        self.speed = randint(0, 200)
        col = ['red', 'blue', 'yellow', 'grey', 'black', 'silver', 'purple', 'white', 'green']
        self.color = col[randint(0, 8)]
        self.name = 'Toyota'
        self.is_police = bool(randint(0, 1))

    def go(self):
        return ("The car moved off")

    def stop(self):
        return ("The car stopped")

    def turn(self):
        dir = ['left', 'right']
        value = randint(0, 1)
        direction = dir[value]
        return ("The car turned " + direction)

    def show_speed(self):
        return (self.speed)


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return ("You exceeded speed limitation!")
        else:
            return ("You speed is ok")


class SportCar(Car):

    def issportcar(self):
        if self.speed > 100:
            return ("This is a sport car")
        else:
            return ("This is not a sport car")


class WorkCar(Car):

    def show_speed(self):
        print('This is a workcar')
        if int(self.speed) > 40:
            return ("You exceeded speed limitation!")
        else:
            return ("You speed is ok")


class PoliceCar(Car):

    def ispolice(self):
        if self.is_police == True:
            return ("This is a police car")
        else:
            return ("This is not a police car")


a = TownCar()
print(a.name + " " + a.color)
print(a.go())
print(a.turn())
print(a.show_speed())
print()

b = PoliceCar()
print(b.ispolice())
print(b.show_speed())
print()

c = SportCar()
print(c.issportcar())
print()

d = WorkCar()
print(d.show_speed())
