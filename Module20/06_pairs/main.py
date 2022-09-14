import random

random_list = [random.randint(1, 100) for num in range(10)]
print(list(zip(random_list[:5], random_list[5:])))
