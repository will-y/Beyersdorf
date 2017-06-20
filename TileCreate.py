import pygame as pg
import time
import math

"""Creates tile"""
class GenerateTile:

    def __init__(self, tileType):
        self.tileType = tileType
        self.tileResourceWood = 0
        self.tileResourceStone = 0
        self.tileResourceOre = 0

    def generate_tile(self, x, y, tilesize):
        tile = pg.rect((x*tilesize, y*tilesize),(tilesize, tilesize))

    def generate_Resources(self,tileType):
        pass