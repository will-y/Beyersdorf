import pygame as pg, math
from source import Terrain

class Health():
    """Class that deals with health of buildings"""
    
    def __init__(self, position, tileSize, screen):
        self.position = position
        self.screen = screen
        self.tileSize = tileSize

    def drawHealth(self, maxHealth, currentHealth):
        """Draws the health onto a tile givin percentage of health"""
        percentageHealth = currentHealth/maxHealth
        if not currentHealth == 0 and not percentageHealth == 1:
            if(percentageHealth <= 1/3):
                pg.draw.rect(self.screen, pg.Color("snow 4"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70, self.tileSize * .15))
                pg.draw.rect(self.screen, pg.Color("red"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70 * percentageHealth, self.tileSize * .15))
            elif(percentageHealth <= 2/3):
                pg.draw.rect(self.screen, pg.Color("snow 4"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70, self.tileSize * .15))
                pg.draw.rect(self.screen, pg.Color("yellow"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70 * percentageHealth, self.tileSize * .15))
            elif(percentageHealth < 1):
                pg.draw.rect(self.screen, pg.Color("snow 4"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70, self.tileSize * .15))
                pg.draw.rect(self.screen, pg.Color("green"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70 * percentageHealth, self.tileSize * .15))
            pg.draw.rect(self.screen, pg.Color("black"), (self.position[0] + self.tileSize * .15, self.position[1] + self.tileSize * .75, self.tileSize * .70, self.tileSize * .15), 2)
