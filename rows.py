"""class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

class cuboid(Rectangle):
    def __init__(self, h , l, b):
        self.height=h
        super().__init__(l, b)

    def volumn(self):
        return self.length * self.breadth * self.height

c = cuboid(10, 3 , 5)
print(c.volumn()).



"""
"""str = "qwertyuiop"
n = sorted(str)
print(n)
str1='--'.join(n)
print(str1)"""

"""credit_card = input('Please enter the card number: ')
Last_four_digits = credit_card[9::]
First_digits = '*' * 4 + ' '
Valid_card = First_digits * 3 + Last_four_digits
print(Valid_card)

"""
"""n = int(input("enter any numebr: "))
while(n <= 5 ):
    print('hi' +str(n))
    n += 1

"""
a = int(input('Any number'))
rev = 0

while a>0:
    r = a%10  # reminder
    a = a//10 # cofieciant
    rev = (rev*10)+r
    print(rev)