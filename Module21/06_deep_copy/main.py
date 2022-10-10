from copy import deepcopy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def make_copy(struct, key, new_name):
    if key in struct:
        struct[key] = new_name
        return struct
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = make_copy(sub_struct, key, new_name)
            if result:
                return struct


def get_template():
    new_site = []
    number_sites = int(input('Сколько сайтов: '))
    for num in range(number_sites):
        new_name = input('Введите название продукта для нового сайта: ')
        key = {'title': f'Куплю/продам {new_name} недорого', 'h2': f'У нас самая низкая цена на {new_name}'}
        copy_site = deepcopy(site)
        for i in key:
            make_copy(copy_site, i, key[i])
        new_site.append({new_name: copy_site})

    for elem in new_site:
        for key, value in elem.items():
            print(f'Сайт для {key}: ')
            print(value)


get_template()


