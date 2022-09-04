def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


user_input = input('Введите текст: ')
hist = histogram(user_input)


def swap_dict(d):
    new_hist = {}
    for key, values in d.items():
        new_hist[values] = new_hist.get(values, []) + [key]
    return new_hist


for i_sym in sorted(swap_dict(hist).keys()):
    print(f'{i_sym} : {swap_dict(hist)[i_sym]}')
