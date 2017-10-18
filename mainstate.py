import pygame
from gamestate import GameState
from gui import Button
from oneplayerstate import OnePlayerState
from twoplayerstate import TwoPlayerState
from selectdifficultystate import SelectDifficultyState

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
        #self.game.state_stack.append(OnePlayerState(self.game))
        self.game.state_stack.append(SelectDifficultyState(self.game))

    def changeToTwoPlayerState(self):
        self.game.state_stack.append(TwoPlayerState(self.game))
