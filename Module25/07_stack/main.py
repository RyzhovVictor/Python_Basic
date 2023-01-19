class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return '; '.join(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, elem):
        self.stack.append(elem)


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{str(i_priority)}: {self.task[i_priority]}.\n')
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

    def delete_task(self, task, priority):
        if priority not in self.task.keys() and task not in self.task.keys():
            print("Задача с таким приоритетом нет!")
        else:
            self.task[priority].pop()


manager = TaskManager()
manager.new_task('Украсить елку', 4)
manager.new_task('Сделать уборку', 4)
manager.new_task('Помыть посуду', 4)
manager.new_task('Отдохнуть', 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.new_task("Лечь", 3)
print(manager)
manager.delete_task("поесть", 2)
manager.delete_task('Сделать уборку', 4)
manager.delete_task('Украсить елку', 4)
print(manager)
