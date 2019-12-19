class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("--->", emp.fullname())


emp_1 = Developer("Frank", "Tesla", 50000, "Python")
emp_2 = Developer("Jack", "Rank", 70000, "Javascript")
man_1 = Manager("Jack", "Rank", 70000, [emp_1, emp_2])

print(emp_1.prog_lang)
print(emp_2.fullname())

print(man_1.print_employees())

print(isinstance(man_1, Employee))  # True
print(isinstance(man_1, Manager))  # True
print(isinstance(man_1, Developer))  # False
