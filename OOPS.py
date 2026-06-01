
"""class rectangle:

    def __init__(self):
        self.length = 10
        self.breadth = 6

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


r = rectangle()
print(r.area())
print(r.perimeter())
"""

# passing our own parameter in arguments and also we can give default arguments
'''
class rectangle:

    def __init__(self, l=1, b=2):  #Initilization step 
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


r = rectangle(18, 19)
print(r.area())
print(r.perimeter())
'''
'''
class rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    @staticmethod
    def calc_area(length, breadth):
        return length * breadth

print(rectangle.calc_area(10 , 5))
'''

'''
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return(x, y)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


v1 = vector(2, 3)
v2 = vector(2, 5)
v3 = v1 + v2
print("vector sum :", v3)
'''
'''
from threading import *
from time import *

def display():
    for i in range(65, 91):
        print(chr(i))
        sleep(1)
t = Thread(target = display, name = 'spliting and combining')
t.start()
for i in range(65, 91):
    print(i)
    sleep(1)
t.join()
'''

'''
n = 6
for i in range(1,n + 1):
    for j in range(i):
        print('*', end=' ')
    print('')
'''
'''
#merge dictionary
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
merged = {**dict1, **dict2}

print(merged)
'''
'''
#create safely a nested directory
import os

nested_direct = "parent/child/grandchild"
os.makedirs(nested_direct, exist_ok=True)
print(f"Directory '{nested_direct}' created successfully.")
'''
'''
#acces index of a list using for loop
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Value: {fruit}")
    '''
'''
#flatten nested loop
matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]]

for row in matrix:
    for num in row:
        print(num, end=' ')
'''
'''
#slice list
colors = ["red", "green", "blue", "yellow", "purple"]
sliced_colors = colors[1:3]
print(sliced_colors)
'''
'''
#iterate over dictonary by using for loop
student = {"name": "John",
            "grade": "A",
            "age": 16}
for key, value in student.items():
    print(f"{key}: {value}")
'''
'''
#sort a dict by values
scores = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 70,
    "David": 90
}
sorted_by_value = dict(sorted(scores.items(), key=lambda item: item[1]))
print(sorted_by_value)
'''
'''
#check if list is empty
my_list = []
if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")
 
    '''
'''
#multiple excemption in one line
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Oops! Error occurred: {e}")
else:
    print(f"Result is {result}")
    '''
'''
#copy file
import shutil

source = 'path/to/source_file.txt'
destination = 'path/to/destination_file.txt'
shutil.copy(source, destination)
print("File copied successfully.")
'''
'''
#concate two list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)
'''
'''
#check if a key is already in dict
my_dict = {"name": "Alice", "age": 25}

if "age" in my_dict:
    print("Key 'age' is present in the dictionary")
else:
    print("Key 'age' is not present")
'''
"""n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print('.', end=' ')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()"""

"""n = 6
for i in range(n):
    for j in range(n):
        print('.', end= ' ')
    print()"""
'''n = 5
for i in range(n + 1):
    for j in range(n - i):
        print(' ', end= ' ')
    for k in range(i + 1):
        print('*', end='   ')
    print()
'''

"""n = 6
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('.', end =' ')
        else:
            print(' ', end=' ')
    print()"""
"""
n = 5
for i in range(n + 1):
    for j in range(n - i):
        print('', end = ' ')
    for k in range(i + 1):
        print('*', end=' ')
    print()
    
"""

"""
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j== n-1:
            print('*',  end=' ')
        else:
            print (' ', end = ' ')
    print()
"""