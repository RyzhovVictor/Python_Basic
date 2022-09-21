user_count = int(input('Введите количество дисков: '))


def move(n, x, y):
    if n == 1:
        print(f'Переложить диск 1 со стержня номер {x} на стержень номер {y}')
    else:
        move(n - 1, x, 6 - x - y)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n - 1, 6 - x - y, y)


move(user_count, 1, 3)
