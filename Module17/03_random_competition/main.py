import random

second_competitors = []
first_competitors = []
winners = []

for competitors in range(1, 21):
    firsts = round(random.uniform(1, 20), 2)
    seconds = round(random.uniform(1, 20), 2)
    first_competitors.append(firsts)
    second_competitors.append(seconds)
    if firsts > seconds:
        winners.append(firsts)
    else:
        winners.append(seconds)


print('Первая команда: ', first_competitors)
print('Первая команда: ', second_competitors)
print('Победители тура: ', winners)


