import math
import pygame as pg
import Terrain

"""Class that deals with health of buildings"""
class Health():
    def __init__(self, position, tileSize, screen):
        self.position = position
        self.screen = screen
        self.tileSize = tileSize

    """Draws the health onto a tile givin percentage of health"""
    def drawHealth(self, maxHealth, currentHealth):
        percentageHealth = currentHealth/maxHealth
        if not currentHealth == 0:
            if(percentageHealth <= 1/3):
                pg.draw.rect(self.screen, pg.Color("red"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70 * currentHealth/maxHealth, self.tileSize * .15))
            elif(percentageHealth <= 2/3):
                pg.draw.rect(self.screen, pg.Color("yellow"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70 * currentHealth/maxHealth, self.tileSize * .15))
            elif(percentageHealth <= 1):
                pg.draw.rect(self.screen, pg.Color("green"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70 * currentHealth/maxHealth, self.tileSize * .15))
            pg.draw.rect(self.screen, pg.Color("black"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70, self.tileSize * .15), 2)
