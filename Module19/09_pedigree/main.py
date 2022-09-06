mans_count = int(input('Введите количество человек: '))
save_pair = dict()
count_dict = dict()

for pair in range(1, mans_count):
    pair_input = input(f'{pair} пара: ').split()
    save_pair[pair_input[0]] = pair_input[1]
    count_dict[pair_input[0]] = 0
    count_dict[pair_input[1]] = 0


for i in save_pair:
    mans = i
    while mans in save_pair:
        mans = save_pair[mans]
        count_dict[i] += 1


print('\n' f'«Высота» каждого члена семьи: ')
for height in sorted(save_pair):
    print(height, count_dict[height])
