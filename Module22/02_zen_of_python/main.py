reverse_list = []

with open('zen.txt', 'r') as file:
    for line in file:
        reverse_list.append(line.split('\n'))


for i_str in reverse_list[::-1]:
    print(' '.join(map(str, i_str)))

