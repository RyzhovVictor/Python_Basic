goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name_goods, code_goods in goods.items():
    inside_store = store[code_goods]
    count_total = 0
    price_total = 0
    for furniture in inside_store:
        count = furniture['quantity']
        count_total += count
        price = furniture['price']
        price_total += price
        all_cost = price_total * count_total
    print(name_goods, '-', count_total, 'шт.', 'стоимость', all_cost, 'руб.')

