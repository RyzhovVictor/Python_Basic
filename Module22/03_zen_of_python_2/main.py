import os


def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result


file_path = find_file(os.path.abspath(os.path.join('..', '..')), 'zen.txt')

if file_path:
    print('Абсолютный путь: ', file_path)
else:
    print('Файл не найден.')

num_lines = 0
num_words = 0
num_chars = 0

with open(file_path, 'r') as file:
    for line in file:
        words = line.lower().split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

text = open(file_path).read().lower()
letters = [c for c in text if c in "abcdefghijklmnopqrstuvwxyz"]
rare_letter = min(letters, key=letters.count, default='Нет букв')

print('Количество букв в файле: ', num_chars)
print('Количество слов в файле:', num_words)
print('Количество строк в файле:', num_lines)
print('Наиболее редкая буква: ', rare_letter)
