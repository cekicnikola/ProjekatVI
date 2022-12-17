
from sys import stdout


"""

#for index,k in enumerate(prva):
  stdout.write(str(k))
    stdout.write(str(prva[index+1]))
    print()
#print(prva)

"""
class GameInfo:
    def __init__(self, rows, columns,player,AIplayer,player2):
        self.rows=rows
        self.columns=columns
        self.player=player
        self.AIplayer=AIplayer
        self.player2=player2
        self.table=[]
        self.letter =[]
        self.winner=True
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
            stdout.write(str(i+1)+ "| ")
            for j in range(0,self.columns):
                if(self.table[i][j]==0):
                    stdout.write("*" + " ")
                elif(self.table[i][j]=="X"):
                    stdout.write("X" + " ")
                elif(self.table[i][j]=="O"):
                    stdout.write("O" + " ")
            print()

    def isValidMove(self, row, colu, player):
        if(player == "X"): #Validacija za X
            if(row > self.rows or row+1 > self.rows):
                print("Unete koordinate su van domasaja table!")
                return False
            elif (self.table[row][colu] != 0 or self.table[row+1][colu] != 0):
                print("Unete koordinate su zauzete!")
                return False
        elif(player == "O"):    #Validacija za O
            if(colu > self.columns or colu+1 > self.columns):
                print("Unete koordinate su van domasaja table!")
                return False
            elif (self.table[row][colu] != 0 or self.table[row][colu+1] != 0):
                print("Unete koordinate su zauzete!")
                return False
            return True

    def winnerChecker(self)->bool:
        self.winner=True
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                #checking rows
                if(self.table[i][j]=="O" and self.table[i][j+1]=="O"): 
                    if(self.table[i][j]=="X" and self.table[i+1][j]=="X"): 
                        self.winner=False
                #checking columns
                if(self.table[i][j]=="X" and self.table[i+1][j]=="X"):
                    if(self.table[i][j]=="O" and self.table[i][j+1]=="O"):
                        self.winner=False
        return self.winner


def move(g:GameInfo,player,row,column):
    col=g.letter.index(column)
    convertedRow=row-1
    if(player=="X"):
        if(g.isValidMove(convertedRow,col)):
            g.table[convertedRow][col]="X"
            g.table[convertedRow+1][col]="X"
    elif(player=="O"):
        if(g.isValidMove(convertedRow,col)):
            g.table[convertedRow][col]="O"
            g.table[convertedRow][col+1]="O"
         
def sizeOfTable()->tuple[int,int]:
    print()
    print()
    print("------------------Dobrodosli u Domineering------------------")
    print("Molimo Vas unesite dimenzije table.")
    print("Unesite broj vrsta:")
    rows=int(input())
    print("Unesite broj kolona:")
    columns=int(input())
    return (rows,columns)

def chooseFirst()->tuple[str,str]:
    twoPlayers=int(input("Unesite 1, ako zelite da igrate protiv racunara. U suprotnom 0, ako zelite da igru igraju dva igraca."))
    if(twoPlayers==0):
        return ("X","O")
    else:

        print("Unesite 1, ako Vi zelite da igrate prvi. U suprotnom 0, ako igra racunar")
        value=int(input())
        if(value==1):
            return ("X","O")
        elif(value==0):
            return("O","X")
        else:
            print("Unesite ponovo vrednosti")
            return chooseFirst()




def main():
    dim=sizeOfTable()
    player=chooseFirst()
    game=GameInfo(dim[0],dim[1],player[0],player[1],player[1])
    
    
    move(game,"X",1,"b")
    move(game,"O",8,"b")
    game.printTable()
    print(game.winnerChecker())
main()




