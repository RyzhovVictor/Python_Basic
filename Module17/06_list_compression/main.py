import random

user_input = int(input('Кол-во чисел в списке: '))

create_list = [int(random.randint(0, 2)) for i in range(user_input)]
print('Список до сжатия:', create_list)

create_new_list = [us_list for us_list in create_list if us_list > 0]
print('Список после сжатия:', create_new_list)
