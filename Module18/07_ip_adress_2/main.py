user_input = input('Введите IP: ').split('.')
print(user_input)

for i in user_input:
    print(i)
    # if not user_input.isdigit():
    #     print('- Это не целое число.')
    # else:
    #     print('Все гуд')