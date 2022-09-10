total_quan_str_protocols = int(input('Сколько записей вносится в протокол? '))
protocols = {}


def protocol_input_data():
    print('Записи (результат и имя):')
    for i_rec in range(1, total_quan_str_protocols + 1):
        records = input(f'{i_rec}-я запись: ').split()
        if int(records[0]) / float(records[0]) == 1.0 and int(records[0]) > 0:
            protocols.setdefault(records[0], []).append(records[1])
        else:
            print('Результат участника должен быть целым и неотрициательным числом')
            break


def competitions_result():
    for i_point, i_name in sorted(protocols.items()):
        for i_sep in i_name:
            print(i_sep, i_point)
# TODO функция, которая выше.
# Не могу дальше разобраться, как правильно отсортировать и правильно вывести.
# Может я не так начал все делать.


protocol_input_data()
competitions_result()
