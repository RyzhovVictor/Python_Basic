user_count = int(input('Количество стран: '))
user_country_dict = {}

for i in range(user_count):
    user_country = input(f'{i + 1} страна: ').split()
    for city in user_country[1:]:
        user_country_dict[city] = user_country[0]

for i in range(3):
    city = input(f'{i + 1} город: ')
    country = user_country_dict.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')
