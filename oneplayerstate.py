import pygame
from gui import MessageBox
from gamestate import GameState
from board import Board

class OnePlayerState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.board = Board(self.game.width, self.game.height)
    
    def render(self):
        self.game.screen.fill((170,170,170))
        self.board.draw(self.game.screen, self.game.resources)
        pygame.display.flip()

