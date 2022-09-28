import random
from random import randrange


def createArr():
    i = []
    for n in range(1, 46):
        i.append(n)
    return i


def ziehung():
    zahlen = createArr()
    for i in range(0,6):
        g = randrange(45-i)
        zahlen[g], zahlen[44-i] = zahlen[44-i], zahlen[g]
    return zahlen[-6:]

liste = []

for i in range(1000000):
    liste = liste + ziehung()
    
for i in range(45):
    print(i+1, "=" ,liste.count(i))
