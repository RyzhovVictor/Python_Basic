class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


print(' ***** Расчет налогов на имущество *****')
amount_money = int(input('Введите количество имеющихся денег: '))
print('Введите стоимость имущества: ')

flat = float(input('Квартира: '))
tax_apart = Apartment(flat)
print('Налог на квартиру {}'.format(tax_apart.tax()))

car = float(input('Машина: '))
tax_car = Car(car)
print('Налог на машину {}'.format(tax_car.tax()))

country_house = float(input('Дача: '))
tax_country_house = CountryHouse(country_house)
print('Налог на дачу {}'.format(tax_country_house.tax()))

sum_nalog = tax_apart.tax() + tax_car.tax() + tax_country_house.tax()

if sum_nalog < amount_money:
    print('Всего налога на сумму {}, а у вас только {}'.format(sum_nalog, amount_money))
    print('Денег не хватает')
else:
    print('Всего налога на сумму {}\nОтлично, денег хватает '.format(sum_nalog))
