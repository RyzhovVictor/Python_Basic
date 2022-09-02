user_input = input('Введите IP: ').split('.')

# for i in user_input:
#     if len(user_input) < 4:
#         print('Адрес — это четыре числа, разделённые точками.')
#     elif not i.isdigit():
#         print(f'{i} - Это не целое число.')
#     elif int(i) > 255:
#         print(f'{i} превышает 255.')
#     else:
#         print('IP-адрес корректен.')

if len(user_input) < 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    num = 0
    out = 0
    for i in user_input:
        if i.isdigit():
            num += 1
            if int(i) > 255:
                out += 1
                print(f'{i} превышает 255.')
        else:
            print(f'{i} - Это не целое число.')
    if out == 0 and num == 4:
        print('IP-адрес корректен.')


