import pygame
from gamestate import MainMenuState

pygame.init()

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.state_stack = []
        self.state_stack.append(MainMenuState(self))

    def run(self):
        while(self.running):
            self.handleEvents()

            self.render()

            self.clock.tick()

        pygame.quit()

    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                self.running = False
            self.state_stack[-1].handleEvent(event)
    def render(self):
        self.state_stack[-1].render()
        
    def update(self):
        self.state_stack[-1].update()

    
