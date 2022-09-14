some_str = 'abcd'
some_tuple = (10, 20, 30, 40)


def my_zip(a, b):
    return ((a[i], b[i]) for i in range(min(len(a), len(b))))

unzip = my_zip(some_str, some_tuple)

print('Результат:')
print(unzip)
print(*unzip, sep='\n')



