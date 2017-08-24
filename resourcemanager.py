import pygame

IMAGE_TYPE = 0

class ResourceManager:
    def __init__(self):
        self.resources = {}

    def loadResource(self, name, filename, rtype):
        if(rtype == IMAGE_TYPE):
            self.resources[name] = 
