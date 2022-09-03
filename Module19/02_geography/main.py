user_count = int(input('Количество стран: '))
user_country_dict = dict()

for i in range(user_count):
    user_country = input(f'{i + 1} страна: ').split()
    user_country_dict = {user_country[0]: user_country[1:]}
    # print(user_country_dict)

print(user_country_dict)

