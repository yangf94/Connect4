import pygame
from gui import Button, MessageBox
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
    def checkInputs(self):
        pass

