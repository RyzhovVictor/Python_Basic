import os


def save_notes():
    user_text = input('Введите строку: ')
    user_save = input('Куда хотите сохронить документ?'
                      ' Введите последовательность папок '
                      '(через пробел): ').replace(' ', os.path.sep)

    user_name_file = input('Введите имя файла: ') + '.txt'

    get_path = os.path.join(os.getenv('SystemDrive'), os.path.sep, user_save, user_name_file)
    print(get_path)

    check_file = os.path.exists(get_path)

    if check_file:
        answer = input('Вы действительно хотите перезаписать файл? (Да/Нет)').lower()
        if answer == 'да' or answer == 'yes':
            with open(get_path, 'w', encoding='UTF-8') as file:
                file.write(user_text)
                file.close()
                print('Файл успешно перезаписан!')
        else:
            print('Файл не перезаписан!')
    else:
        with open(get_path, 'w', encoding='UTF-8') as file:
            file.write(user_text)
            file.close()
            print('Файл успешно сохранен!')


save_notes()
