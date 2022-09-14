total_quan_str_protocols = int(input('Сколько записей вносится в протокол? '))
protocols = {}  # type: ignore


def score_key(a):
    return a[1][0] * 100000000 - a[1][1]


def protocol_input_data():
    print('Записи (результат и имя):')
    for i_rec in range(1, total_quan_str_protocols + 1):
        point, name = input(f'{i_rec}-я запись: ').split()
        point = int(point)
        if name in protocols:
            if point > protocols[name][0]:
                protocols[name][0] = point
                protocols[name][1] = i_rec
        else:
            protocols[name] = [point, i_rec]


def competitions_result():
    protocol = list(protocols.items())
    protocol.sort(key=score_key, reverse=True)
    print('\n', 'Итоги соревнований: ')
    for winner_index in range(3):
        print(f'{winner_index + 1}-е место {protocol[winner_index][0]}', end=' ')
        print(f'({protocol[winner_index][1][0]})', sep='')


protocol_input_data()
competitions_result()
