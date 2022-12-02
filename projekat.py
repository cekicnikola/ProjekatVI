
from sys import stdout


"""

#for index,k in enumerate(prva):
  stdout.write(str(k))
    stdout.write(str(prva[index+1]))
    print()
#print(prva)

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
    def isValidMove(self, row, colu):
        #Validacija za X
        if(row > self.rows or row+1 > self.rows):
            print("Unete koordinate su van domasaja table!")
            return False
        elif (self.table[row][colu] != 0 or self.table[row+1][colu] != 0):
            print("Unete koordinate su zauzete!")
            return False
    #Validacija za O
        if(colu > self.columns or colu+1 > self.columns):
            print("Unete koordinate su van domasaja table!")
            return False
        elif (self.table[row][colu] != 0 or self.table[row][colu+1] != 0):
            print("Unete koordinate su zauzete!")
            return False
        return True

def Move(g:GameInfo,player,row,column):
    if(player=="X"):
        if(g.isValidMove(row,column)):
            g.table[row][column]="X"
            g.table[row+1][column]="X"
    elif(player=="O"):
        if(g.isValidMove(row,column)):
            g.table[row][column]="O"
            g.table[row][column+1]="O"
         








def main():
    tabla=GameInfo(7,6,"X","O")
    tabla.table[0][1]="X"
    tabla.table[1][1]="X"
    tabla.table[0][2]="O"
    tabla.table[0][3]="O"
    tabla.printTable()
    print()
    Move(tabla,"X",1,1)
    tabla.printTable()
main()




