import pygame as pg
import math
import time
import Terrain
import Health
import TileCreate
import TurnManager
import Player

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
        self.maxHealth = None
        self.currentHealth = self.maxHealth
        self.image = None
        self.createBuilding(x, y, tilesize, screen, player)
        self.playerOwned = None
        self.destroyed = False

    def drawBuilding(self, player):
        #pg.draw.rect(self.screen, pg.Color(244, 101, 66), (self.x, self.y, self.tilesize, self.tilesize))
        if self.buildingType == 9:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x + self.tilesize/10, self.y + self.tilesize/10))

        if player == 1:
            pg.draw.rect(self.screen, pg.Color(255, 0, 0), (self.x, self.y, self.tilesize, self.tilesize), 1)

        if player == 2:
            pg.draw.rect(self.screen, pg.Color(0, 0, 255), (self.x, self.y, self.tilesize, self.tilesize), 1)

    def __str__(self):
        return str(self.buildingType)
    
    def takeDamage(self, amount, terrain, receivingPlayer, attackedBuilding):
        self.currentHealth = self.currentHealth - amount
        if self.currentHealth <= 0:
            print("Building Destroyed!")
            #redraws tile after finding tileimage then draws rubble.png
            self.destroyed = True
            tileType = terrain.board[math.floor(self.x/100)][math.floor(self.y/100)].tileType
            if tileType == 0:
                tileimage = pg.image.load("Images/forestTile.png")
            elif tileType == 1:
                tileimage = pg.image.load("Images/mountainTile.png")
            elif tileType == 2:
                tileimage = pg.image.load("Images/hillTile.png")
            elif tileType == 3:
                tileimage = pg.image.load("Images/plainTile.png")
            elif tileType >= 4:
                tileimage = pg.image.load("Images/waterTile.png")
            self.redraw = pg.transform.scale(tileimage, (int(self.tilesize), int(self.tilesize)))
            self.screen.blit(self.redraw, (math.floor(self.x/100) * self.tilesize, math.floor(self.y/100) * self.tilesize))
            self.image = pg.image.load("Images/rubble.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (2/5))))
            self.screen.blit(self.image, (self.x + self.tilesize/10, self.y + self.tilesize/2))
            terrain.board[math.floor(self.x/100)][math.floor(self.y/100)].builtOn = False
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 0
            self.woodCost = 0
            self.stoneCost = 0
            self.oreCost = 0
            self.canFire = False
            for i in range(len(receivingPlayer.buildings)):
                if attackedBuilding == receivingPlayer.buildings[i]:
                    print(i)
                    receivingPlayer.buildings.pop(i)
                    break

        else:
            health = Health.Health((self.x, self.y), self.tilesize, self.screen)
            health.drawHealth(self.maxHealth, self.currentHealth)
       
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
            self.oreCost = 1
            self.maxHealth = 100
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #Ranch
        if self.buildingType == 1:
            self.productionRate = 10
            self.populationCost = 2
            self.populationAdd = 0
            self.woodCost = 200
            self.stoneCost = 100
            self.oreCost = 4
            self.maxHealth = 150
            self.image = pg.image.load("Images/ranch.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False
       
            #Fishhut
        if self.buildingType == 2:
            self.productionRate = 8
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 125
            self.stoneCost = 75
            self.oreCost = 2
            self.maxHealth = 100
            self.image = pg.image.load("Images/fishingHut.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #LumberMill
        if self.buildingType == 3:
            self.productionRate = 50
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 50
            self.stoneCost = 50
            self.oreCost = 2
            self.maxHealth = 150
            self.image = pg.image.load("Images/lumberMill.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #Quarry
        if self.buildingType == 4:
            self.productionRate = 50
            self.populationCost = 2
            self.populationAdd = 0
            self.woodCost = 100
            self.stoneCost = 0
            self.oreCost = 5
            self.maxHealth = 200
            self.image = pg.image.load("Images/quarry.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #Mine
        if self.buildingType == 5:
            self.productionRate = 10
            self.populationCost = 5
            self.populationAdd = 0
            self.woodCost = 200
            self.stoneCost = 150
            self.oreCost = 0
            self.maxHealth = 200
            self.image = pg.image.load("Images/mine.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #House
        if self.buildingType == 6:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 5
            self.woodCost = 100
            self.stoneCost = 50
            self.oreCost = 0
            self.maxHealth = 100
            self.image = pg.image.load("Images/house.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #Town
        if self.buildingType == 7:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 250
            self.stoneCost = 100
            self.oreCost = 5
            self.maxHealth = 200
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #City
        if self.buildingType == 8:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 20
            self.woodCost = 500
            self.stoneCost = 300
            self.oreCost = 50
            self.maxHealth = 300
            self.image = pg.image.load("Images/farm.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = False

            #Bridge
        if self.buildingType == 9:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 0
            self.woodCost = 150
            self.stoneCost = 50
            self.oreCost = 0
            self.maxHealth = 200
            self.image = pg.image.load("Images/bridge.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize), int(self.tilesize)))
            self.canFire = False

            #Castle
        if self.buildingType == 10:
            self.productionRate = 0
            self.populationCost = 0
            self.populationAdd = 10
            self.woodCost = 1000  
            self.stoneCost = 800
            self.oreCost = 100
            self.maxHealth = 500
            self.image = pg.image.load("Images/castle1.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = True
            self.damage = 30
            self.range = 4

            #Outpost
        if self.buildingType == 11:
            self.productionRate = 0
            self.populationCost = 1
            self.populationAdd = 0
            self.woodCost = 200 
            self.stoneCost = 100
            self.oreCost = 15
            self.maxHealth = 200
            self.image = pg.image.load("Images/outpost.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = True
            self.damage = 15
            self.range = 4
            print(self.canFire)

            #CannonTower
        if self.buildingType == 12:
            self.productionRate = 0
            self.populationCost = 3 
            self.populationAdd = 0
            self.woodCost = 250
            self.stoneCost = 400
            self.oreCost = 30
            self.maxHealth = 300
            # self.image = pg.image.load("Images/cannonTower.png")
            self.image = pg.image.load("Images/cannonTower.png")
            self.image = pg.transform.scale(self.image, (int(self.tilesize * (4/5)), int(self.tilesize * (4/5))))
            self.canFire = True
            self.damage = 40
            self.range = 3

        self.currentHealth = self.maxHealth