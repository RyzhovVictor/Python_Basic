def calc(lines):
    operand_1, operation, operand_2 = lines.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '*':
        value = operand_1 * operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        raise ValueError('Unknown operation {operation}')
    return value


total = 0
with open('calc.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            msg = f'Обнаружена ошибка в строке: {line} хотите исправить? '
            answer = input(msg.lower())
            if answer == 'да' or answer == 'yes':
                new_line = input('Введите исправленную строку: ')
                total += calc(new_line)

print(f'Total {total}')
