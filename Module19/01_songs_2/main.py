violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

user_count = int(input('Сколько песен выбрать? '))
summ = 0
for count in range(user_count):
    name_song = input(f'Название {count + 1} песни: ')
    if name_song in violator_songs.keys():
        summ += violator_songs[name_song]
    else:
        print('Такой песни нет')
        break

print(f'Общее время звучания песен: {summ} минуты')



