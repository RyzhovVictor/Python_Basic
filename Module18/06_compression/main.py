user_input = input('Введите строку: ')
count = 1
length = len(user_input)

for i in range(len(user_input)):
    if i == (length - 1):
        print(f'{user_input[i]}{count}', end='')
    else:
        if user_input[i] == user_input[i + 1]:
            count += 1
        else:
            print(f'{user_input[i]}{count}', end='')
            count = 1
