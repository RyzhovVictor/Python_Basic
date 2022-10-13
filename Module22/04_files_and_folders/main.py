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


file_path = find_file(os.path.abspath(os.path.join('..', '..')), 'Module14')

if file_path:
    print('Абсолютный путь: ', file_path)
else:
    print('Файл не найден.')

count_dirs = 0
count_files = 0
size = 0

for root, directories, files in os.walk(file_path):
    for directory in directories:
        count_dirs += 1
    for file in files:
        count_files += 1
        fp = os.path.join(root, file)
        size += os.path.getsize(fp) / 1024

print('Размер каталога (в КБ): ', size)
print('Количество подкаталогов: ', count_dirs)
print('Количество файлов:', count_files)
