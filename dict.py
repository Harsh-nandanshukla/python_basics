student={'name':'Harsh','location':'jodhpur','age':'25'}
print(student['name'])#Harsh
# print(student['dob'])# will give key error 
print(student.get('name'))# will give harsh
print(student.get('dob'))# will give none
student.update({'name':'shukla','location':'alld'})
print(student)#{'name': 'shukla', 'location': 'alld', 'age': '25'}

age=student.pop('age')
print(student)#{'name': 'shukla', 'location': 'alld'}
print(age)# 25
print(len(student))
print(student.keys())
print(student.values())
for key,value in student.items():
    print(key,value)

student.update({'dob':'25 aug, 2008'})
print(student)#{'name': 'shukla', 'location': 'alld', 'dob': '25 aug, 2008'}  
