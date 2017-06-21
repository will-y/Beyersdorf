import pygame as pg
import math
import time
import Terrain
import Health

class Building:

    def __init__(self, type):
        building_type = type

    def createBuilding(self, x, y, tilesize, screen):
        self.building = pg.Rect(x, y, tilesize, tilesize)
        pg.draw.rect(screen, pg.Color(244, 101, 66), xloc, yloc, 100, 100)
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)