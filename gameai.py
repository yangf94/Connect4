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
        self.done = True

    def getMove(self):
        move = self.move
        self.move = -1
        self.running = False
        self.done = False
        return move

    def simplestEvaluation(self, board, aiPiece, humanPiece, move):
        score = 0
        board.insertIntoColumn(move, aiPiece)
        
        if(board.checkWin(aiPiece)):
            score = 100

        board.removeFromColumn(move)

        return score
    
class Level1AI(GameAI):
    def __init__(self):
        super().__init__()

    def calculate(self, board, aiPiece, humanPiece):
        super().calculate(board, aiPiece, humanPiece)
        possible = []
        
        for i in range(7):
            if(board.canInsertIntoColumn(i)):
                possible.append(i)

        if(len(possible)>0):
            self.move = random.choice(possible)
        
class Level2AI(GameAI):
    def __init__(self):
        super().__init__()

    def calculate(self, board, aiPiece, humanPiece):
        possible = []
        
        for i in range(7):
            if(board.canInsertIntoColumn(i)):
                possible.append(i)

        bestMoves = []
        bestScore = 0
        for p in possible:
            score = self.simplestEvaluation(board,aiPiece,humanPiece,p)
            if(score==bestScore):
                bestMoves.append(p)
            elif(score>bestScore):
                bestScore = score
                bestMoves = []
                bestMoves.append(p)
        print(bestMoves)
        self.move = random.choice(bestMoves)
        super().calculate(board, aiPiece, humanPiece)

