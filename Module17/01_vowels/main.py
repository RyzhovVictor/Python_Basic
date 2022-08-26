user_text = list(input('Введите текст: '))
count = 0
vowels = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
user_vowels = []

for letter in user_text:
    for find_letter in vowels:
        if letter == find_letter:
            count += 1
            user_vowels.append(find_letter)

print('\nСписок гласных букв: ', user_vowels)
print('Длина списка: ', count)
