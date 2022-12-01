
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

v = str("l")
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
    print(" ")
    for i in range(0,r):
       stdout.write(m[a][i] + " ")
def printBoard():
    m=[]
    for i in range (r):
        l=[]
        for j in range (c):
            #v = "-"   #int(input())
            l.append(v)
        m.append(l)
    for a in range(0,r):
        print(" ")
        for i in range(0,r):
           stdout.write(m[a][i] + "  ")

printBoard()

def checkMovemant():
    return 0

def placeXtile():
    print("Enter coordinates for movemant: ")
    x = int(input("Enter number: "))
    y = int(input("enter columns: "))
    return 0


"""
class GameInfo:
    def __init__(self, rows, columns,player,AIplayer):
        self.rows=rows
        self.columns=columns
        self.player=player
        self.AIplayer=AIplayer
        self.table=[]
        self.letter =[]
        for z in range(0,self.columns):
            self.letter.append(chr(97 + z))

        for i in range (rows):
            l=[]
            for j in range (columns):
                l.append(0)
            self.table.append(l)


    def printTable(self):
        stdout.write("   ")
        for z in range(0,self.columns):
            stdout.write(self.letter[z] + " ") 
        print()      
        for i in range(0,self.rows):
            stdout.write(str(i)+ "| ")
            for j in range(0,self.columns):
                if(self.table[i][j]==0):
                    stdout.write("*" + " ")
                elif(self.table[i][j]=="X"):
                    stdout.write("X" + " ")
                elif(self.table[i][j]=="O"):
                    stdout.write("O" + " ")
            print()




def main():
    tabla=GameInfo(8,4,"X","O")
    tabla.table[0][1]="X"
    tabla.table[1][1]="X"
    tabla.table[0][2]="O"
    tabla.table[0][3]="O"
    tabla.printTable()
    print()
    print(tabla.letter[3])
main()


        




