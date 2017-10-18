import pygame
from gamestate import GameState
from gui import Button
from oneplayerstate import OnePlayerState

class SelectDifficultyState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.buttons = []
        x = (game.width)//2-250
        
        for i in range(1,3):
            self.buttons.append(Button(str(i),(x+25+((i-1)%5)*100,160+((i-1)//5)*100,50,50), (220,220,0),action=self.selectAIDifficulty, args=(i,)))

    def render(self):
        self.game.screen.fill((170,170,170))
        for button in self.buttons:
            button.draw(self.game.screen)
        pygame.display.flip()
    def handleEvent(self, event):
        if(event.type==pygame.MOUSEBUTTONDOWN):
            for button in self.buttons:
                button.checkClick(event.pos, event.button)


    def selectAIDifficulty(self, i):
        if(i==1 or i==2):
            self.game.state_stack.pop()
            self.game.state_stack.append(OnePlayerState(self.game,i))
        else:
            print(i)
