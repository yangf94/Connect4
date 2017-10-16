
class Board:
    EMPTY = 0
    BLACK_PIECE = 1
    RED_PIECE = 2
    
    def __init__(self, screen_width, screen_height):
        self.columns = []
        for i in range(7):
            self.columns.append([Board.EMPTY]*6)
        self.tops = [0]*7
        self.pieceSize = 64
        self.width = self.pieceSize*7
        self.height = self.pieceSize*6

        self.x = (screen_width-self.width)/2
        self.y = (screen_height-self.height)/2

    def draw(self, screen, resources):
        for i in range(7):
            for j in range(6):
                x = self.x+64*i
                y = self.y+64*j
                screen.blit(resources.get("board"), (x,y))

            for j in range(len(self.columns[i])):
                x = self.x+64*i
                y = (self.y+self.height)-(j+1)*64
                if(self.columns[i][j] == Board.RED_PIECE):
                    screen.blit(resources.get("red piece"), (x,y))
                elif(self.columns[i][j] == Board.BLACK_PIECE):
                    screen.blit(resources.get("black piece"), (x,y))
    def canInsertIntoColumn(self, column):
        return self.tops[column]<6

    def insertIntoColumn(self, column, piece):
        if(self.canInsertIntoColumn(column)):
            self.columns[column][self.tops[column]] = piece
            self.tops[column]+=1
    def checkDraw(self):
        for i in range(7):
            if(self.canInsertIntoColumn(i)):
                return False
        return True
    def checkWin(self, piece):
        for i in range(6):
            if(self.checkRow(piece, i)):
                return True

        for i in range(7):
            if(self.checkColumn(piece, i)):
                return True
        if(self.checkDiagonals(piece)):
            return True
        
        return False
    def checkRow(self, piece, row):
        count = 0
        for i in range(7):
            if(self.columns[i][row]==piece):
                count+=1
                if(count==4):
                    return True
            else:
                count = 0
        return False
    def checkColumn(self, piece, column):
        count = 0
        for i in range(6):
            if(self.columns[column][i]==piece):
                count+=1
                if(count==4):
                    return True
            else:
                count = 0
        return False

    def checkDiagonals(self, piece):
        for i in range(4):
            for j in range(3):
                count = 0
                for k in range(4):
                    if(self.columns[i+k][j+k]==piece):
                        count+=1
                        if(count==4):
                            return True
                    else:
                        break
        
        for i in range(6, 2, -1):
            for j in range(3):
                count = 0
                for k in range(4):
                    if(self.columns[i-k][j+k]==piece):
                        count+=1
                        if(count==4):
                            return True
                    else:
                        break
        return False
