
while True:
    user_password = input('Придумайте пароль: ')
    num = [int(i) for i in user_password if i.isdigit()]
    if len(user_password) < 8:
        print('Пароль ненадежный. Попробуйте еще раз.')
    elif user_password.islower():
        print('Пароль ненадежный. Попробуйте еще раз.')
    elif len(num) < 3:
        print('Пароль ненадежный. Попробуйте еще раз.')
    else:
        print('Это надежный пароль!')
        break
