import math
import pygame as pg
import Terrain

"""Class that deals with health of buildings"""
class Health():
    def __init__(self, health, position, tileSize):
        self.health = health
        self.position = position

    """Draws the health onto a tile givin percentage of health"""
    def drawHealth(self, percentOfTotalHealth):
        pg.draw.rect(self.screen, pg.Color("black"), (position.x + 15, position.y + 75, 70, 15), 2)
        pg.draw.rect(self.screen, pg.Color("green"), (position.x + 15, position.y + 75, 70, 15))