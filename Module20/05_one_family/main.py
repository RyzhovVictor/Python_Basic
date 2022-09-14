families = {
    'Пупков Ваня': 18,
    'Пупкова Лена': 14,
    'Пупков Сергей': 45,
    'Сидоров Костя': 27,
    'Сидорова Женя': 32,
    'Дубова Катя': 46,
    'Дубов Артем': 48,
    'Тучин Федя': 99,
    'Тучина Маша': 150
}

user_find = input('Введите фамилию: ')
for i_man, i_age in families.items():
    surname = i_man.split()[0]
    if surname[:-1] in user_find:
        print(i_man, i_age)


