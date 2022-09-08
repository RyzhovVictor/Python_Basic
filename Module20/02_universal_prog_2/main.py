def return_elem(obj_iter):
    return [i_iter for i_iter, value in enumerate(obj_iter) if is_prime(i_iter)]


def is_prime(num):
    if num >= 2:
        result = True
        for i in range(2, num):
            if num % i == 0:
                result = False
                break
    else:
        result = False
    return result


def crypto(text):
    i_list = return_elem(text)
    elem = []
    for i_index in i_list:
        elem.append(text[i_index])
    return elem


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

