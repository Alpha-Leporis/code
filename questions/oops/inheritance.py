
'''
Every class and python is inherits from (builtins.object) this base object.

Inheritance: It allows us to inherite the attributes and methods
from the parent class.

python has two built-in functions:
isinstance and issubclass
'''
class Employee:
    # class variable
    num_of_emps = 0
    raise_amount = 1.04
    # Constructor function
    def __init__(self, first, last, pay):
        # we are going to set all the instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        # first, last and pay are attributes of the class.

        Employee.num_of_emps += 1

    #  regular method -> takes instance as a first argument  
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # special methods
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # here class method is used as a alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # returns emp object
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

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

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('alpha','leporis',50000,'python') # emp_1 and emp_2 are instances of this class
dev_2 = Developer('test','user',60000,'java')

mgr_1 = Manager('Sue','Smith', 90000,[dev_1])

'''
# a object is an instance of this class
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# a class is subclass of another class
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager,Developer))

'''
# special methods # https://docs.python.org/3/reference/datamodel.html#object.__add__
print(dev_1 + dev_2)
print(len(dev_1))

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# # mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

#print(help(dev_1))

# print(dev_1.email)
# print(dev_1.prog_lang)



