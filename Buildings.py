import pygame as pg
import math
import time
import Terrain
import Health

class Building:

    def __init__(self, type, x, y, tilesize, screen):
        building_type = type
        self.createBuilding(x, y, tilesize, screen)

    def createBuilding(self, x, y, tilesize, screen):
        self.building = pg.Rect(x, y, tilesize, tilesize)
        pg.draw.rect(screen, pg.Color(244, 101, 66), (x, y, 100, 100))
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)

