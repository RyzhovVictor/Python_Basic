class Students:
    def __init__(self, name, num_group, progress):
        self.name = name
        self.num_group = num_group
        self.progress = progress


student_1 = Students('Вася Пупкин', 1, [2, 3, 4, 2, 5])
student_2 = Students('Алеся Петрова', 2, [3, 4, 5, 5, 2])
student_3 = Students('Земфира Валадаева', 3, [1, 2, 3, 4, 5])
student_4 = Students('Коля Чернобровкин', 4, [5, 5, 4, 5, 3])
student_5 = Students('Демид Дорохов', 5, [3, 4, 5, 4, 3])
student_6 = Students('Доллар Евров', 6, [2, 3, 2, 2, 5])
student_7 = Students('Азамат Мусагалиев', 7, [2, 4, 5, 5, 2])
student_8 = Students('Поп Русский', 8, [1, 2, 4, 4, 5])
student_9 = Students('Пиво местное', 9, [5, 2, 4, 5, 3])
student_10 = Students('Таганрок Прибалтийский', 10, [5, 4, 5, 4, 3])

all_students = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9,
                student_10]

avg_list = []

for student in all_students:
    sum_lst = sum(student.progress)
    str_avg = sum_lst / len(student.progress)
    avg_list.append(str_avg)

print(sorted(avg_list))

