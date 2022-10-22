import datetime

with open('people.txt', 'r', encoding='utf-8') as people_file:
    name_line = people_file.read().split('\n')
    res = ''.join(name_line)
    try:
        for number, name in enumerate(name_line):
            if len(name) < 3:
                raise ValueError(f'Менее трёх символов в строке №{number + 1}')
    except ValueError:
        print(f'Менее трёх символов в строке №{number + 1}')
        with open('errors.txt', 'a', encoding='utf-8') as rec:
            print(f'{datetime.datetime.now()} менее трёх символов в строке {number + 1}', file=rec)
    finally:
        print(f'Общее количество символов: {len(res)}')