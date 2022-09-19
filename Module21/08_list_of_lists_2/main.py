nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def slicing(args):
    if not args:
        return args
    if isinstance(args[0], list):
        return slicing(args[0]) + slicing(args[1:])
    return args[:1] + slicing(args[1:])


print(slicing(nice_list))
