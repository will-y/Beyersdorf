import pygame as pg
import time
import math
import random

"""Creates tile"""
class GenerateTile:

    def __init__(self, tileType):
        self.tileType = tileType
        self.tileResourceWood = 0
        self.tileResourceStone = 0
        self.tileResourceOre = 0

    def generate_tile(self, x, y, tilesize):
        tile = pg.Rect((x*tilesize, y*tilesize),(tilesize, tilesize))

    def generate_Resources(self,tileType):
        if self.tileType == "Forest" or self.tileType == "forest":
            self.tileResourceWood = 1000
            self.tileResourceStone = 100
            self.tileResourceOre = 0
        if self.tileType == "Mountain" or self.tileType == "mountain":
            self.tileResourceWood = 100
            self.tileResourceStone = 2000
            self.tileResourceOre = 300
        if self.tileType == "Hill" or self.tileType == "hill":
            self.tileResourceWood = 300
            self.tileResourceStone = 700
            self.tileResourceOre = 100
        if self.tileType == "Plains" or self.tileType == "plains":
            self.tileResourceWood = 300
            self.tileResourceStone = 50
            self.tileResourceOre = 0
        if self.tileType == "Water" or self.tileType == "water":
            self.tileResourceWood = 0
            self.tileResourceStone = 0
            self.tileResourceOre = 0