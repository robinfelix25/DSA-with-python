

# c++ 
# int a = 1
# char c = 'a'

# Python
a = 1
c = 'surya'

# print(c)

#addition
a = 1
b = 2
c = a + b
# print(c)

# 1. What are the data structures available in PYthon?
# - integer
# - String
# - float
# - list
# - tuple
# - dictionary

# LIST
list1 = [1,2,3,4,5,6,7,8,9,10]

# student_list = ['name','surya', '']

#Tuple
tuple1 = (1,2,3,4,5,6,7,8,9,10)

# print("before altering", list1[0])
# list1[0] = 11
# print("after altering", list1[0])


# print("before altering", tuple1[0])
# tuple1[0] = 11
# print("after altering", tuple1[0])


# print(type(list1))


# a = 1
# b = 11

# if a == b:
#     print("True")
# else:
#     print("False")

student = [
    {'name' : 'Surya',
    'age' : 16,
    'class' : 'A'},
    {'name' : 'Robin',
     'age' : '31',
     'class' : 'B'}
]

for i, s in enumerate(student):
    print(student[i]['age'])