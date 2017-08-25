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

class MainMenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.buttons = []
        x = (game.width-150)/2
        self.buttons.append(Button("1-Player",(x,100,150,40), (220,220,0),self.changeOnePlayerState))
    def render(self):
        self.game.screen.fill((170,170,170))
        for button in self.buttons:
            button.draw(self.game.screen)
        pygame.display.flip()
    def handleEvent(self, event):
        if(event.type==pygame.MOUSEBUTTONDOWN):
            for button in self.buttons:
                button.checkClick(event.pos, event.button)
    def changeOnePlayerState(self):
        self.game.state_stack.append(OnePlayerState(self.game))

class OnePlayerState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.board = Board(self.game.width, self.game.height)
    
    def render(self):
        self.game.screen.fill((170,170,170))
        self.board.draw(self.game.screen, self.game.resources)
        pygame.display.flip()
    
    
