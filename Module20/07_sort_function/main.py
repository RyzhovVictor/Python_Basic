nums = ([6, 3, -1, 8, 4, 10, -5])


def tuple_sort(any_tuple):
    for i in any_tuple:
        if not isinstance(i, int):
            return tuple(any_tuple)
    return tuple(sorted(any_tuple))


print(tuple_sort(nums))
