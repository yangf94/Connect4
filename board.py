

class Board:
    EMPTY = 0
    BLACK_PIECE = 1
    RED_PIECE = 2
    
    def __init__(self, screen_width, screen_height):
        self.columns = []
        for i in range(7):
            self.columns.append([])
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
                if(self.columns[i][j] == RED_PIECE):
                    screen.blit(resources.get("red piece"), (x,y))
                elif(self.columns[i][j] == BLACK_PIECE):
                    screen.blit(resources.get("black piece"), (x,y))
    def canInsertIntoColumn(self, column):
        return len(self.columns[column])<6

    def insertIntoColumn(self, column, piece):
        print(self.columns)
        if(self.canInsertIntoColumn(column)):
            self.columns[column].append(1)
        print(self.columns)
