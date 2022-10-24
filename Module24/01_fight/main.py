import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def fight(self, unit):
        unit.health -= 20
        if unit.health > 0:
            print(f'{self.name} атаковал {unit.name}. '
                  f'У {unit.name} осталось {unit.health} здоровья')
        else:
            print(f'{self.name} атаковал {unit.name}. {unit.name} убит')
            unit.health = 0
        return unit.health


warrior_1 = Warrior('Петя')
warrior_2 = Warrior('Вася')
warriors = [warrior_1, warrior_2]

while True:
    attack_index = random.randint(0, 1)
    target_index = (attack_index + 1) % 2
    target_health = warriors[attack_index].fight(warriors[target_index])
    if target_health == 0:
        print(f'{warriors[attack_index].name} Победил!')
        break
