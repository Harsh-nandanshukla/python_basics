class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@iitj.ac.in'
    def fullname(self): # -> method : a function of a class
        return f'{self.first}, {self.last}'


   

emp_1=Employee('harsh','shukla',50000)# emp_1 is instance of the class
print(emp_1.fullname())#harsh shukla
print(Employee.fullname(emp_1))#harsh shukla