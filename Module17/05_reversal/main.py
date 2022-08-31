user_input = input('Введите строку: ')

chars = [positions for positions, char in enumerate(user_input) if char == 'h']

start = chars[0]
end = chars[len(chars) - 1] - 1

print('Развернутая последовательность между первым и последним h: ', user_input[end:start:-1])