class Parent:
    lst_childes = []

    def __init__(self, name, age, lst_child):
        self.name = name
        self.age = age
        for child in lst_child:
            if age - child.age > 16:
                self.lst_childes.append(child)

    def __str__(self):
        return self.name + ' ' + str(self.age) + '\n' + '\n'.join(str(child) for child in self.lst_childes)

    def soothe_the_child(self, children):
        for child in self.lst_childes:
            if child is children:
                child.state_of_calm = True

    def feed_baby(self, children):
        for child in self.lst_childes:
            if child in children:
                child.state_hanger = True


class Child:
    def __init__(self, name, age, state_of_calm, state_hanger):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.state_hanger = state_hanger

    def __str__(self):
        calm = ('Спокоен' if self.state_of_calm else 'Раздражен')
        hanger = ('Сыт' if self.state_hanger else 'Голоден')
        return f'{self.name} {self.age} лет {calm} {hanger}'


pytya = Child('Петя', 3, True, True)
nadya = Child('Надя', 12, True, False)
kostya = Child('Костя', 23, False, True)
mama = Parent('Вика', 43, [pytya, nadya, kostya])
print(mama)

