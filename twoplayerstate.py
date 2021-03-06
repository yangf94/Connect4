import pygame
from gui import MessageBox
from playablestate import PlayableState
from board import Board

class TwoPlayerState(PlayableState):
    def __init__(self, game):
        super().__init__(game)
        
    def render(self):
        self.game.screen.fill((170,170,170))
        
        self.board.draw(self.game.screen, self.game.resources)
        if(self.heldPiece!=None):
            if(self.turn == TwoPlayerState.PLAYER1_TURN):
                piece = self.player1Piece
            elif(self.turn == TwoPlayerState.PLAYER2_TURN):
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
            column = int((pos[0]-self.board.x)/self.board.pieceSize)
            if(column>=0 and column<7 and (not self.gameOver)):
                if(self.board.canInsertIntoColumn(column)):
                    if(self.turn == TwoPlayerState.PLAYER1_TURN):
                        self.board.insertIntoColumn(column, self.player1Piece)
                        if(self.board.checkWin(self.player1Piece)):
                            self.gameOver = True
                            self.gameOverMessageBox.text = "Player 1 wins"
                        elif(self.board.checkDraw()):
                                self.gameOver = True
                                self.gameOverMessageBox.text = "Draw"
                    elif(self.turn == TwoPlayerState.PLAYER2_TURN):
                        self.board.insertIntoColumn(column, self.player2Piece)
                        if(self.board.checkWin(self.player2Piece)):
                            self.gameOver = True
                            self.gameOverMessageBox.text = "Player 2 wins"
                        elif(self.board.checkDraw()):
                                self.gameOver = True
                                self.gameOverMessageBox.text = "Draw"
                    if(not self.gameOver):
                        self.turn = not self.turn

            self.gameOverMessageBox.checkClick(pos, event.button)
    
