class Employee:
    nums_of_emps=0
    raise_amount=1.05 # class variable 
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@iitj.ac.in'
        Employee.nums_of_emps+=1
    def fullname(self): # -> method : a function of a class
        return f'{self.first}, {self.last}'
    
    def apply_raise(self):
       return self.pay*self.raise_amount # we cant just use elf.pay * raise_amount as it's class varible we are trying to access
        # we can alos do it Employee.raise_amount

print(Employee.nums_of_emps)#0    
emp_1=Employee('harsh','shukla',50000)   
print(Employee.nums_of_emps)#1
emp_2=Employee('hmanshu','jam',60000)   
print(Employee.nums_of_emps)#2
print(Employee.fullname(emp_1))
print(emp_1.pay)
print(Employee.apply_raise(emp_1))
print(emp_1.__dict__)#{'first': 'harsh', 'last': 'shukla', 'pay': 50000, 'email': 'harsh.shukla@iitj.ac.in'}
emp_1.raise_amount=1.06
print(emp_1.raise_amount)#1.06
print(emp_2.raise_amount)# 1.05 unchnaged
print(Employee.raise_amount)#1.05 un chnaged
print(emp_1.__dict__)#{'first': 'harsh', 'last': 'shukla', 'pay': 50000, 'email': 'harsh.shukla@iitj.ac.in', 'raise_amount': 1.06}
Employee.raise_amount=1.08
print(emp_1.raise_amount)#1.06
print(emp_2.raise_amount)# 1.08 
print(Employee.raise_amount)#1.08 

