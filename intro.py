# import my_module #->Imported my_module...
from my_module import find_index,test
# import sys
import random
# from my_module import * #-> this imports evrything that my_module has 
courses = ['History', 'Math', 'Physics', 'CompSci']
print(random.choice(courses))#-> random elemnt form courses
print(find_index(courses,'CompSci'))
#print(sys.path)# in sequnece first the directory containing the script -> python path env variable ->std lib-> pacakges