import pygame

pygame.init()

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while(self.running):
            for event in pygame.event.get():
                self.handleEvent(event)

            self.render()

            self.clock.tick()

        pygame.quit()

    def handleEvent(self, event):
        if(event.type==pygame.QUIT):
            self.running = False
        
    def render(self):
        self.screen.fill((0,230,210))
        pygame.display.flip()
