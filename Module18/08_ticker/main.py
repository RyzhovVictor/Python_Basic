first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

for i in range(len(first_str)):
    if first_str == second_str:
        print(f'Первая строка получается из второй со сдвигом {i}.')
        break
    second_str = second_str[-1] + second_str[:-1]
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
