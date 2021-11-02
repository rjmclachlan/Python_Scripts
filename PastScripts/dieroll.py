import random


def dieroll(sides):
    x = random.randint(1,sides)
    return x
i=0
DR=[]
while i < 100:
    Y=dieroll(10)
    DR.append(Y)
    i=i+1

d = {x:DR.count(x) for x in DR}
print(sorted(d.items()))
print(d)




