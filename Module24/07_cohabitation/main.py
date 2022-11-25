import random
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'{self.name} нет еды', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 50
        self.fullness -= 10

    def play(self):
        cprint(f'{self.name} Играл на компьютере целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин за едой', color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} деньги кончились!', color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} Въехал в дом', color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='red')
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}'


citizens = [
    Man(name='Вася'),
    Man(name='Костя'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print(f'================ день {day} ==================')
    for citizen in citizens:
        citizen.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)
