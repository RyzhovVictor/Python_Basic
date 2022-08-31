file_name = input('Название файла: ')

spec_symbol = '@№$%^&\(*)'

if not file_name.endswith('.txt') and not file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
elif file_name[0] in spec_symbol:
    print('Ошибка: название начинается на один из спецаильных символов.')
else:
    print('Файл назван верно.')
