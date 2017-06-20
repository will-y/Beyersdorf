import pygame as pg

class UserInterface():
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.SysFont("monospace", 50)
        self.resourceText = self.font.render("Resources", True, pg.Color('black'))
        

    def drawInterface(self):
        self.screen.blit(self.resourceText, (1125, 25))