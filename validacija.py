from sys import stdout


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
                stdout.write(str(self.table[i][j]) + " ")
            print(" ")


tabla=GameInfo(8,26,"X","O")
tabla.printTable()

