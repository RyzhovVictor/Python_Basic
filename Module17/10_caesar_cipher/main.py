alphabet_ru = ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)])
string = ''


def encryption(symbl, offset, list_alphabet):
    index = list_alphabet.index(symbl)
    print(index)
    if index + offset > len(list_alphabet) - 1:
        index = index + offset - len(list_alphabet)
    else:
        index += offset
    return index


text = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

for symbol in text:
    if symbol in alphabet_ru:
        string += alphabet_ru[encryption(symbol, shift, alphabet_ru)]
    else:
        string += symbol

print(string)
