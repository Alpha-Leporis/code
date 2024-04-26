'''
# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6&ab_channel=CoreySchafer
# https://www.freecodecamp.org/news/python-property-decorator/

property decorator: It allows as to define a method that
we can access like an attribute

we're defining our email in our class like 
it's a method but we're able to access
it like an attribute and

# getter  --> @property

# setter  --> @Method_name.setter

# Deleter  --> @Method_name.deleter

'''

# getter

class Employee:

    # Constructor function
    def __init__(self, first, last, pay):  # special methods
        # we are going to set all the instance variables
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' + last + '@gmail.com'
    
    # getter  --> function overloading
    @property  # property decorator
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property  # property decorator
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    # setter  --> function overriding
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    # deleter
    @fullname.deleter
    def fullname(self):
        print('--> ' + 'Deleted Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Sue','Smith', 90000)

emp_1.first = 'Jim'

print('getter')
print('-->',emp_1.first)
print('-->',emp_1.email)
print('-->',emp_1.fullname)
print()


# setter
emp_1.fullname = 'Alpha Leporis'
print('setter')
print('-->',emp_1.first)
print('-->',emp_1.email)
print('-->',emp_1.fullname)
print()

# deleter
print('deleter')
del emp_1.fullname
