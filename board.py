
EMPTY = 0
BLACK_PIECE = 1
RED_PIECE = 2

class Board:
    def __init__(self, screen_width, screen_height):
        self.columns = []
        self.width = 64*7
        self.height = 64*6

        self.x = (screen_width-self.width)/2
        self.y = (screen_height-self.height)/2

    def draw(self, screen):
        for i in range(7):
            for j in range(6):
                
