user_input = input('Введите строку: ')


def is_palindrome(text):
    char_dict = dict()
    for i_sym in text:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            count += 1
    return count <= 1


if is_palindrome(user_input):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
