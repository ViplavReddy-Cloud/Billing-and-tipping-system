'''a = int(input("Give a:"))
b = int(input("Give a:"))
c = int(input("Give a:"))

root1 = 0
root2 = 0
d = (b**2) - 4*a*c
root1 = (-b + (d**(0.5)))/2*a
root2 = (-b - (d**(0.5)))/2*a

print(f"Roots:({root1},{root2})")
'''

"""x = 20
y = 30

temp = x

x = y
y = temp
print(x , y)"""

"""x = int(input("give a value:"))
y = int(input("give a value:"))

temp = x
x = y
y = temp

print(f"value of:{x}")
print(f"value of:{y}")"""

"""x = 10
y = 20
y = y-x
x = y+x
print(x)
print(y)
"""

"""c = int(input("convert vaule:"))

f = c*(9/5) + 32
print(f)
"""

"""wheather = input("give the value:")
time_of_day = input("give the name:")

if wheather == "rainy":
    if time_of_day == "day":
        print("sleep", "have the dream", end=".")
elif wheather == "sunny" and time_of_day == "day":
    if wheather == "sunny":
        print("play with the balls")
    else:
        print("light the candles")
else:
    print("play indoor games")"""

"""a = "viplav's reddy"
print(a)
"""

n = 6
for i in range(1, n):
    for j in range(1, n):
        print('*', end = '_')
    print('')

a = 6
for i in range(1, n):
    for j in range(1, n):
        if i >= j:
            print("*", end = (' '))
    print('')

for i in range(1, 6):
    for j in range(1, i + 1):
        print("#", end = (' '))
    print('')

for i in range(1, 6):
    for j in range(1, 6 - (i - 1)):
        print("#", end=(' '))
    print('')