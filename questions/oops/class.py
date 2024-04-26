# Python Object-Oriented Programming
'''
class -> A class is a blueprint for creating instances.
it is an real-worl entity or object.

instance-> and each unique employee that we created using the employee 
class will be the instance of the class.

method -> A function that is associated with the class.

instance variables -> contains data that is unique to each instance(like name, email, pay)

class variables -> are variables that are shared among all instances of a class.
                class variables should be same for each instance.

Note: 
1. Regular methods or instance methods: when we create methods within the class they recieve
the instance as the first argument, by convention we call this
instance as a self.

2. class methods: recieve class as the first argument insted of instance, 
by convention we call this as a cls.

class methods are used as a alternative constructors.
that you can use these class methods in order to provide multiple ways 
of creating our objects.

3. static methods: method should be a static method is if we dont access 
the instance or the class anywhere within the function.
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


emp_1 = Employee('alpha','leporis',50000) # emp_1 and emp_2 are instances of this class
emp_2 = Employee('test','user',60000 )

'''
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
'''

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

