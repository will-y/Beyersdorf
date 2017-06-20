import pygame as pg
import time
import math
import Health

"""Creates tile"""
class GenerateTile:
    def __init__(self, tileType):
        self.tileType = tileType
        self.tileResourceWood = 0
        self.tileResourceStone = 0
        self.tileResourceOre = 0
        

    def generate_tile(self, x, y, tilesize, screen):
        tile = pg.Rect((x*tilesize, y*tilesize),(tilesize, tilesize))
        pg.draw.rect(screen, pg.Color("black"), (x*tilesize, y*tilesize,tilesize, tilesize), 1)
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)

    def generate_Resources(self,tileType):
        pass