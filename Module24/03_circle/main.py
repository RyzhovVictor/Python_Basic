import math as M


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area_circle(self):
        find_area_circle = M.pi * self.r * self.r
        return f'Площадь заданного круга: {find_area_circle}'

    def perimetr_circle(self):
        find_perimetr_circle = 2 * M.pi * self.r
        return f'Периметр заданного круга: {find_perimetr_circle}'

    def increase(self, K):
        K += self.r
        return f'Радиус круга увелился на {self.r}, и теперь он состовляет {K}'

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


print('Круг №1')
circle_1 = Circle(r=50)
circle_1.area_circle()
circle_1.perimetr_circle()
circle_1.increase(50)

print('\nКруг №2')
circle_2 = Circle(x=20, y=45, r=100)
circle_2.area_circle()
circle_2.perimetr_circle()
circle_2.increase(50)

print('\nПересение')
print(circle_1.is_intersect(circle_2))
