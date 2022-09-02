user_input = input('Введите строку: ').split()
find_max_len = max(user_input, key=len)

print('Самое длинное слово: ', find_max_len)
print('Длина этого слова: ', len(find_max_len))
