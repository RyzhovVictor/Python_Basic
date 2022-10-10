summ = 0

with open('numbers.txt', 'r') as file:
    for line in file:
        for i_digit in line.split():
            summ += int(i_digit)


with open('answer.txt', 'w') as file:
    file.write(str(summ))
