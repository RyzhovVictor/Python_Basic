import time
import random
import math


class Car:
    def __init__(self, x: int, y: int, fi: float):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist: int):
        self.x = self.x + dist * math.cos(self.fi)
        self.y = self.y + dist * math.sin(self.fi)

    def __str__(self):
        return f'Координаты: X={round(self.x, 2)} Y={round(self.y, 2)}'


class Bus(Car):
    PAY_COEFFICIENT = 0.01
    MAX_PASSENGERS = 60

    def __init__(self, x: int, y: int, direction: float):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def move(self, distance: int):
        self.money += Bus.PAY_COEFFICIENT * self.passengers * distance
        super().move(distance)

    def enter(self, passengers: int):
        if passengers + self.passengers > Bus.MAX_PASSENGERS:
            print('Достигнута максимальная вместимость автобуса.')
            left = Bus.MAX_PASSENGERS - (self.passengers + passengers)
            stayed = passengers - left
            print(f'Уехать смогли только {left} пассажиров, остались {stayed}.')
        else:
            self.passengers += passengers

    def exit(self, passengers: int):
        if passengers > self.passengers:
            print('Вышли все из автобуса')
            self.passengers = 0
        else:
            self.passengers -= passengers

    def __str__(self):
        lines = [
            super().__str__(),
            f'В автобусе {self.passengers} пассажиров.',
            f'У водителя {round(self.money, 2)} денег.',
        ]
        return '\n'.join(lines)


car = Car(0, 0, 120)
bus = Bus(1, 2, 40)


def time_line(sec):
    spent_time = random.randint(300, 900)
    sec += spent_time
    ty_res = time.gmtime(sec)
    res = time.strftime('%H:%M:%S', ty_res)
    print(f'\nВремя: {res}')
    return spent_time


second = 118800

for passed_time in range(1, 10):
    second += time_line(second)

    car.move(random.randint(0, 360))
    print(car)

    e2e = random.randint(1, 2)
    if e2e == 1:
        if bus.passengers > 0:
            bus.exit(random.randint(1, 3))
    else:
        bus.enter(random.randint(1, 3))
    bus.move(random.randint(0, 360))
    print(bus)
