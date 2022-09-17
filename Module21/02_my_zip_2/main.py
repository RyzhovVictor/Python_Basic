a = [{"x": 4}, "b", "z", "d"]

b = (10, {20, }, [30], "z")


def my_zip(*args):
    zip_on = [i_elem[0] for i_elem in args]
    print(zip_on)


my_zip(a, b)
