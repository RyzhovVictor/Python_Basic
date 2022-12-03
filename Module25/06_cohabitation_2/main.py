from random import randint
from termcolor import cprint


class House:
    total_money = 0
    total_food = 0
    total_buy_coat = 0

    def __init__(self):
        self.count_money = 100
        self.count_food = 50
        self.count_mud = 0
        self.food_for_cat = 30

    def __str__(self):
        return 'В доме денег осталось: {}, кол-во еды осталось: {}, кол-во грязи осталось: {}'.format(self.count_money,
                                                                                                      self.count_food,
                                                                                                      self.count_mud)


class Man:
    def __init__(self, name):
        self.degree_satiety = 30
        self.degree_happy = 100
        self.house = home
        self.name = name

    def __str__(self):
        return 'Еды осталось: {}, уровень счастья: {}'.format(self.degree_satiety, self.degree_happy)

    def depression(self):
        if self.house.count_mud >= 90:
            self.degree_happy -= 5

    def food(self):
        self.degree_satiety -= 10

    def eat(self):
        if self.house.count_food >= 15:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.degree_satiety += 25
            self.house.total_food += 15
            self.house.count_food -= 15
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def petting_cat(self):
        self.degree_happy += 5
        cprint('{} погладил(а) кота'.format(self.name), color='yellow')

    def act(self):
        if (self.degree_satiety <= 0) or (self.degree_happy < 10):
            cprint('{} умер...'.format(self.name), color='red')
            return False
        self.depression()
        self.food()
        if self.degree_satiety <= 30:
            self.eat()
            return False
        return True


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def __str__(self):
        return 'Я {}, Степень сытости: {} Степень счастья: {}'.format(self.name, self.degree_satiety,
                                                                      self.degree_happy)

    def act(self):

        if not super().act():
            return
        dice = randint(1, 5)
        if self.house.count_money <= 200:
            self.work()
        elif self.degree_happy < 30:
            self.gaming()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.work()
        elif dice == 4:
            self.work()
        elif dice == 5:
            self.petting_cat()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.count_money += 150
        self.house.total_money += 150

    def gaming(self):
        cprint('{} Играл в Dota2'.format(self.name), color='green')
        self.degree_happy += 20


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def __str__(self):
        return 'Я {}, Степень сытости: {} Степень счастья: {}'.format(self.name, self.degree_satiety,
                                                                      self.degree_happy)

    def act(self):
        if not super().act():
            return
        dice = randint(1, 5)
        if self.house.count_food <= 30:
            self.shopping()
        elif self.degree_happy < 30:
            self.buy_fur_coat()
        elif self.degree_happy <= 15:
            self.petting_cat()
        elif self.house.count_mud > 100:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.buy_fur_coat()
        elif dice == 5:
            self.petting_cat()

    def shopping(self):
        if self.house.count_money >= 150:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.count_money -= 150
            self.house.count_food += 150
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        if self.house.count_money >= 400:
            cprint('{} сходила в магазин за шубой'.format(self.name), color='magenta')
            self.house.count_money -= 350
            self.house.total_buy_coat += 350
            self.degree_happy += 60
        else:
            cprint('Денег на шубу нет!', color='red')

    def clean_house(self):
        if self.house.count_mud >= 100:
            self.house.count_mud -= 100
            cprint('{} Убралась'.format(self.name))


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = home
        self.degree_satiety = 30

    def __str__(self):
        return 'Я {}, Степень сытости: {}'.format(self.name, self.degree_satiety)

    def act(self):
        if self.degree_satiety <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.degree_satiety <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.tear_wallpaper()

    def eat(self):
        if self.house.count_food > 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.degree_satiety += 10
            self.house.total_food += 10
            self.house.count_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.degree_satiety -= 10
        cprint('{} спал весь день'.format(self.name), color='magenta')

    def tear_wallpaper(self):
        self.degree_satiety -= 10
        self.house.count_mud += 5
        cprint('{} драл обои целый день'.format(self.name), color='magenta')


class Child:

    def __init__(self, name):
        self.name = name
        self.house = home
        self.degree_satiety = 30
        self.degree_happy = 100

    def __str__(self):
        return 'Я {}, Степень сытости: {} Степень счастья: {}'.format(self.name, self.degree_satiety,
                                                                      self.degree_happy)

    def act(self):
        if self.degree_satiety <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.degree_satiety <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        if self.house.count_food >= 15:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.degree_satiety += 20
            self.house.total_food += 10
            self.house.count_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.degree_satiety -= 10
        cprint('{} спал весь день'.format(self.name), color='magenta')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
murzik = Cat(name='Мурзик')
kolya = Child(name='Коля')

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murzik.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')
    home.count_mud += 5

count_coat = int(home.total_buy_coat / 350)

cprint('Всего заработанных денег: {}'.format(home.total_money), color='yellow')
cprint('Всего съедено еды: {}'.format(home.total_food), color='yellow')
cprint('Всего куплено шуб: {}'.format(count_coat), color='yellow')
