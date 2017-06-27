import pygame as pg, time, math, Health, random

class GenerateTile:
    """Creates tile that holds what type of tile it is(ie forest, mountain, hill, plains, water) and the resources that exist on that tile(wood, stone, ore)"""

    def __init__(self, tileType, x, y, screen):
        self.tileType = tileType
        self.wood = 0
        self.stone = 0
        self.ore = 0
        self.builtOn = False
        self.x = x
        self.y = y
        self.screen = screen
    
    def __str__(self):
        """Returns the values saved in the tile"""
        mystr = str.format("{}, {}, {}, {}", self.tileType, self.wood, self.stone, self.ore)
        return mystr
        
    def generate_tile(self, tilesize, tileimage):
        """Creates a new tile"""
        self.image = tileimage
        self.screen.blit(self.image, (self.x * tilesize, self.y * tilesize))
        self.generateResources(self.tileType)

    def generateResources(self, tileType):
        """Generates resources within the tile object"""
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
        """Changes the amount of a resource in a tile"""
        if type == "wood":
            self.wood += amount
        elif type == "stone":
            self.stone += amount
        elif type == "ore":
            self.ore += amount