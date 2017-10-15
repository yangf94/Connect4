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

class MessageBox:
    def __init__(self, text, x=-1, y=-1, action=None):
        self.text = text
        self.rect = [x, y, 200, 100]
        self.color = (200,200,0)
        self.action = action
        self.font = pygame.font.SysFont('Calibri', 25, True, False)

        self.button = Button("Ok", [x+25, y+40, 150, 40], color=(200,200,200), action=action)

    def draw(self, screen):
        if(self.rect[0]==-1 or self.rect[1]==-1):
            self.rect[0] = screen.get_width()//2-100
            self.rect[1] = screen.get_height()//2-50
            self.button.rect[0] = screen.get_width()//2-75
            self.button.rect[1] = self.rect[1] + 40
        pygame.draw.rect(screen, self.color, self.rect)
        text = self.font.render(self.text, True, (0,0,0))
        size = self.font.size(self.text)
        x = self.rect[0]+(self.rect[2]-size[0])/2
        y = self.rect[1]+5

        screen.blit(text,[x,y])

        self.button.draw(screen)
    def checkClick(self, pos, button):
        self.button.checkClick(pos, button)
