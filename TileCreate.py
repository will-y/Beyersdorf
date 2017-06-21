import pygame as pg, time, math, random, Health

# Creates tile that holds what type of tile it is(ie forest, mountain, hill, 
# plains, water) and the resources that exist on that tile(wood, stone, ore)
class GenerateTile:

    def __init__(self, tileType):
        self.tileType = tileType
        self.wood = 0
        self.stone = 0
        self.ore = 0
        
<<<<<<< HEAD
    def generate_tile(self, x, y, tilesize, screen):
        tileTypes = ["Forest","Mountain","Hill","Plains","Water"]
=======

    def generateTile(self, x, y, tilesize, screen):
>>>>>>> 5e4cae07d629794df5f650a2da117e38fa6bbef1
        self.tile = pg.Rect((x*tilesize, y*tilesize),(tilesize, tilesize))
        pg.draw.rect(screen, pg.Color("black"), (x*tilesize, y*tilesize,tilesize, tilesize))
        pg.rect
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)

    def generateResources(self, tileType):
        if self.tileType == "Forest" or self.tileType == "forest":
            self.wood = 1000
            self.stone = 100
            self.ore = 0
        if self.tileType == "Mountain" or self.tileType == "mountain":
            self.wood = 100
            self.stone = 2000
            self.ore = 300
        if self.tileType == "Hill" or self.tileType == "hill":
            self.wood = 300
            self.stone = 700
            self.ore = 100
        if self.tileType == "Plains" or self.tileType == "plains":
            self.wood = 300
            self.stone = 50
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