any_elem = 2
slicer = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)


def add_tuple(any_tuple, elem):
    if elem in any_tuple:
        if any_tuple.count(elem) > 1:
            first_index = any_tuple.index(elem)
            second_index = any_tuple.index(elem, first_index + 1) + 1
            return any_tuple[first_index:second_index]
        else:
            return any_tuple[any_tuple.index(elem):]
    else:
        return ()


print(add_tuple(slicer, any_elem))
