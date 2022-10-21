import random

finish_num = 777
finish_user_nums = 0
errors = [ArithmeticError('Вас постигла неудача !'), AssertionError('Вас постигла неудача !'),
          AttributeError('Вас постигла неудача !'), TypeError('Вас постигла неудача !'),
          ValueError('Вас постигла неудача !'), NameError('Вас постигла неудача !')]

dropping = open('out_file.txt', 'w')
dropping.close()
while True:
    user_nums = int(input('Введите число: '))
    finish_user_nums += user_nums
    if random.choices((0, 1), (1 - 1 / 13, 1 / 13))[0]:
        raise random.choice(errors)
    with open('out_file.txt', 'a', encoding='utf-8') as save_nums:
        save_nums.seek(0)
        save_nums.write(str(user_nums) + '\n')
        if finish_user_nums >= finish_num:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
            print('Сумма всех ваших чисел: ', finish_user_nums)
            break
