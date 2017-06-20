import pygame as pg
import time
import math

"""Creates tile"""
class GenerateTile:

    def __init__(self, tileType):
        self.tileType = tileType
        self.tileResourceWood = 
        self.tileResourceStone = 
        self.tileResourceOre = 

    def generate_tile(self, x, y, tilesize):
        tile = pg.rect((x*tilesize, y*tilesize),(tilesize, tilesize))
