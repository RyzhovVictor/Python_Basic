data_list = []
count_competitors = 0


def custom_key(scr):
    return scr[3]


with open('first_tour.txt', 'r', encoding='UTF-8') as file:
    result_K = file.readline()
    result_first_tour = file.read().split('\n')
    result_first_tour.sort(key=custom_key, reverse=True)
    print(result_first_tour)
    for line in result_first_tour:
        surname, name, scores = line.split(' ', 1)[0], line.split(' ', 2)[1], line.split(' ', 3)[2]
        if scores > result_K:
            count_competitors += 1
            data_list.append([count_competitors, name, surname, int(scores)])


with open('second_tour.txt', 'w', encoding='UTF-8') as file:
    file.write(str(count_competitors) + '\n')

with open('second_tour.txt', 'a', encoding='UTF-8') as file:
    for i in data_list:
        num, name, surname, scores = i
        file.write(f'{str(num) + ")"} {name[0] + "."} {surname} {str(scores)}\n')
