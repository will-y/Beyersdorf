import pygame as pg
import math
import time
import Terrain
import Health

class Building:

    def __init__(self, buildingType, x, y, tilesize, screen):
        self.buildingType = buildingType
        self.productionRate = None
        self.populationCost = None
        self.populationAdd = None
        self.woodCost = None
        self.stoneCost = None
        self.oreCost = None
        self.createBuilding(x, y, tilesize, screen)

    def createBuilding(self, x, y, tilesize, screen):
        self.building = pg.Rect(x, y, tilesize, tilesize)
        pg.draw.rect(screen, pg.Color(244, 101, 66), (x, y, 100, 100))
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

            #Ranch
        if self.buildingType == 1:
            self.productionRate = 10
            self.populationCost = 2
            self.populationAdd = 0
            self.woodCost = 300
            self.stoneCost = 200
            self.oreCost = 10
       
            #Fishhut
        if self.buildingType == 2:
            self.productionRate = 8
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 200
            self.stoneCost = 100
            self.oreCost = 5

            #LumberMill
        if self.buildingType == 3:
            self.productionRate = 50
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 100
            self.stoneCost = 50
            self.oreCost = 2

            #Quarry
        if self.buildingType == 4:
            self.productionRate = 50
            self.populationCost = 2
            self.populationAdd = 0
            self.woodCost = 100
            self.stoneCost = 25
            self.oreCost = 5

            #Mine
        if self.buildingType == 5:
            self.productionRate = 10
            self.populationCost = 5
            self.populationAdd = 0
            self.woodCost = 300
            self.stoneCost = 200
            self.oreCost = 5

            #HouseCastle
        if self.buildingType == 6:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 5
            self.woodCost = 100
            self.stoneCost = 50
            self.oreCost = 0

            #Town
        if self.buildingType == 7:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 250
            self.stoneCost = 100
            self.oreCost = 5

            #City
        if self.buildingType == 8:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 20
            self.woodCost = 500
            self.stoneCost = 300
            self.oreCost = 50

            #Bridge
        if self.buildingType == 9:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 0
            self.woodCost = 200
            self.stoneCost = 100
            self.oreCost = 0

            #Castle
        if self.buildingType == 10:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 1000    
            self.stoneCost = 1000
            self.oreCost = 200

            #Outpost
        if self.buildingType == 11:
            self.productionRate = 0
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 300 
            self.stoneCost = 100
            self.oreCost = 10

            #CannonTower
        if self.buildingType == 12:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 1000    
            self.stoneCost = 1000
            self.oreCost = 200