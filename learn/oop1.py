class Employee():
    """A simple employee class """

    raiseAmount = 1.04
    employeeCount = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "".join((first,'.',last,'@company.com'))
        '''In the above line self.first and self.last instead of first and
            last also works fine'''
        Employee.employeeCount += 1
        '''Here using self.employeeCount is a dumb idea since for every
            instance number of employees always remains the same '''

    def fullname(self):
        return(" ".join((self.first,self.last)))

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)
        '''
            We have to use Employee.raiseAmount instead of self.raiseAmount
            using raiseAmount as instance variable makes possible to change
            the default value for specific instances and also allows overriding
            while in subclasses
        '''

    # The methods above are all static methods or regular methods
    # Class methods are defined along with a decorator

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raiseAmount = amount

    # Using class method as alternate constructor
    @classmethod
    def from_string(cls,employeeStr):
        first , last, pay = empStr1.split('-')
        return(cls(first,last,pay))


print(Employee.employeeCount,Employee.raiseAmount)
emp1 = Employee('sandeep','mandali',100)
emp2 = Employee('venu','masini',100)
print(emp1.__dict__, emp2.__dict__, sep='\n')

print(emp1.email,emp2.email,sep='\n')
print(emp1.fullname(),emp2.fullname(),sep='\n')
print(Employee.fullname(emp1), Employee.fullname(emp2))
print(Employee.employeeCount, emp1.employeeCount,emp2.employeeCount)
print(Employee.raiseAmount,emp1.raiseAmount,emp2.raiseAmount)
emp1.apply_raise()
print(emp1.pay)
emp2.raiseAmount = 1.05
''' This feels like we updated the class varible but instead we created an
instance variable with same name and it overides class variable since LEGB '''
print(emp1.__dict__,emp2.__dict__,sep='\n')
print(Employee.raiseAmount,emp1.raiseAmount,emp2.raiseAmount)
emp2.apply_raise()
print(emp2.pay)
# As the name suggests class mehtods are class as class attributes
Employee.set_raise_amount(1.06)
# This still doesn't overide the local raiseAmount for emp2
print(Employee.raiseAmount,emp1.raiseAmount,emp2.raiseAmount)
#we can call class methods with instances as well but it is not recommended
emp2.set_raise_amount(1.07)
# This still doesn't overide the local raiseAmount for emp2
print(Employee.raiseAmount,emp1.raiseAmount,emp2.raiseAmount)

empStr1 = 'John-Doe-70'
emp3 = Employee.from_string(empStr1)
print(emp3.email)
print(Employee.employeeCount)
