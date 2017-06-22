import pygame as pg, time, math, Health, random

class GenerateTile:
    """Creates tile that holds what type of tile it is(ie forest, mountain, hill, plains, water) and the resources that exist on that tile(wood, stone, ore)"""

    def __init__(self, tileType):
        self.tileType = tileType
        self.wood = 0
        self.stone = 0
        self.ore = 0
        self.builtOn = False
    
    def __str__(self):
        mystr = str.format("{}, {}, {}, {}", self.tileType, self.wood, self.stone, self.ore)
        return mystr
        
    def generate_tile(self, x, y, tilesize, tilecolor, screen):
        self.tile = pg.Rect((x*tilesize, y*tilesize),(tilesize, tilesize))
        self.generateResources(self.tileType)
        pg.draw.rect(screen, tilecolor, (x*tilesize, y*tilesize,tilesize, tilesize))
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)

    def generateResources(self, tileType):
            #Forest
        if self.tileType == 0:
            self.wood = random.randint(750, 1250)
            self.stone = random.randint(50, 150)
            self.ore = random.randint(0, 10)
            #Mountain
        if self.tileType == 1:
            self.wood = random.randint(75, 125)
            self.stone = random.randint(2000, 4000)
            self.ore = random.randint(250, 450)
            #Hill
        if self.tileType == 2:
            self.wood = random.randint(300, 500)
            self.stone = random.randint(750, 1500)
            self.ore = random.randint(75, 150)
            #Plains
        if self.tileType == 3:
            self.wood = random.randint(200,400)
            self.stone = random.randint(25, 75)
            self.ore = 0
            #Water
        if self.tileType == 4:
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