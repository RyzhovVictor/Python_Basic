# list_1 = [[1, 2, [3]], [1], 3]
# list_2 = (1, 2, 3, 4, 5)


def my_sum(args):
    summ = 0
    for arg in args:
        if isinstance(arg, (list, tuple)):
            summ += my_sum(arg)
        elif isinstance(arg, int):
            summ += arg
        else:
            raise TypeError(f'Ошибка типа данных: {type(arg)}')
    return summ


# print(my_sum(list_2))
