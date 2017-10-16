import pygame
from gui import MessageBox
from gamestate import GameState
from board import Board

class PlayableState(GameState):
    PLAYER1_TURN = False
    PLAYER2_TURN = True
    def __init__(self, game):
        super().__init__(game)
        self.board = Board(self.game.width, self.game.height)

        self.player1Piece = Board.RED_PIECE
        self.player2Piece = Board.BLACK_PIECE

        self.turn = False

        self.heldPiece = None

        self.gameOver = False

        self.gameOverMessageBox = MessageBox("Game Over", action=self.exitState)
    def exitState(self):
        self.game.state_stack.pop()

    def checkInputs(self):
        pos = pygame.mouse.get_pos()
        column = int((pos[0]-self.board.x)/self.board.pieceSize)
        if(column>=0 and column<7 and (not self.gameOver)):
            self.heldPiece = ((self.board.x+column*self.board.pieceSize), (self.board.y-self.board.pieceSize))
        else:
            self.heldPiece = None
