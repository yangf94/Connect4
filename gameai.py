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

    def getMove(self):
        move = self.move
        self.move = -1
        self.running = False
        self.done = False
        return move

    def evaluateBoard(self, board, aiPiece, humanPiece):
        score = 0
        
        if(board.checkWin(aiPiece)):
            score = 100

        return score

    def getPossibleMoves(self, board):
        possible = []

        for i in range(7):
            if (board.canInsertIntoColumn(i)):
                possible.append(i)

        return possible
    
class Level1AI(GameAI):
    def __init__(self):
        super().__init__()

    def calculate(self, board, aiPiece, humanPiece):
        possible = self.getPossibleMoves(board)

        if(len(possible)>0):
            self.move = random.choice(possible)

        # telling the thread that the AI is done evaluating a move
        self.done = True
        
class Level2AI(Level1AI):
    def __init__(self):
        super().__init__()

    def calculate(self, board, aiPiece, humanPiece):
        possible = self.getPossibleMoves(board)

        bestMoves = []
        bestScore = 0
        for move in possible:
            # Temporarily add piece to board to evaluate board state
            board.insertIntoColumn(move, aiPiece)

            score = self.evaluateBoard(board,aiPiece,humanPiece)
            if(score==bestScore):
                bestMoves.append(move)
            elif(score>bestScore):
                bestScore = score
                bestMoves = []
                bestMoves.append(move)

            # Remove temporarily added piece from board
            board.removeFromColumn(move)

        self.move = random.choice(bestMoves)

        # telling the thread that the AI is done evaluating a move
        self.done = True


class Level3AI(Level2AI):
    def __init__(self):
        super().__init__()

    def calculate(self, board, aiPiece, humanPiece):
        possible = self.getPossibleMoves(board)

        bestMoves = []
        bestScore = 0
        for move in possible:
            # Temporarily add piece to board to evaluate board state
            board.insertIntoColumn(move, aiPiece)

            score = self.evaluateBoard(board,aiPiece,humanPiece)

            # Remove temporarily added piece from board
            board.removeFromColumn(move)

            # Temporarily add human piece to board to see if human can win
            board.insertIntoColumn(move, humanPiece)

            score += 2*self.evaluateBoard(board, humanPiece, aiPiece)

            # Remove temporarily added piece from board
            board.removeFromColumn(move)

            if(score==bestScore):
                bestMoves.append(move)
            elif(score>bestScore):
                bestScore = score
                bestMoves = []
                bestMoves.append(move)

        self.move = random.choice(bestMoves)
        print(self.move)

        # telling the thread that the AI is done evaluating a move
        self.done = True

