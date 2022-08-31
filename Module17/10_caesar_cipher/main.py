alphabet_ru = ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)])


def encryption(symbl, offset, list_alphabet):
    index = list_alphabet.index(symbl)
    if index + offset > len(list_alphabet) - 1:
        index = (index + offset) % len(list_alphabet)
    else:
        index += offset
    return index


text = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

result = [alphabet_ru[encryption(letter, shift, alphabet_ru)] if letter in alphabet_ru else letter
          for letter in text]

print(result)
