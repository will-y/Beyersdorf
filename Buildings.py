import pygame as pg
import math
import time
import Terrain
import Health
import TileCreate
import TurnManager

class Building:

    def __init__(self, buildingType, x, y, tilesize, screen, player):
        self.buildingType = buildingType
        self.productionRate = None
        self.populationCost = None
        self.populationAdd = None
        self.woodCost = None
        self.stoneCost = None
        self.oreCost = None
        self.x = x
        self.y = y
        self.screen = screen
        self.tilesize = tilesize
        self.image = None
        self.createBuilding(x, y, tilesize, screen, player)
        self.playerOwned = None

    def drawBuilding(self, player):
        #pg.draw.rect(self.screen, pg.Color(244, 101, 66), (self.x, self.y, self.tilesize, self.tilesize))
        self.screen.blit(self.image, (self.x + self.tilesize/10, self.y + self.tilesize/10))

        if player == 1:
            pg.draw.rect(self.screen, pg.Color(255, 0, 0), (self.x, self.y, self.tilesize, self.tilesize), 1)

        if player == 2:
            pg.draw.rect(self.screen, pg.Color(0, 0, 255), (self.x, self.y, self.tilesize, self.tilesize), 1)

    def __str__(self):
        return str(self.buildingType)

    def createBuilding(self, x, y, tilesize, screen, player):
        self.building = pg.Rect(x, y, tilesize, tilesize)
        self.playerOwned = player
        #pg.draw.rect(screen, pg.Color(244, 101, 66), (x, y, tilesize, tilesize))
        healthBar = Health.Health((x*tilesize, y*tilesize), 100, screen)
        healthBar.drawHealth(100, 100)
       
            #Farm
        if self.buildingType == 0:
            self.productionRate = 5
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 100
            self.stoneCost = 50
            self.oreCost = 2
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Ranch
        if self.buildingType == 1:
            self.productionRate = 10
            self.populationCost = 2
            self.populationAdd = 0
            self.woodCost = 300
            self.stoneCost = 200
            self.oreCost = 10
            self.image = pg.image.load("Images/ranch.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
       
            #Fishhut
        if self.buildingType == 2:
            self.productionRate = 8
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 200
            self.stoneCost = 100
            self.oreCost = 5
            self.image = pg.image.load("Images/fishingHut.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #LumberMill
        if self.buildingType == 3:
            self.productionRate = 50
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 100
            self.stoneCost = 50
            self.oreCost = 2
            self.image = pg.image.load("Images/lumberMill.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Quarry
        if self.buildingType == 4:
            self.productionRate = 50
            self.populationCost = 2
            self.populationAdd = 0
            self.woodCost = 100
            self.stoneCost = 25
            self.oreCost = 5
            self.image = pg.image.load("Images/quarry.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Mine
        if self.buildingType == 5:
            self.productionRate = 10
            self.populationCost = 5
            self.populationAdd = 0
            self.woodCost = 300
            self.stoneCost = 200
            self.oreCost = 5
            self.image = pg.image.load("Images/mine.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #House
        if self.buildingType == 6:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 5
            self.woodCost = 100
            self.stoneCost = 50
            self.oreCost = 0
            self.image = pg.image.load("Images/house.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Town
        if self.buildingType == 7:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 250
            self.stoneCost = 100
            self.oreCost = 5
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #City
        if self.buildingType == 8:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 20
            self.woodCost = 500
            self.stoneCost = 300
            self.oreCost = 50
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Bridge
        if self.buildingType == 9:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 0
            self.woodCost = 200
            self.stoneCost = 100
            self.oreCost = 0
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Castle
        if self.buildingType == 10:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 1000    
            self.stoneCost = 1000
            self.oreCost = 200
            self.image = pg.image.load("Images/castle1.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #Outpost
        if self.buildingType == 11:
            self.productionRate = 0
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 300 
            self.stoneCost = 100
            self.oreCost = 10
            self.image = pg.image.load("Images/outpost.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))

            #CannonTower
        if self.buildingType == 12:
            self.productionRate = 0
            self.populationCost = 2
            self.populationAdd = 10
            self.woodCost = 700
            self.stoneCost = 800
            self.oreCost = 80
            # self.image = pg.image.load("Images/cannonTower.png")
            self.image = pg.image.load("Images/Dr._Rupakheti.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))