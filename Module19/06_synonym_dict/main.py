count_user = int(input('Введите колличество пар слов: '))
syn_dict = dict()

for i in range(count_user):
    letter_pair = input(f'{i + 1} пара: ').lower().split()
    syn_dict[letter_pair[0]] = letter_pair[2]
    syn_dict[letter_pair[2]] = letter_pair[0]

while True:
    user_input_letter = input('Введите слово: ').lower()
    if user_input_letter not in syn_dict:
        print('Такого слова в словаре нет.')
    else:
        print(f'Синоним: {syn_dict[user_input_letter].capitalize()}')
        break
