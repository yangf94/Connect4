import pygame
from gui import MessageBox
from playablestate import PlayableState
from board import Board

class OnePlayerState(PlayableState):
    def __init__(self, game):
        super().__init__(game)
        self.board = Board(self.game.width, self.game.height)
    
    def render(self):
        self.game.screen.fill((170,170,170))
        self.board.draw(self.game.screen, self.game.resources)
        pygame.display.flip()

