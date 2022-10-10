user_input = int(input('Введите num: '))


def func_seq(end, start=1):
    if start <= end:
        print(start)
        func_seq(end, start + 1)


func_seq(user_input)
