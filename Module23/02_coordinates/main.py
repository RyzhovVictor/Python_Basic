import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


line_number = 0
my_list = []
with open('coordinates.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_number += 1
        num_list = line.split()
        try:
            res1 = f(int(num_list[0]), int(num_list[1]))
            try:
                res2 = f2(int(num_list[0]), int(num_list[1]))
                number = random.randint(0, 100)
                my_list.append([number, res1, res2])
                with open('result.txt', 'w', encoding='utf-8') as save_file:
                    for line in save_file:
                        save_file.write(my_list)
            except Exception:
                print("Что-то пошло не так")
        except Exception:
            print(f'Строка {line_number} содержит не верные данные')

