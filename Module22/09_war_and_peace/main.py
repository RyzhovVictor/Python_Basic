import zipfile


class StatLetter:
    def __init__(self, file_name):
        self.total_count = 0
        self.file_name = file_name
        self.stat = {}
        self.sorted_date = None

    def unzip(self):
        global filename
        z_file = zipfile.ZipFile(self.file_name, 'r')
        for filename in z_file.namelist():
            z_file.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='UTF-8') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for prev_char in line:
            if prev_char.isalpha():
                if prev_char in self.stat:
                    self.stat[prev_char] += 1
                else:
                    self.stat[prev_char] = 1

    def sort(self):
        self.sorted_date = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)

    def printed(self):
        print(f'+{"+":-^30}+')
        print(f'|{"Буква":^13} {"|":^1} {"Частота":^14}|')
        print(f'+{"+":-^30}+')
        for alphabet, count in self.sorted_date:
            print(f'|{alphabet:^13} {"|":^1} {count:^14}|')
            self.total_count += count
        print(f'+{"+":-^30}+')
        print(f'|{"ИТОГО":^13} {"|":^1} {self.total_count:^14}|')
        print(f'+{"+":-^30}+')

    def run(self):
        self.collect()
        self.sort()
        self.printed()


stat_letter = StatLetter(file_name='voyna-i-mir.zip')
stat_letter.run()