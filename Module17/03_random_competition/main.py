import random

first_competitors = [round(random.uniform(1, 20), 2) for first_team in range(1, 21)]
second_competitors = [round(random.uniform(1, 20), 2) for second_team in range(1, 21)]
# Ниже - вариант по короче
# winners = [max(i) for i in zip(first_competitors, second_competitors)]
winners = [first_competitors[i] if first_competitors[i] > second_competitors[i] else second_competitors[i] for i in
           range(len(first_competitors))]

print('Первая команда: ', first_competitors)
print('Вторая команда: ', second_competitors)
print('Победители тура: ', winners)
