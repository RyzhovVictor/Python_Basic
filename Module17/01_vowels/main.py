user_text = list(input('Введите текст: '))

vowels = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']

user_vowels = [letter for letter in user_text if letter in vowels]

print('\nСписок гласных букв: ', user_vowels)
print('Длина списка: ', len(user_vowels))
