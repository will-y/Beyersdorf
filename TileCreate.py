import pygame as pg, time, math, Health

class GenerateTile:
    """Creates tile that holds what type of tile it is(ie forest, mountain, hill, plains, water) and the resources that exist on that tile(wood, stone, ore)"""

    def __init__(self, tileType):
        self.tileType = tileType
        self.wood = 0
        self.stone = 0
        self.ore = 0
        
    def generate_tile(self, x, y, tilesize, tilecolor, screen):
        self.tile = pg.Rect((x*tilesize, y*tilesize),(tilesize, tilesize))
        pg.draw.rect(screen, tilecolor, (x*tilesize, y*tilesize,tilesize, tilesize))
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)

    def generateResources(self, tileType):
        if self.tileType == "Forest" or self.tileType == "forest":
            self.wood = random.randint(750, 1250)
            self.stone = random.randint(50, 150)
            self.ore = random.randint(0, 10)
        if self.tileType == "Mountain" or self.tileType == "mountain":
            self.wood = random.randint(75, 125)
            self.stone = random.randint(2000, 4000)
            self.ore = random.randint(250, 450)
        if self.tileType == "Hill" or self.tileType == "hill":
            self.wood = random.randint(300, 500)
            self.stone = random.randint(750, 1500)
            self.ore = random.randint(75, 150)
        if self.tileType == "Plains" or self.tileType == "plains":
            self.wood = random.randint(200,400)
            self.stone = random.randint(25, 75)
            self.ore = 0
        if self.tileType == "Water" or self.tileType == "water":
            self.wood = 0
            self.stone = 0
            self.ore = 0

    def changeResourceAmount(self,type,amount):
        if type == "wood":
            self.wood += amount
        elif type == "stone":
            self.stone += amount
        elif type == "ore":
            self.ore += amount