# a = [1, 2, 3]
# b = '456'
# c = (7, 8, 9)

# a = [1, 2, 3, 4, 5]
# b = {1: "s", 2: "q", 3: 4}
# c = (1, 2, 3, 4, 5)

a = [{"x": 4}, "b", "z", "d"]
b = (10, {20, }, [30], "z")


def my_zip(*args):
    # args = list(map(list, args))
    return ((i_elem[j_elem] for i_elem in args) for j_elem in range(len(args)))


unzip = my_zip(a, b)

print('Результат:')

for i in unzip:
    print(*i)

