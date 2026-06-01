"""n = int(input('Any number'))
m = int(input("any number"))
if n-m>0:
     print(n-m)
else:
     print(m-n)"""

'''odd or even'''
"""m = int(input("any number"))
if m%2 ==0:
    print("then the it is even ")
else:
    print("it is odd")"""

"""maths = int(input('Any number'))
pys = int(input('Any number'))
sci = int(input('Any number'))
if maths>=45 and pys>= 45 and sci>=45:
    print("passed")
else:
    print("failed")"""

"""
count = 0

while count<10:
    print("hello")
    count = count +1"""

'''reversed
a = int(input('Any number'))

while a>0:
    r= a%10
    a= a//10
    print(r)1'''

'''a = int(input('Any number'))
count = 0
while count<11:
    print(a,'x',count,'=', a*count )
    count = count + 1'''

'''a = int(input('Any number'))
sum = 0

while a>0:
    r= a%10
    a= a//10
    sum = sum + r

print(sum)'''

"""reverse
a = int(input('Any number'))
rev = 0

while a>0:
    r = a%10  -- reminder
    a = a//10 -- cofieciant 
    rev = (rev*10)+r

print(rev)"""

"""palindrome
a = int(input('Any number'))
m = a
rev = 0

while a>0:
    r = a%10
    a = a//10
    rev = (rev*10)+r

if m == rev:
    print("it is a palindrome")
else:
    print("It is not palindorme")"""
'''
#finging the sum of the value
num = int(input("enter any number"))
sum = 0 
count = 0
while count<num or count ==num:
    num = int(input("enter any number"))
    sum = sum+num
    count = count +1
print(sum)
'''
'''
num = int(input('enter the number'))
psum =0
nsum= 0
count = 0
while count<num:
    num = int(input('enter the number'))
    if num>0:
        psum = psum + num
    else:
        nsum = nsum + num
        count = count+1
print("its is a positive")
print("its is negative")'''

"""num = int(input('enter the number'))
max= int(input('enter the number'))
count = 0
while count<num:
    n = int(input('enter the number'))
    if n > max:
     max = n
    count = count +1

print(max)"""

'''guessing game
import random
n = random.randint(1,10)
guess = 0
while guess !=n or guess == n:
    guess = int(input("enter any number:"))
    if guess < n:
        print("it is lesser")
    elif guess > n:
        print("it is greater")
    else:
        print("it is correct")'''

"""
count = 0
while count < 10:
    num = int(input('enter the number'))
    if num%3==0:
        continue
    print(num)
    count+=1"""

'''
for i in range(0,6):
    print(i)'''

''' multipilcation
n = int(input("any number"))
for count in range (1,10):
   print(n,'x',count,'=', count*n)
'''

'''
n = int(input("Any number"))
fact = 1
for count in range(1,n+1):
    fact = fact*count
print(fact)'''


"""AP series
n= int(input("any number n:"))
m= int(input("any number m:"))
o= int(input("any number o:"))
for t in range (1,20,3):
     print(t)"""

'''fibnacci
n= int(input("any number n:"))
a = 0
b= 1
for i in range(n):
    c = a +b
    a = b
    b=c
    print(a)'''

'''factor numbers
n = int(input("any number n:"))
for i in range(1, n+1):
    if n%i == 0:
        print(i)'''

"""finding the prime numbers
n = int(input("any number n:"))
count = 0
for i in range(1, n+1):
    if n%i == 0:
        count += 1
if count ==2:
        print("it is a prime number")
else:
        print('it is not prime number')"""
'''
for i in range(0,5):
    for j in range(0,5):
        if i>=j:
         print('*' ,end = ' ')
    print('')
'''

'''finding the prime number
for n in range(1, 100+1):
    count = 0
    for i in range(1,100+1):
        if n%i == 0:
         count += 1
    if count == 2:
     print(n)'''

'''strings with indexing
s1 = 'hello world' 
for x in range (0, len(s1)):
    print(s1[x])
    
s1 = 'hello world'
for x in range (len(s1)-1,-1,-1):
    print(s1[x])'''

'''
str = "qwertyuiop"
n = sorted(str)
print(n)
str1='-'.join(n)
print(str1)

n = (input('any number'))
m = (input('any number'))
total_len = len(n) + len(m)
dot = '.' * (25 - total_len)
print(n+dot+m)

pass1 = input("any pass: ")
pass2 = input("any pass: ")

if pass1 == pass2:
    print('it is same')
else:
    if pass1.casefold() == pass2.casefold():
      print('it is matching but case sensitive')
    else:
        print("it is not matching")'''
'''
Card_number =input('enter the card number: ')
Enddigit = Card_number[15::]
first = '*' * 4 + ' '
n = first * 3 + Enddigit
print(n)'''
'''
emailid = input("any email: ")
atrate = emailid.find('@')
print(atrate)
print('userid: ', emailid[:atrate])
print('domianid: ',emailid[atrate+1:] )
'''

'''
a = input('any name')
rev = a[::-1]
if a==rev:
  print('it is a palimndrom')
else:
    print('it is not')'''
'''
mydate=input("enter any date format 03/15/2001: ")
proper = mydate.split('/')

print('day', proper[0])
print('month', proper[1])
print('year', proper[2])'''
'''
anagram = input("any name")
b = input("any name")
if len(anagram) != len(b):
    print("it is not")
else:
    for x in anagram:
        if x not in b:
           print("it is not anagram")
           break;
    else:
         print("it is anagram")'''
'''
str = 'AbcDefGhI'
lower =''
upper =''
for x in str:
   if x.islower():
    lower += x
   else:
    upper += x
print(lower+upper)'''

'''stored string
str ='asdfgfghjk'
n = sorted(str)
print(n)
str2=''.join(n)
print(str2)'''

'''Data Cleaning
scan = 'I am+Viplav reddy#chennupalli and i have recently0graduted from university+of north+texas'
clean = ''
for x in scan:
    if x.isalpha() or x.isspace():
        clean = clean + x
    else:
        clean += ' '
print(clean)'''

'''password project
pass1 = input('new pass: ')
pass2 = input('new pass: ')

if pass1==pass2:
    print('pass changed')
else:
    if pass1.casefold() == pass2.casefold():
        print('check pass is case sensitive')
    else:
        print('it is not matching')'''
'''
print('hello ',' world', sep='-', end='\t')
print('Viplav')
'''
'''
num = 123456
print('start {0:^15e} end'.format(num))
'''
'''triangle pattern
n = 6
for i in range(n):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()'''

'''class and Object
class candle:
    def __init__(self, color, scent):
        self.color = color
        self.scent = scent
    def burn(self):
        return f"the {self.color} candle with {self.scent} scent is buring."
candle1 = candle('red', "lavender")
candle2 = candle("purple", "choco")

print(candle1.burn())
print(candle2.burn())
'''
'''
l1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'Burger']
l2 = ['Burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

index1 = 10
index2 = 10

for i in range(len(l1)):
    indx = l2.index(l1[i])

    if i + indx < index1 + index2:
        index1 = i
        index2 = indx

print(l1[index1], index1 + index2)
'''
'''
l1 = [3, 4, 5 ,6, 7, 8, 9, 10, 11]
l2 = [4, 5, 6, 7, 8, 9, 11, 20,30]
l3 = []

for x in l1:
    if x in l2:
        l3.append(x)
print(l3)
'''
'''
def fun(length, breadth, height):
    vol = length*breadth*height
    return vol

v = fun(10,5,3)
print(v)
'''
'''
def result(mrk1, mrk2, mrk3):
    total = mrk1 + mrk2 + mrk3
    percent = total/3
    if percent >= 45:
        grade = 'pass'
    else:
        grade = 'fail'
    return total,percent,grade

print(result(55,60,70))
'''
'''
r = range(4)
print(r)
v = iter(r)
r.next(v)
print(r)
'''
'''
def days():
    d = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
    i = 0
    while True:
        yield d[i]
        i = (i + 1) % 7
m = days()
for day in m:
    print(day)
'''
'''
def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)

f = fact(5)
print(f)
'''

'''
def add(x, y):
    return (x+y)

def sub(x, y):
    return(x-y)

def artimetic(f, x, y):
    return f(x, y)

sum = print(add(10, 5))
diff = print(sub(10, 5))
print(add,diff)
'''
'''
a = 120
temp = a
sum = 0
if temp > 0:
    sum = temp%10
    temp = sum//10
    print("it is a armstrong number")
else:
    print("it is not amrstrong number")
'''
'''
a = [2, 3, 4, 5, 6]

sum = 0

for i,num in enumerate(a):
    sum += i
    print(sum)
'''

''' fibonocci series
x = int(input("enter any number :"))
a = 0
b = 1

for i in range(x):
    c = a + b
    a = b
    b = c
    print(a)
    '''


'''
n = 6
for i in range(n//2, n, 2):
    for j in range(1, n - i, 2):
        print(" ", end="")
    for j in range(1, i + 1):
        print(".", end="")
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print(".", end="")
    print()
    '''
n = 6
for i in range(n, 0, - 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(".", end="")
    print()


'''
n = 6
for i in range(n):
    for j in range(n):
        print(' * ', end ='')
    print()
'''
'''
n = 6
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    '''