
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
        stdout.write("    ")
        for z in range(0,self.columns):
            stdout.write(self.letter[z] + " ") 
        print()      
        for i in range(0,self.rows):
            if(i<9):
                stdout.write(str(i+1)+ " | ")
            else:
                stdout.write(str(i+1)+ "| ")
            for j in range(0,self.columns):
                if(self.table[i][j]==0):
                    stdout.write("*" + " ")
                elif(self.table[i][j]=="X"):
                    stdout.write("X" + " ")
                elif(self.table[i][j]=="O"):
                    stdout.write("O" + " ")
            print()

    def isValidMove(self, row, colu, player)->tuple[bool,str]:
        if(player == "X"):      #Validacija za X
            if(row > self.rows or row+1 > self.rows):
                return (False,"Unete koordinate su van domasaja table!")
            elif (self.table[row][colu] != 0 or self.table[row+1][colu] != 0):
                return (False,"Unete koordinate su zauzete!")
            return (True,"Koordinate su ispravne")
        elif(player == "O"):    #Validacija za O
            if(colu > self.columns or colu+1 > self.columns):
                return (False,"Unete koordinate su van domasaja table!")
            elif (self.table[row][colu] != 0 or self.table[row][colu+1] != 0):
                return (False,"Unete koordinate su zauzete!")
            return (True,"Koordinate su ispravne")

    def winnerChecker(self)->bool:
        if(len(self.possibleMove("X"))==0 or len(self.possibleMove("O"))==0):
            return True
        else:
            return False
        

    def possibleMove(self, player):
        moveX = []
        moveY = []

        if(player == "X"):
            for i in range(0,self.rows-1):
                for j in range(0,self.columns):            
                    coord = []    
                    if(self.isValidMove(i,j,"X")[0]):         
                        coord.append(i+1)
                        coord.append(j+1)
                        moveX.append(coord)                        
            return moveX
        if(player == "O"):
            for i in range(self.rows):
                for j in range(self.columns-1):            
                    coord = []    
                    if(self.isValidMove(i,j,"O")[0]):         
                        coord.append(i+1)
                        coord.append(j+1)
                        moveY.append(coord)                        
            return moveY



def move(g:GameInfo,player,row,column):
    col=g.letter.index(column)
    convertedRow=int(row-1)
    if(player=="X"):
        if(g.isValidMove(convertedRow,col,"X")[0]):
            g.table[convertedRow][col]="X"
            g.table[row][col]="X"
    elif(player=="O"):
        if(g.isValidMove(convertedRow,col,"O")[0]):
            g.table[convertedRow][col]="O"
            g.table[convertedRow][col+1]="O"

def makeAMove(g:GameInfo,player):
    igrac=""
    potez=""
    if(player=="X"):
        igrac="prvi"
        potez="vertikalno"
    elif(player=="O"):
        igrac="drugi"
        potez="horizontalno"
    
    print(f"Na potezu je {igrac} igrac, koji igra {potez}. Izaberite koordinate poteza. Unesite vrednost vrste: ")
    r=int(input("Unos vrste(mora biti ceo broj): "))
    print("Unesite vrednost kolone(slovo): ")
    c=str(input("Unos kolone: "))
   
    #greska=uslov[1]
    col=g.letter.index(c)
    filledValue= g.isValidMove(r-1,col,player)
    if((r not in range(0,g.rows + 1) or (c not in g.letter)) or not(filledValue[0]) ):
        return makeAMove(g,player)
    else:
        move(g,player,r,c)
        
    
    g.printTable()
    print(f"Potez iznad je odigrao {igrac} igrac ")
    print("")
    
  
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
    print("Unesite 1, ako zelite da igrate protiv racunara. U suprotnom 0, ako zelite da igru igraju dva igraca.")
    twoPlayers=int(input("Unos:"))
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
    game.printTable()
    
    
    while(not game.winnerChecker()):
       makeAMove(game,game.player)
       makeAMove(game,game.player2)
       
    print("Kraj igre")
    if(len(game.possibleMove(game.player)) !=0):
        print("Pobednik je prvi igrac")
    if(len(game.possibleMove(game.player2)) !=0 ):
        print("Pobednik je drugi igrac")
    
    
    
main()




