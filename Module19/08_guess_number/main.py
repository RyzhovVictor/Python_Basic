input_number = int(input('Введите максимальное число: '))
all_nums = set(range(1, input_number + 1))

while True:
    des_numbers = input('Нужное число есть среди вот этих чисел: ')
    if des_numbers == 'Помогите!':
        break
    des_numbers = {int(x) for x in des_numbers.strip()}
    answer = input('Ответ Артема: ')
    if answer == 'Да':
        all_nums &= des_numbers
    else:
        all_nums -= des_numbers

print('Артем мог загадать следующие числа:', *all_nums)
