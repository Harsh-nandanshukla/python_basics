courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0:2])# ['History', 'Math']
print(courses[0:-1])#['History', 'Math', 'Physics']
print(courses[2:])#['Physics', 'CompSci']
courses.append('LinAl')#['History', 'Math', 'Physics', 'CompSci', 'LinAl']
print(courses)
courses.insert(0,'Calculus')#['Calculus', 'History', 'Math', 'Physics', 'CompSci', 'LinAl']
print(courses)

course_2=["Art",'Phuilosphy']
# courses.insert(0,course_2)#[['Art', 'Phuilosphy'], 'Calculus', 'History', 'Math', 'Physics', 'CompSci', 'LinAl']
# print(courses)
courses.extend(course_2) #['Calculus', 'History', 'Math', 'Physics', 'CompSci', 'LinAl', 'Art', 'Phuilosphy']
print(courses)
courses.remove('Art')# removes art
print(courses)
popped=courses.pop()# removes and gves last element 
print(popped)
courses.reverse()
print(courses)
courses.sort()
print(courses)
nums=[1,45,67,3,7]
nums.sort()
print(nums)
courses.sort(reverse=True)
print(courses)
nums.sort(reverse=True)
print(nums)
sorted_spurse=sorted(courses)# it won't alter the original list and gives us new list by sorting
print(courses)#['Physics', 'Math', 'LinAl', 'History', 'CompSci', 'Calculus']  
print(sorted_spurse)# ['Calculus', 'CompSci', 'History', 'LinAl', 'Math', 'Physics']
print(min(nums))
print(max(nums))
print(courses.index('Math'))
print('Art' in courses)
for idx, course in enumerate(courses):
    print(idx,course) # will print idx and courses 


#coversion from list to string 
course_str= ' , '.join(courses)
print(course_str)#Physics , Math , LinAl , History , CompSci , Calculus
# course_str=''
# for i in range(len(courses)):
#     course_str+=courses[i] 
#     if i!=len(courses)-1  :
#         course_str+=','
   
# print(course_str)     

new_list=course_str.split(',')
print(new_list)#['Physics ', ' Math ', ' LinAl ', ' History ', ' CompSci ', ' Calculus']


# TUPLES -> Immutable 

tuple_1=('History', 'Math', 'Physics', 'CompSci')
print(tuple_1)
# tuple_1[0]='Art'#TypeError: 'tuple' object does not support item assignment

#SETS
cs_courses={'History', 'Math', 'Physics', 'CompSci','Math'}
art_courses={'History','Phlosphy','Political Sci'}
print(cs_courses)#{'History', 'Physics', 'CompSci', 'Math'} # ignioreds duplicates
print(cs_courses.intersection(art_courses))# comman elemntgs
print(cs_courses.difference(art_courses))# in cs but not i art
print(cs_courses.union(art_courses))

empty_list=[]# works
empty_list=list()# works
empty_tuple=()# works
empty_tuple=tuple()# works
# NOT FOR SET
empty_set={}# won't works wil create dictionary empty one
empty_list=set()# works