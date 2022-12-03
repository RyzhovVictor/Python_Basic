from dataclasses import dataclass, field


@dataclass(order=True)
class TaskData:
    sort_index: int = field(init=False, repr=False)

    name: str
    index: int

    def __post_init__(self):
        self.sort_index = self.index


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self, index: int = -1):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(index)

    def push(self, item):
        self.stack.append(item)


class TaskManager:
    stack = Stack()

    def __str__(self):
        result = ''
        old_index: int = 0
        self.stack.stack.sort()
        result += 'Результат:'
        for task in self.stack.stack:
            if old_index == task.index:
                result += f'; {task.name}'
            else:
                result += f'\n{task.index} {task.name}'
                old_index = task.index
        return result

    def new_task(self, name: str, index: int):
        self.stack.push(TaskData(name, index))

    def delete_task(self, name: str, index: int):
        index_element = 0
        for item in self.stack.stack:
            if item.name == name and item.index == index:
                self.stack.pop(index_element)
                break
            index_element += 1


manager = TaskManager()
manager.new_task('Сделать уборку', 4)
manager.new_task('Помыть посуду', 4)
manager.new_task('Отдохнуть', 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.delete_task("поесть", 2)
manager.delete_task('Сделать уборку', 4)
print(manager)

