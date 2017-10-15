import pygame
from gamestate import MainMenuState
from resourcemanager import ResourceManager, IMAGE_TYPE
import tkinter as tk

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

        self.resources = ResourceManager()
        self.resources.loadResource("board", "assets/board.png", IMAGE_TYPE)
        self.resources.loadResource("red piece", "assets/red_piece.png", IMAGE_TYPE)
        self.resources.loadResource("black piece", "assets/black_piece.png", IMAGE_TYPE)

        self.tkroot = tk.Tk()
        self.tkroot.wm_withdraw()
    def run(self):
        while(self.running):
            self.handleEvents()
            self.update()
            self.render()

            self.clock.tick()

        pygame.quit()

    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                self.running = False
            self.state_stack[-1].handleEvent(event)
        self.state_stack[-1].checkInputs()
        
    def render(self):
        self.state_stack[-1].render()
        
    def update(self):
        self.state_stack[-1].update()

    
