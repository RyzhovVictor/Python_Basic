user_input = int(input('Введите количество заказов: '))
orders_dict = dict()

for i_order in range(user_input):
    orders = input(f'{i_order + 1} заказ: ').split()
    if orders[0] not in orders_dict:
        orders_dict[orders[0]] = {orders[1]: orders[2]}
    else:
        orders_dict[orders[0]].update({orders[1]: orders[2]})

for name, order in sorted(orders_dict.items()):
    print(f'{name}: ')
    for pizza, count in sorted(order.items()):
        print('\t' f'{pizza}: {count}')


