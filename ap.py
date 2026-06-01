class viplav:
    def sum(self, a, b, c=None):
        s = a + b
        if c==None:
           return s
        else:
           return s + c

v = viplav()
print(v.sum(10 , 5, 15))


