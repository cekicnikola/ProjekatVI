
from sys import stdout
"""

prva=[]



slova=["a","b","c","d","e"]

i = 5
j = 5
druga=[]
for x in range(0,i):
    prva.append((slova[x],druga))
    
for y in range(0,j):

        druga.append(1)

#for index,k in enumerate(prva):
  stdout.write(str(k))
    stdout.write(str(prva[index+1]))
    print()
#print(prva)

broj= list(filter(lambda x:  x[0]=='d',prva))
broj=broj[0][1][2]
print(broj)




recnik=dict()
slova=["a","b","c","d","e"]

i = 5
j = 5
druga=[]
for y in range(0,j):

   druga.append(0)
for x in range(0,i):
    recnik[slova[x]]=druga

print(recnik.get("d")[1]) 
print(recnik)

lista=list(recnik["d"])
lista[3]=5
recnik["d"]=lista
print(recnik)


tabla=[[5,6,7],[8,9,10],[12,13,14]]
print(tabla[1][1])


def putDomino():
    return 0

def validMove(x:int,y:int):
    return 0


r = 0
c = 0

def dimension():
    r = int(input("enter rows"))
    c = int(input("enter columns"))
m=[]
def createBoard():
    for i in range (r):
        l=[]
        for j in range (c):
            v = int(input())
            l.append(v)
    m.append(l)

def printBoard():
    stdout.write(m)
def play():
    dimension()
    createBoard()
    printBoard()
play()
"""
v = '*'
r = int(input("enter rows: "))
c = int(input("enter columns: "))
m=[]
for i in range (r):
    l=[]
    for j in range (c):
        #v = "-"   #int(input())
        l.append(v)
    m.append(l)
for a in range(0,r):
    print(m[a])