import re

message = input('Сообщение: ')
result = (re.split('([^a-zA-Z0-9а-яА-Я])', message))

for i in result:
    print(i[::-1], end='')
