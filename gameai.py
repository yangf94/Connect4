import random
from threading import Thread
from board import Board
import time

class GameAI:
    def __init__(self):
        self.move = -1
        self.running = False
        self.done = False
    def calculateMove(self, board, aiPiece, humanPiece):
        thread = Thread(target = self.calculate, args = (board, aiPiece, humanPiece))
        self.running = True
        self.done = False
        thread.start()
    def calculate(self, board, aiPiece, humanPiece):
        pass

    def getMove(self):
        move = self.move
        self.move = -1
        self.running = False
        self.done = False
        return move
    
class Level1AI(GameAI):
    def __init__(self):
        super().__init__()

    def calculate(self, board, aiPiece, humanPiece):
        possible = []
        
        for i in range(7):
            if(board.canInsertIntoColumn(i)):
                possible.append(i)

        if(len(possible)>0):
            self.move = random.choice(possible)
        self.done = True
