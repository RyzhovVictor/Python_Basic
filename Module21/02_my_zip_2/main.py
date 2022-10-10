# a = [1, 2, 3, 5]
# b = '456'
# c = (7, 8, 9)

# a = [1, 2, 3, 4, 5]
# b = {1: "s", 2: "q", 3: 4}
# c = (1, 2, 3, 4, 5)

# a = [{"x": 4}, "b", "z", "d"]
# b = (10, {20, }, [30], "z")


def my_zip(*args):
    min_args = min(map(len, args))
    args = list(map(list, args))
    return [tuple(i_elem[k_elem] for i_elem in args) for k_elem in range(min_args)]


unzip = my_zip(a, b, c)

print('Результат:')
print(*unzip)
