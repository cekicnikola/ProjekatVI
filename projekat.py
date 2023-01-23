
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
            if(row > self.rows or row+1 > self.rows-1):
                return (False,"Unete koordinate su van domasaja table!")
            elif (self.table[row][colu] != 0 or self.table[row+1][colu] != 0):
                return (False,"Unete koordinate su zauzete!")
            return (True,"Koordinate su ispravne")
        elif(player == "O"):    #Validacija za O
            if(colu > self.columns or colu-1 < 0):
                return (False,"Unete koordinate su van domasaja table!")
            elif (self.table[row][colu] != 0 or self.table[row][colu-1] != 0):
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
            for i in range(self.rows-1):
                for j in range(self.columns):            
                    coord=[]
                    if(self.isValidMove(i,j,"X")[0]):         
                        coord.append(i) 
                        coord.append(j)    
                        moveX.append(coord)                       
            return moveX
        if(player == "O"):
            for i in range(self.rows):
                for j in range(self.columns): 
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
                self.table[row][column-1]=0

    def emptyFieldX(self, tabla):
        allX = []
        for i in range(self.rows-1):
            for j in range(self.columns):
                coord = []
                if((tabla[i][j] == 0 and tabla[i+1][j] == 0) and self.isValidMove(i,j,"X")[0]):                     
                    coord.append(i)
                    coord.append(j)
                    allX.append(coord)                        
        return allX

    def emptyFieldO(self, tabla):
        allY = []
        for i in range(self.rows):
            for j in range(self.columns):
                coord = []
                if((tabla[i][j] == 0 and tabla[i][j-1] == 0) and self.isValidMove(i,j,"O")[0]):                    
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
            g.table[convertedRow][col-1]="O"

def compMove(g:GameInfo, player, row, column):
    if(player=="X"):
        if(g.isValidMove(row,column,"X")[0]):
            g.table[row][column]="X"
            g.table[row+1][column]="X"

    elif(player=="O"):
        if(g.isValidMove(row,column,"O")[0]):
            g.table[row][column]="O"
            g.table[row][column-1]="O"

    return g.table

def makeACompMove(g:GameInfo,player,row, column):
    filledValue= g.isValidMove(row,column,player)
    if( not(filledValue[0])):
        listOfCoords=g.possibleMoves(player)
        coords= listOfCoords[0]
        compMove(g,player,coords[0],coords[1])
        
    else:
        compMove(g, player,row, column)
        return g.table



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
    while True:
        try:
            r=int(input(f"Unos vrste(broj od 1 do {g.rows}): "))
            if(r not in range(1,g.rows+1)):
                print(f"Vrednost mora biti broj od 1 do {g.rows})!")
                continue
            break            
        except ValueError:
            print(f"Vrednost mora biti broj od 1 do {g.rows})!")

    """    r=int(input("Unos vrste(mora biti ceo broj): "))
    print("Unesite vrednost kolone(slovo): ")
    """
    while True:
        try:
            c=str(input("Unos kolone:(malo slovo) "))
            col=g.letter.index(c)
            if(col not in range(g.columns)):
                print(f"Vrednost mora biti slovo u opsegu {g.letter})!")
                continue
            break            
        except ValueError:
            print(f"Vrednost mora biti slovo u opsegu {g.letter})")
 
    #greska=uslov[1]
    col=g.letter.index(c)
    filledValue= g.isValidMove(r-1,col,player)
    if((r not in range(0,g.rows + 1) or (c not in g.letter)) or not(filledValue[0]) ):
        print("Koordinate koje ste uneli su zauzete ili su izvan tabele!")
        print("")
        return makeAMove(g,player)
    else:
        move(g,player,r,c)
        
    g.printTable()
    print(f"Potez iznad je odigrao {igrac} igrac, koji igra {potez}. ")
    print("")



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
  
  
def sizeOfTable()->tuple[int,int]:
    print()
    print()
    print()
    print("------------------Dobrodosli u Domineering------------------")
    print("Molimo Vas unesite dimenzije table.")
    while True:
        try:
            rows = int(input("Unesi broj vrsta: "))
            if(rows not in range(1,26)):
                print("Broj vrsti mora biti izmedju 1 i 26!")
                continue
            break            
        except ValueError:
            print("Vrednosti moraju biti  brojevi, unesite ponovo...")
    while True:
        try:
            columns = int(input("Unesi broj kolona: "))
            print()
            if(columns not in range(1,26)):
                print("Broj kolona mora biti izmedju 1 i 26!")
                continue
            break
        except ValueError:
            print("Vrednosti moraju biti  brojevi, unesite ponovo...")            
    return (rows,columns)

def chooseFirst()->tuple[str,str]:
    print("Unesite 1, ako zelite da igrate protiv racunara.")
    print("U suprotnom 0, ako zelite da igru igraju dva igraca.")    
    while True:
        try:
            twoPlayers = int(input("Unesi broj: "))
            print()
            if(twoPlayers == 0 or twoPlayers == 1):
                break
            print("Vrednost mora biti  broj  1 ili 0!")
            continue            
        except ValueError:
            print("Vrednost mora biti  broj  1 ili 0!")
    if(twoPlayers==0):
        print("-----Igru igraju dva igraca.-----\n")
        return ("X","O",False)
    else:
        print("-----Igru igraju igrac i racunar.-----\n")
        print("Unesite 1, ako Vi zelite da igrate prvi. U suprotnom 0, da racunar igra prvi")       
        while True:
            try:
                value = int(input("Unesi broj: "))
                print()
                if(value == 0 or value == 1):
                    break
                print("Vrednost mora biti  broj izmedju 1 i 0!")
                continue            
            except ValueError:
                print("Vrednost mora biti  broj izmedju 1 i 0!")

        if(value==1):
            print("-----Igrac igra prvi!-----")
            return ("X","O",True)
        elif(value==0):
            print("-----Racunar igra prvi!-----")
            return("O","X",True)
    
    
    """twoPlayers=int(input("Unos:"))
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
            return chooseFirst()"""


def getPosibilitiesHeurO(g:GameInfo):
    return len(g.possibleMoves("O"))-len(g.possibleMoves("X"))
def getPosibilitiesHeurX(g:GameInfo):
    return len(g.possibleMoves("X"))-len(g.possibleMoves("O"))

def max_stanje(lsv):
    return max(lsv, key=lambda x: x[1])
    
def min_stanje(lsv):
    return min(lsv, key=lambda x: x[1])   

def minimax(stanje:GameInfo,state, dubina, moj_potez, potez = None):
    copyGame:GameInfo = deepcopy(stanje)
    igrac = "X" if moj_potez else "O"
    funkcija_min_max = max_stanje if moj_potez else min_stanje
    if(igrac == "X"):    
        lista_poteza = list(copyGame.emptyFieldX(state))    
    elif(igrac =="O"):
        lista_poteza = list(copyGame.emptyFieldO(state)) 
        
    if dubina == 0 or len(lista_poteza) == 0:
        if(igrac=="X"):
            return (potez, getPosibilitiesHeurX(copyGame)) ###
        else: 
            return (potez, getPosibilitiesHeurO(copyGame))
    #print(f'za {igrac}:{lista_poteza}')
    scores=[]
    for x in lista_poteza:
        
        tabla=compMove(copyGame,igrac, x[0] , x[1])
        scores.append(minimax(copyGame,tabla, dubina - 1, not moj_potez, x ) )
        copyGame.remove(igrac,x[0],x[1])
        #print(f'Potez{igrac} {x}')

    """print(scores)
    print("============================================")"""
    return funkcija_min_max(scores)

def miniMaxAlfaBetaOdsecanje(stanje:GameInfo, igrac, dubina:int = 0, alpha=(None,-55000), beta=(None,55000)):
    copyGame:GameInfo = deepcopy(stanje)
    copyGame.minMax = []
    #if alfa == None: alpha = (copyGame, -stanje.rows*stanje.columns)
    #if beta == None:  beta = (copyGame,  stanje.rows*stanje.columns)
    
    if (igrac):
        return maxState(copyGame, dubina, alpha, beta)
    else:
        return minState(copyGame, dubina, alpha, beta)

def maxState(stanje:GameInfo, dubina, alpha,beta,potez = None):
       
    lista_poteza = list(stanje.emptyFieldX(stanje.table))    
            
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        
        return (potez, getPosibilitiesHeurX(stanje)) ###
       
    #print(f'za {igrac}:{lista_poteza}')
    else:
        for x in lista_poteza:
        
            compMove(stanje,"X", x[0] , x[1])
            alpha=max(alpha,minState(stanje,dubina-1,alpha,beta, x if potez is None else potez),key = lambda y:y[1]) 
            stanje.remove("X",x[0],x[1])
            if alpha[1] >= beta[1]:
                return beta

    return alpha

    

   
def minState(stanje:GameInfo, dubina, alpha,beta,potez = None):
       
    lista_poteza = list(stanje.emptyFieldO(stanje.table))    
      
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        
        return (potez, getPosibilitiesHeurO(stanje)) ###
       
    #print(f'za {igrac}:{lista_poteza}')
    else:
        for x in lista_poteza:
        
            compMove(stanje,"O", x[0] , x[1])
            beta=min(beta,maxState(stanje,dubina-1,alpha,beta, x if potez is None else potez),key = lambda y:y[1]) 
            stanje.remove("O",x[0],x[1])
            if beta[1] <= alpha[1]:
                return alpha

    return beta




def main():
    dim=sizeOfTable()
    player=chooseFirst()
    game=GameInfo(dim[0],dim[1],player[0],player[1],player[1])
    game.printTable()
    
    if(player[2]):
        if(game.AIplayer == "X"):
            potez=True
            while(not game.winnerChecker()):  
                move=miniMaxAlfaBetaOdsecanje(game,potez,4)
                naj = move[0] if type(move[0]) is list else (0, 0)

                print(move)
                makeACompMove(game,game.AIplayer,naj[0], naj[1])     #
                game.printTable() 
                makeAMove(game,game.player)
                
        else:
            potez=False
            while(not game.winnerChecker()):  
                makeAMove(game,game.player)      
                move=miniMaxAlfaBetaOdsecanje(game,potez,3)
                naj = move[0] if type(move[0]) is list else (0, 0)
                print(move)
                makeACompMove(game,game.AIplayer,naj[0], naj[1])  
                game.printTable()   
                    
    else:
        while(not game.winnerChecker()):         
            makeAMove(game,game.player)      
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




