students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def accept_arg(dict_students):
    lst = []
    string = ''
    for i in dict_students:
        lst += (dict_students[i]['interests'])
        string += dict_students[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])

my_lst = accept_arg(students)[0]
l = accept_arg(students)[1]

print(f'Список пар "ID студента - возраст": {pairs}')
print(f'Полный список интересов всех студентов: {my_lst}')
print(f'Общая длина всех фамилий студентов: {l}')

