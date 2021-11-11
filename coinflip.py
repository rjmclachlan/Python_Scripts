import random
from collections import Counter
import matplotlib.pyplot as plt

results=[]
diereults=0

while diereults < 10000:
    x=random.randint(0,6)
    y=random.randint(0, 6)
    results.append(x+y)
    diereults = diereults+1

presults= Counter(results)
#print(presults)


x = presults.keys()
y = presults.values()

plt.bar(x,y)


plt.show()