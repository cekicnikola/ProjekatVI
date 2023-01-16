
from shutil import copystat
from sys import stdout
from copy import copy, deepcopy

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
        if(len(self.possibleMoves("X"))==0 or len(self.possibleMoves("O"))==0):
            return True
        else:
            return False
        

    def possibleMoves(self, player):
        moveX = []
        moveY = []

        if(player == "X"):
            for i in range(0,self.rows-1):
                for j in range(0,self.columns):            
                    coord=[]
                    if(self.isValidMove(i,j,"X")[0]):         
                        coord.append(i) 
                        coord.append(j)    
                        moveX.append(coord)                       
            return moveX
        if(player == "O"):
            for i in range(self.rows):
                for j in range(self.columns-1): 
                    coord=[]                                  
                    if(self.isValidMove(i,j,"O")[0]):         
                        coord.append(i) 
                        coord.append(j)    
                        moveY.append(coord)                       
            return moveY

    def remove(self, player, row, column):
        if(player=="X"):
                self.table[row][column]=0
                self.table[row+1][column]=0
        elif(player=="O"):
                self.table[row][column]=0
                self.table[row][column+1]=0




def emptyFieldX(g:GameInfo):
    allX = []
    for i in range(g.rows-1):
        for j in range(g.columns):
            coord = []
            if(g.table[i][j] == 0 and g.table[i+1][j] == 0):
                coord.append(i)
                coord.append(j)
                allX.append(coord)
    return allX
def emptyFieldO(g:GameInfo):
    allY = []
    for i in range(g.rows):
        for j in range(g.columns-1):
            coord = []
            if(g.table[i][j] == 0 and g.table[i][j+1] == 0):
                coord.append(i)
                coord.append(j)
                allY.append(coord)
    return allY





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

def compMove(g:GameInfo, row, column):
    if(g.AIplayer=="X"):
        if(g.isValidMove(row,column,"X")[0]):
            g.table[row][column]="X"
            g.table[row+1][column]="X"
    elif(g.AIplayer=="O"):
        if(g.isValidMove(row,column,"O")[0]):
            g.table[row][column]="O"
            g.table[row][column+1]="O"
          
    return g.table

def fakeMove(g:GameInfo,pos,igrac):
        return [[igrac if pos[0]==j and pos[1]==i else g.table[j][i] for i in range(0, g.columns) ] for j in range(0,g.rows)]

def allMoves(g:GameInfo):
    move = []
    for i in range(g.rows):
        for j in range(g.columns):            
            coord = []    
            if(g.table[i][j] == 0):         
                coord.append(i+1)
                coord.append(j+1)
                move.append(coord)                        
    return move


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
        return ("X","O",False)
    else:
        print("Unesite 1, ako Vi zelite da igrate prvi. U suprotnom 0, da racunar igra prvi")
        value=int(input())
        if(value==1):
            return ("X","O",True)
        elif(value==0):
            return("O","X",True)
        else:
            print("Unesite ponovo vrednosti")
            return chooseFirst()


def getPosibilitiesHeur(g:GameInfo):
    return len(g.possibleMoves("X"))-len(g.possibleMoves("O"))

def max_stanje(lsv):
    return max(lsv, key=lambda x: x[1])

def min_stanje(lsv):
    return min(lsv, key=lambda x: x[1])   

def minimax(stanje:GameInfo,state, dubina, moj_potez, potez = None):
    copyGame:GameInfo = deepcopy(stanje)
    igrac = "X" if moj_potez else "O"
    funkcija_min_max = max_stanje if moj_potez else min_stanje
    lista_poteza = list(copyGame.possibleMoves(igrac))
    if dubina == 0 or len(lista_poteza) == 0:
        return (potez, getPosibilitiesHeur(copyGame))
    return funkcija_min_max([minimax(copyGame,compMove(copyGame, x[0], x[1]), dubina - 1, not moj_potez, x ) for x in lista_poteza])


def miniMaxAlfaBetaOdsecanje(stanje:GameInfo, igrac, dubina:int = 0, alfa = None, beta= None):
    copyGame:GameInfo = deepcopy(stanje)
    copyGame.minMax = []
    if alfa == None: alpha = (copyGame, -stanje.rows*stanje.columns)
    if beta == None:  beta = (copyGame,  stanje.rows*stanje.columns)
    
    if (igrac == "X"):
        return maxValue(copyGame, dubina, alpha, beta, igrac)
    else:
        return minValue(copyGame, dubina, alpha, beta, igrac)


def maxValue(stanje, dubina, alfa, beta, igrac):
    listaPoteza = stanje.possibleMoves(igrac)
    
    if dubina == 0 or len(listaPoteza) == 0:
        return (stanje, getPosibilitiesHeur(stanje, "X", "O"))
    else:
        for potez in listaPoteza:  
            beta = min( beta, maxValue(potez, dubina - 1, alfa , beta), key = lambda x:x[1])
            if(alfa[1] > beta[1]):
                return beta
    return alfa
   
def minValue(stanje, dubina, alfa, beta, igrac):
    listaPoteza = stanje.possibleMoves(igrac)
    if dubina == 0 or len(listaPoteza) == 0:
        return (stanje, getPosibilitiesHeur(stanje, "X", "O"))
    else:
        for potez in listaPoteza:  
            beta = min( beta, maxValue(potez, dubina - 1, alfa , beta), key = lambda x:x[1])
            if(beta[1] < alfa[1]):
                
                return alfa
    return beta




def main():
    dim=sizeOfTable()
    player=chooseFirst()
    game=GameInfo(dim[0],dim[1],player[0],player[1],player[1])
    game.printTable()
    
    if(player[2]):
        if(game.AIplayer == "X"):
            while(not game.winnerChecker()):  
                move=minimax(game,game.table,3, True)
                naj = move[0] if type(move[0]) is list else (0, 0)
                print(move)
                compMove(game,naj[0], naj[1])     
                makeAMove(game,game.player)
        else:
            while(not game.winnerChecker()):  
                makeAMove(game,game.player)      
                move=minimax(game,game.table,3, True)
                naj = move[0] if type(move[0]) is list else (0, 0)
                print(move)
                compMove(game,naj[0], naj[1])         
    else:
        while(not game.winnerChecker()):         
            makeAMove(game,game.player)
            print(game.possibleMoves(game.player))      
            makeAMove(game,game.player2)    
    
       
    if(not player[2]):
        if(len(game.possibleMoves(game.player)) == len(game.possibleMoves(game.player2)) ==0):
            print("Pobednik je igrac koji je odigrao poslednji potez.")
        if(len(game.possibleMoves(game.player)) !=0):
            print("Pobednik je igrac koji igra vertikalno.")
        if(len(game.possibleMoves(game.player2)) !=0 ):
            print("Pobednik je igrac koji igra horizontalno.")
        print("===============KRAJ IGRE===============")
    else:
        if(len(game.possibleMoves(game.AIplayer)) == len(game.possibleMoves(game.player)) ==0):
            print("Pobednik je igrac koji je odigrao poslednji potez.")
        if(len(game.possibleMoves(game.AIplayer)) !=0):
            print("Pobednik je racunar.")
        if(len(game.possibleMoves(game.player)) !=0 ):
            print("Pobednik je igrac.")
        print("===============KRAJ IGRE===============")
    
    
main()




