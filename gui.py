import pygame

class Button:
    def __init__(self, text, rect, color, action=None):
        self.text = text
        self.rect = rect
        self.color = color
        self.action = action
        self.font = pygame.font.SysFont('Calibri', 25, True, False)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text = self.font.render(self.text, True, (0,0,0))
        size = self.font.size(self.text)
        x = self.rect[0]+(self.rect[2]-size[0])/2
        y = self.rect[1]+(self.rect[3]-size[1])/2

        screen.blit(text,[x,y])

    def checkClick(self, pos, button):
        if(pos[0]>self.rect[0] and pos[0]<self.rect[0]+self.rect[2]):
            if(pos[1]>self.rect[1] and pos[1]<self.rect[1]+self.rect[3]):
                if(button==1 and self.action!=None):
                    self.action()
                elif(button==1 and self.action==None):
                    print("Click")
