from random import randint, choice

NAMES = ['Алексей', 'Женя', 'Иван', 'Петр', 'Семен', 'Антон', 'Максим']
SURNAMES = ['Первый', 'Второй', 'Иванов', 'Четвертый', 'Петров']


# generate randon name, surname, age from constants arrays above
def generate_person():
    name = choice(NAMES)
    surname = choice(SURNAMES)
    age = randint(20, 50)
    return name, surname, age


class Person:
    def __init__(self, name, surname, age, job):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.job = job

    def __str__(self):
        return f'{"-":-^35}\nМеня зовут {self.__name} {self.__surname}. Мой возраст - {self.__age}'


class Employee(Person):
    def calc_salary(self):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f'\nМоя должность: {self.job}\nМоя зарплата: {self.calc_salary()}'


class Manager(Employee):
    def calc_salary(self):
        return 13000


class Agent(Employee):
    sales: int

    def calc_salary(self):
        return 5000 + .05 * self.sales


class Worker(Employee):
    hours: int

    def calc_salary(self):
        return 100 * self.hours


employees = list()

# managers
for _ in range(3):
    employees.append(Manager(*generate_person(), 'Manager'))

# agents
for _ in range(3):
    agent = Agent(*generate_person(), 'Agent')
    agent.sales = randint(2000, 10000)
    employees.append(agent)

# workers
for _ in range(3):
    worker = Worker(*generate_person(), 'Worker')
    worker.hours = randint(20, 50)
    employees.append(worker)

# logging out
for emp in employees:
    print(emp)
