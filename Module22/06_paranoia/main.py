def encryption(symbl, offset, list_alphabet):
    index = list_alphabet.index(symbl)
    if index + offset > len(list_alphabet) - 1:
        index = (index + offset) % len(list_alphabet)
    else:
        index += offset
    return index


alfavit_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
result = ''
line_count = 0

with open('text.txt', 'r', encoding='UTF-8') as file:
    for row in file:
        line_count += 1
        for smb in row:
            if smb in alfavit_EN:
                result += alfavit_EN[encryption(smb, line_count, alfavit_EN)]
            else:
                result += smb

with open('cipher_text.txt', 'w', encoding='UTF-8') as file:
    file.write(result)
