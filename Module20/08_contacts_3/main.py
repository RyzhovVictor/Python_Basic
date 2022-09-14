phonebook = {}


def add_contact(phone_dict):
    name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if name in phone_dict.keys():
        print('Такой человек уже есть в контактах.')
        print(f'Текущий словарь контактов: {phone_dict}')
    else:
        phonenum = input('Введите номер телефона: ')
        phone_dict[name]: phonenum
        phonebook.update({(name[0], name[1]): phonenum})
        print(f'Текущий словарь контактов: {phone_dict}')


def find_contact(phone_dict):
    find_str = input('Введите фамилию для поиска: ').capitalize().split()
    for i_name, i_num in phone_dict.items():
        if i_name[1] in find_str:
            name = [str(i) for i in i_name]
            user_name, user_surname = name
            print(user_name, user_surname, i_num)
            break
    else:
        print('Такой контакт не найден')


while True:
    user_choice = int(input('Введите номер действия: \n'
                            '1. Добавить контакт\n'
                            '2. Найти человека\n'))
    if user_choice == 1:
        add_contact(phonebook)
    elif user_choice == 2:
        find_contact(phonebook)
    else:
        break
