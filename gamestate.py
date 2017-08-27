import pygame
from gui import Button
from board import Board

class GameState:
    def __init__(self, game):
        self.game = game
    def update(self):
        pass
    def render(self):
        pass
    def handleEvent(self, event):
        pass
    def checkInputs(self):
        pass
class MainMenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.buttons = []
        x = (game.width-150)/2
        self.buttons.append(Button("1-Player",(x,100,150,40), (220,220,0),self.changeToOnePlayerState))
        self.buttons.append(Button("2-Player",(x,160,150,40), (220,220,0),self.changeToTwoPlayerState))
    def render(self):
        self.game.screen.fill((170,170,170))
        for button in self.buttons:
            button.draw(self.game.screen)
        pygame.display.flip()
    def handleEvent(self, event):
        if(event.type==pygame.MOUSEBUTTONDOWN):
            for button in self.buttons:
                button.checkClick(event.pos, event.button)
    def changeToOnePlayerState(self):
        self.game.state_stack.append(OnePlayerState(self.game))

    def changeToTwoPlayerState(self):
        self.game.state_stack.append(TwoPlayerState(self.game))

class OnePlayerState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.board = Board(self.game.width, self.game.height)
    
    def render(self):
        self.game.screen.fill((170,170,170))
        self.board.draw(self.game.screen, self.game.resources)
        pygame.display.flip()


class TwoPlayerState(GameState):
    
    PLAYER1_TURN = False
    PLAYER2_TURN = True
    def __init__(self, game):
        super().__init__(game)
        self.board = Board(self.game.width, self.game.height)

        self.player1Piece = Board.RED_PIECE
        self.player2Piece = Board.BLACK_PIECE

        self.turn = False

        self.heldPiece = None
    
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


        pygame.display.flip()
    
    
    def checkInputs(self):
        pos = pygame.mouse.get_pos()
        column = int((pos[0]-self.board.x)/self.board.pieceSize)
        if(column>=0 and column<7):
            self.heldPiece = ((self.board.x+column*self.board.pieceSize), (self.board.y-self.board.pieceSize))
        else:
            self.heldPiece = None
