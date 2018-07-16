import pygame
import random
from gui import MessageBox
from playablestate import PlayableState
from board import Board
from gameai import *
import time

class OnePlayerState(PlayableState):
    def __init__(self, game, AILevel):
        super().__init__(game)

        self.humanTurn = None
        self.AITurn = None
    
        rand = random.randrange(2)
        if(rand==0):
            self.humanTurn = True
            self.AITurn = False
        else:
            self.humanTurn = False
            self.AITurn = True

        self.aiPiece = None
        self.humanPiece = None

        if(self.AITurn == OnePlayerState.PLAYER1_TURN):
            self.aiPiece = self.player1Piece
            self.humanPiece = self.player2Piece
            
        elif(self.AITurn == OnePlayerState.PLAYER2_TURN):
            self.aiPiece = self.player2Piece
            self.humanPiece = self.player1Piece

        if(AILevel==1):
            self.ai = Level1AI()
        elif(AILevel==2):
            self.ai = Level2AI()
        elif(AILevel==3):
            self.ai = Level3AI()
    
    def update(self):
        if(self.turn == self.AITurn and not self.gameOver):
            if(not self.ai.running):
                self.ai.calculateMove(self.board, self.aiPiece, self.humanPiece)
            elif(self.ai.done):
                move = self.ai.getMove()
                self.board.insertIntoColumn(move, self.aiPiece)
                if(self.board.checkWin(self.aiPiece)):
                    self.gameOver = True
                    self.gameOverMessageBox.text = "You lose"
                elif(self.board.checkDraw()):
                    self.gameOver = True
                    self.gameOverMessageBox.text = "Draw"
                    
                if(not self.gameOver):
                    self.turn = not self.turn
                
    def render(self):
        self.game.screen.fill((170,170,170))
        self.board.draw(self.game.screen, self.game.resources)
        
        if(self.heldPiece!=None and self.turn == self.humanTurn):
            if(self.turn == OnePlayerState.PLAYER1_TURN):
                piece = self.player1Piece
            elif(self.turn == OnePlayerState.PLAYER2_TURN):
                piece = self.player2Piece

            if(piece == Board.RED_PIECE):
                self.game.screen.blit(self.game.resources.get('red piece'), self.heldPiece)
            elif(piece == Board.BLACK_PIECE):
                self.game.screen.blit(self.game.resources.get('black piece'), self.heldPiece)
        
        if(self.gameOver):
            self.gameOverMessageBox.draw(self.game.screen)
        pygame.display.flip()

    def handleEvent(self, event):
        if(event.type==pygame.MOUSEBUTTONDOWN):
            pos = event.pos
            if(self.turn == self.humanTurn):
                column = int((pos[0]-self.board.x)/self.board.pieceSize)
                if(column>=0 and column<7 and (not self.gameOver)):
                    if(self.board.canInsertIntoColumn(column)):
                        
                        self.board.insertIntoColumn(column, self.humanPiece)
                        if(self.board.checkWin(self.humanPiece)):
                            self.gameOver = True
                            self.gameOverMessageBox.text = "You win"
                        elif(self.board.checkDraw()):
                            self.gameOver = True
                            self.gameOverMessageBox.text = "Draw"
                        
                        if(not self.gameOver):
                            self.turn = not self.turn

            self.gameOverMessageBox.checkClick(pos, event.button)
