import pygame as pg, sys, math
from source import Player, InspectorGadget, Terrain

class UserInterface():
    def __init__(self, screen):
        #Init stuff
        self.screen = screen
        self.font = pg.font.SysFont("monospace", 50)
        self.resourceCountFont = pg.font.SysFont("monospace", 30)
        self.tab1Font = pg.font.SysFont("monospace", 25)
        self.tab2Font = pg.font.SysFont("monospace", 15)
        self.buildingFont = pg.font.SysFont("monospace", 14)
        
        self.gameHeight = 1000
        self.gameWidth = 1000

        self.UIWidth = self.gameWidth/2
        self.UIHeight = self.gameHeight

        #Resources List
        self.resourceText = self.font.render("Resources", True, pg.Color('black'))
        self.woodCountText = self.resourceCountFont.render("Wood", True, pg.Color('black'))
        self.stoneCountText = self.resourceCountFont.render("Stone", True, pg.Color('black'))
        self.oreCountText = self.resourceCountFont.render("Ore", True, pg.Color('black'))
        self.foodCountText = self.resourceCountFont.render("Food", True, pg.Color('black'))
        self.popCountText = self.resourceCountFont.render("Population", True, pg.Color('black'))

        #Tab texts
        self.tab1BuildingText = self.tab1Font.render("Buildings", True, pg.Color('black'))
        self.tab1InspectorText = self.tab1Font.render("Inspector", True, pg.Color('black'))

        self.endTurnText = self.tab1Font.render("End Turn", True, pg.Color('black'))

        self.resourceTabText = self.tab2Font.render("Resource", True, pg.Color('black'))
        self.militaryTabText = self.tab2Font.render("Military", True, pg.Color('black'))
        self.infrastructureTabText = self.tab2Font.render("Other", True, pg.Color('black'))

        #Resource Images
        self.woodImage = pg.image.load("Images/log.png")
        self.woodImage = pg.transform.scale(self.woodImage, (math.floor(self.UIWidth/7), math.floor(self.UIHeight/22)))
        self.woodCostImage = pg.transform.scale(self.woodImage, (math.floor(self.UIWidth/14.3), math.floor(self.UIHeight/43.5)))

        self.stoneImage = pg.image.load("Images/stone.png")
        self.stoneImage = pg.transform.scale(self.stoneImage, (math.floor(self.UIWidth/7), math.floor(self.UIHeight/22)))
        self.stoneCostImage = pg.transform.scale(self.stoneImage, (math.floor(self.UIWidth/14.3), math.floor(self.UIHeight/43.5)))

        self.oreImage = pg.image.load("Images/ore.png")
        self.oreImage = pg.transform.scale(self.oreImage, (math.floor(self.UIWidth/7), math.floor(self.UIHeight/22)))
        self.oreCostImage = pg.transform.scale(self.oreImage, (math.floor(self.UIWidth/14.3), math.floor(self.UIHeight/43.5)))

        self.foodImage = pg.image.load("Images/food.png")
        self.foodImage = pg.transform.scale(self.foodImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIHeight/22)))

        self.populationImage = pg.image.load("Images/pop.png")
        self.populationImage = pg.transform.scale(self.populationImage, (math.floor(self.UIHeight/22), math.floor(self.UIHeight/22)))
        self.populationCostImage = pg.transform.scale(self.populationImage, (math.floor(self.UIHeight/43.5), math.floor(self.UIHeight/43.5)))

        #Building Images
        self.farmImage = pg.image.load("Images/farm.png")
        self.farmImage = pg.transform.scale(self.farmImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.ranchImage = pg.image.load("Images/ranch.png")
        self.ranchImage = pg.transform.scale(self.ranchImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.fishImage = pg.image.load("Images/fishingHut.png")
        self.fishImage = pg.transform.scale(self.fishImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.quarryImage = pg.image.load("Images/quarry.png")
        self.quarryImage = pg.transform.scale(self.quarryImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.lumberMillImage = pg.image.load("Images/lumberMill.png")
        self.lumberMillImage = pg.transform.scale(self.lumberMillImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.mineImage = pg.image.load("Images/mine.png")
        self.mineImage = pg.transform.scale(self.mineImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.castleImage = pg.image.load("Images/castle1.png")
        self.castleImage = pg.transform.scale(self.castleImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.outpostImage = pg.image.load("Images/outpost.png")
        self.outpostImage = pg.transform.scale(self.outpostImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.cannonImage = pg.image.load("Images/cannonTower.png")
        self.cannonImage = pg.transform.scale(self.cannonImage, (math.floor(500/16.7), math.floor(self.UIWidth / ((1/3) + 8))))

        self.houseImage = pg.image.load("Images/house.png")
        self.houseImage = pg.transform.scale(self.houseImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.townImage = pg.image.load("Images/town.png")
        self.townImage = pg.transform.scale(self.townImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.cityImage = pg.image.load("Images/city.png")
        self.cityImage = pg.transform.scale(self.cityImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        self.bridgeImage = pg.image.load("Images/bridge.png")
        self.bridgeImage = pg.transform.scale(self.bridgeImage, (math.floor(self.UIWidth / ((1/3) + 8)), math.floor(self.UIWidth / ((1/3) + 8))))

        #Resources Per Turn   [wood, stone, ore, food]
        self.resourcesPerTurn = [0,0,0,0]
        self.playerWoodPerTurn = " +0/Turn"
        self.playerStonePerTurn = " +0/Turn"
        self.playerOrePerTurn = " +0/Turn"
        self.playerFoodPerTurn = " +0/Turn"

        #Resource Amounts
        self.woodCount = self.resourceCountFont.render("1000" + " " + str(self.resourcesPerTurn[0]) + '/Turn', True, pg.Color('black'))
        self.stoneCount = self.resourceCountFont.render("500" + " " + str(self.resourcesPerTurn[1]) + '/Turn', True, pg.Color('black'))
        self.oreCount = self.resourceCountFont.render("75" + " " + str(self.resourcesPerTurn[2]) + '/Turn', True, pg.Color('black'))
        self.foodCount = self.resourceCountFont.render("20" + " " + str(self.resourcesPerTurn[3]) + '/Turn', True, pg.Color('black'))

        self.populationCount = self.resourceCountFont.render("10 / 10", True, pg.Color('black'))

        #Background rectangle dimensions
        self.rectXPos = 1000
        self.rectYPos = 0
        self.rectWidth = self.UIWidth
        self.rectHeight = self.UIHeight
        self.rectColor = pg.Color(183, 183, 183)

        self.inspector = False

        #First Tab Dimensions
        self.tabButtonHeight = math.floor(self.UIHeight/28.6)
        self.tabButtonWidth = math.floor(self.UIWidth/2.5)
        self.tabButtonXValue = self.gameWidth + math.floor(self.UIWidth/10)
        self.tabButtonYValue = 400
        self.tabButtonColor = pg.Color(145, 145, 145)
        self.tabButtonSelectedColor = pg.Color(99, 99, 99)

        #Second Tab Dimensions
        self.tabButton2Height = 25
        self.tabButton2Width = 100
        self.tabButton2XValue = self.tabButtonXValue + (self.tabButtonWidth * 2 - self.tabButton2Width * 3)/2
        self.tabButton2YValue = 450

        #CURRENT BUILDING TAB: RESOURCE = 0, MILITARY = 1, INFRASTRUCTURE = 2
        self.currentBuildingTab = 0

        #RESOURCE AMOUNTS TO DISPLAY
        self.wood = 1000
        self.stone = 1000
        self.food = 0
        self.ore = 100
        self.maxPopulation = 0
        self.currentPopulation = 0

        self.buildingRect1Width = self.tabButtonWidth * 2
        self.buildingRect1Height = 60

        #Variables for resources buildings in menus
        self.buildingWidth = 60
        self.buildingPadding = 20

        self.costPadding = 10

        #                     wood  stone  ore   pop
        #ID = 0
        self.farmCost =       "100    50    1     1"
        #ID = 1
        self.ranchCost =      "200    100   4     2"
        #ID = 2
        self.fishCost =       "125    75    2     1"
        #ID = 3
        self.lumberMillCost = "50     50    2     1"
        #ID = 4
        self.quarryCost =     "100    0     5     2"
        #ID = 5
        self.mineCost =       "200    150   0     5"
        #ID = 6
        self.houseCost =      "100    50    0     +5"
        #ID = 7
        self.townCost =       "250    100   5     +10"
        #ID = 8
        self.cityCost =       "500    300   50    +20"
        #ID = 9
        self.bridgeCost =     "150    50    0     0"
        #ID = 10
        self.castleCost =     "1000   800   100   +10"
        #ID = 11
        self.outpostCost =    "200    100   15    1"
        #ID = 12
        self.cannonCost =     "250    400   30    3"

        #INSPECTOR THINGS
        self.currentTile = "Forest"
        self.tileWoodAmount = "0"
        self.tileStoneAmount = "0"
        self.tileOreAmount = "0"
        self.prefBuildingName = "Lumber Mill"
        self.costModiferNumber = "1"
        self.currentBuildingName = "None"
        self.woodPerTurnInspector = ""
        self.stonePerTurnInspector = ""
        self.orePerTurnInspector = ""

        self.buildingID = 0

        self.currentTurn = "red"

    def drawInterface(self):
        '''Draws Everything in the Interface'''
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        pg.draw.rect(self.screen, pg.Color('black'), (self.rectXPos, self.rectYPos, self.rectWidth,self.rectHeight), 5)

        #Draw resource names
        self.screen.blit(self.resourceText, (1125, 25))
        self.screen.blit(self.woodCountText, (1050, 100))
        self.screen.blit(self.stoneCountText, (1050, 150))
        self.screen.blit(self.oreCountText, (1050, 200))
        self.screen.blit(self.foodCountText, (1050, 250))
        self.screen.blit(self.popCountText, (1050, 300))

        #Draw resource images
        self.screen.blit(self.woodImage, (1130, 95))
        self.screen.blit(self.stoneImage, (1135, 140))
        self.screen.blit(self.oreImage, (1110, 190))
        self.screen.blit(self.foodImage, (1130, 240))
        self.screen.blit(self.populationImage, (1235, 290))

        #Draw resource Amounts
        self.screen.blit(self.woodCount, (1210, 100))
        self.screen.blit(self.stoneCount, (1210, 150))
        self.screen.blit(self.oreCount, (1200, 200))
        self.screen.blit(self.foodCount, (1210, 250))
        self.screen.blit(self.populationCount, (1305, 300))

        #End turn button
        self.switchEndTurnButton(self.currentTurn)

        #Error box
        pg.draw.rect(self.screen, pg.Color('white'), (1230, 347, 220, 38))
        pg.draw.rect(self.screen, pg.Color('black'), (1230, 347, 220, 38), 3)

        if(not self.inspector):
            #BUILDING SELECTED
            #LEFT TAB: BUILDING
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButtonXValue, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))
            
            #RIGHT TAB: INSPECTOR
            pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButtonXValue + self.tabButtonWidth, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))            
            
            #DRAW BOTTOM TABS
            if(self.currentBuildingTab == 0):
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))

                self.drawResourceBuildings(self.buildingID)

            elif(self.currentBuildingTab == 1):
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))

                self.drawMilitaryBuildings(self.buildingID)

            elif(self.currentBuildingTab == 2):
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))

                self.drawInfrastructureBuildings(self.buildingID)
            #DRAW DIVIDERS
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, 2, self.tabButton2Height))
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, 2, self.tabButton2Height))

            #BOTTOM TAB NAMES
            self.screen.blit(self.resourceTabText, (self.tabButton2XValue + 14, self.tabButton2YValue + 4))
            self.screen.blit(self.militaryTabText, (self.tabButton2XValue + 14 + self.tabButton2Width, self.tabButton2YValue + 4))
            self.screen.blit(self.infrastructureTabText, (self.tabButton2XValue + 14 + self.tabButton2Width * 2, self.tabButton2YValue + 4))

            #DRAW RESOURCE COST ICONS
            self.screen.blit(self.woodCostImage, (1225, 485))
            self.screen.blit(self.stoneCostImage, (1225 + self.costPadding + 45, 485))
            self.screen.blit(self.oreCostImage, (1225 + self.costPadding * 2 + 90, 485))
            self.screen.blit(self.populationCostImage, (1225 + self.costPadding * 3 + 135, 485))
        else:
            self.drawInspector()
            #INSPECTOR SELECTED

        self.screen.blit(self.tab1BuildingText, (self.tabButtonXValue + 30, self.tabButtonYValue + 5))
        self.screen.blit(self.tab1InspectorText, (self.tabButtonXValue + self.tabButtonWidth + 30, self.tabButtonYValue + 5))

    def goToBuildingTab(self):
        '''Switches to Building Tab'''
        self.inspector = False
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        
        if(self.currentBuildingTab == 0):
            self.goToResourceBuildings()
        elif(self.currentBuildingTab == 1):
            self.goToMilitaryBuildings()
        elif(self.currentBuildingTab == 2):
            self.goToInfrastructureBuildings()

        self.screen.blit(self.resourceTabText, (self.tabButton2XValue + 14, self.tabButton2YValue + 4))
        self.screen.blit(self.militaryTabText, (self.tabButton2XValue + 14 + self.tabButton2Width, self.tabButton2YValue + 4))
        self.screen.blit(self.infrastructureTabText, (self.tabButton2XValue + 14 + self.tabButton2Width * 2, self.tabButton2YValue + 4))

    def goToInspectorTab(self):
        '''Switches to Inspector Tab'''
        self.inspector = True
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()

    def goToResourceBuildings(self):
        '''Switches to Resource Tab'''
        self.currentBuildingTab = 0
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        self.switchSelectedBuilding(0)
        self.drawResourceBuildings(self.buildingID)
        
    def goToMilitaryBuildings(self):
        '''Switches to Military Tab'''
        self.currentBuildingTab = 1
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        self.switchSelectedBuilding(10)
        self.drawMilitaryBuildings(self.buildingID)

    def goToInfrastructureBuildings(self):
        '''Switches to Infrastructure Tab'''
        self.currentBuildingTab = 2
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        self.switchSelectedBuilding(6)
        self.drawInfrastructureBuildings(self.buildingID)
        
    def updateResources(self, player):
        tempW = 0
        tempS = 0
        tempO = 0
        tempF = 0
        for i in range(len(player.buildings)):
            if player.buildings[i].buildingType == 3:     #IF LUMBERMILL
                tempW += player.buildings[i].productionRate
            elif player.buildings[i].buildingType == 4:     #IF QUARRY
                tempS += player.buildings[i].productionRate
            elif player.buildings[i].buildingType == 5:     #IF MINE
                tempO += player.buildings[i].productionRate
            if player.buildings[i].buildingType == 0 or player.buildings[i].buildingType == 1 or player.buildings[i].buildingType == 2:     #IF FARM, RANCH, OR FISH HUT
                tempF += player.buildings[i].productionRate
        
        self.resourcesPerTurn[0] = tempW
        self.resourcesPerTurn[1] = tempS
        self.resourcesPerTurn[2] = tempO
        self.resourcesPerTurn[3] = tempF - (player.playerMaxPop -player.playerCurPop)

        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.woodCount = self.resourceCountFont.render(str(player.playerWood) + " " + str(self.resourcesPerTurn[0]) + "/Turn", True, pg.Color('black'))
        self.stoneCount = self.resourceCountFont.render(str(player.playerStone) + " " + str(self.resourcesPerTurn[1]) + "/Turn", True, pg.Color('black'))
        self.oreCount = self.resourceCountFont.render(str(player.playerOre) + " " + str(self.resourcesPerTurn[2]) + "/Turn", True, pg.Color('black'))
        self.foodCount = self.resourceCountFont.render(str(player.playerFood) + " " + str(self.resourcesPerTurn[3]) + "/Turn", True, pg.Color('black'))
        self.populationCount = self.resourceCountFont.render(str(player.playerCurPop) + " / " + str(player.playerMaxPop), True, pg.Color('black'))
        self.drawInterface()

    def drawInspector(self):
        pg.draw.rect(self.screen, self.rectColor, (1005, 450, 490, 500))
        #LEFT TAB: BUILDING
        pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButtonXValue, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))
        #RIGHT TAB: INSPECTOR
        pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButtonXValue + self.tabButtonWidth, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))

        self.screen.blit(self.tab1BuildingText, (self.tabButtonXValue + 30, self.tabButtonYValue + 5))
        self.screen.blit(self.tab1InspectorText, (self.tabButtonXValue + self.tabButtonWidth + 30, self.tabButtonYValue + 5))

        #INSPECTOR TITLES
        self.tileTypeText = self.tab1Font.render("Tile Type: " + str(self.currentTile), True, pg.Color('black'))
        self.tileResources = self.tab1Font.render("Resources In Tile: ", True, pg.Color('black'))
        self.tileBuilding = self.tab1Font.render("Building: " + self.currentBuildingName, True, pg.Color('black'))
        self.costMod = self.tab1Font.render("Building Cost Modifier: " + self.costModiferNumber, True, pg.Color('black'))
        self.prefBuilding = self.tab1Font.render("Preferred Building: " + self.prefBuildingName, True, pg.Color('black'))

        self.woodInTileImage = pg.transform.scale(self.woodImage, (35, 23))
        self.stoneInTileImage = pg.transform.scale(self.stoneImage, (35, 23))
        self.oreInTileImage = pg.transform.scale(self.oreImage, (35, 23))

        self.woodInTile = self.tab2Font.render(str(self.tileWoodAmount) + self.woodPerTurnInspector, True, pg.Color('black'))
        self.stoneInTile = self.tab2Font.render(str(self.tileStoneAmount) + self.stonePerTurnInspector, True, pg.Color('black'))
        self.oreInTile = self.tab2Font.render(str(self.tileOreAmount) + self.orePerTurnInspector, True, pg.Color('black'))

        self.screen.blit(self.tileTypeText, (1050, 465))
        self.screen.blit(self.costMod, (1050, 510))
        self.screen.blit(self.prefBuilding, (1050, 555))
        self.screen.blit(self.tileBuilding, (1050, 600))
        self.screen.blit(self.tileResources, (1050, 645))

        self.screen.blit(self.woodInTileImage, (1100, 685))
        self.screen.blit(self.stoneInTileImage, (1100, 715))
        self.screen.blit(self.oreInTileImage, (1100, 745))

        self.screen.blit(self.woodInTile, (1150, 690))
        self.screen.blit(self.stoneInTile, (1150, 720))
        self.screen.blit(self.oreInTile, (1150, 750))

    def updateInspector(self, x, y, board):
        inspector = InspectorGadget.Inspector()
        self.currentTileNumber = inspector.inspectTile(board, x, y)[0]
        if(self.currentTileNumber == 0):
            self.currentTile = "Forest"
            self.prefBuildingName = "Lumber Mill"
            self.costModiferNumber = "1.2"
        elif(self.currentTileNumber == 1):
            self.currentTile = "Mountain"
            self.prefBuildingName = "Quarry"
            self.costModiferNumber = "1.5"
        elif(self.currentTileNumber == 2):
            self.currentTile = "Hill"
            self.prefBuildingName = "Farm"
            self.costModiferNumber = "1.3"
        elif(self.currentTileNumber == 3):
            self.currentTile = "Plain"
            self.prefBuildingName = "Ranch"
            self.costModiferNumber = "1"
        elif(self.currentTileNumber == 4):
            self.currentTile = "Water"
            self.prefBuildingName = "None"
            self.costModiferNumber = "1"
        self.tileWoodAmount = inspector.inspectTile(board, x, y)[1]
        self.tileStoneAmount = inspector.inspectTile(board, x, y)[2]
        self.tileOreAmount = inspector.inspectTile(board, x, y)[3]

        done = False
        
        for i in range(len(self.player1.buildings)):
            if(math.floor(self.player1.buildings[i].x/100) == x and math.floor(self.player1.buildings[i].y/100) == y):
                self.currentBuildingName = int(str(self.player1.buildings[i]))
                done = True
                break
            else:
                done = False
                self.currentBuildingName = -1
        if (not done):
            for i in range(len(self.player2.buildings)):
                if(math.floor(self.player2.buildings[i].x/100) == x and math.floor(self.player2.buildings[i].y/100) == y):
                    self.currentBuildingName = int(str(self.player2.buildings[i]))
                    break
                else:
                    self.currentBuildingName = -1

        if(self.currentBuildingName == 0):
            self.currentBuildingName = "Farm"
        elif(self.currentBuildingName == 1):
            self.currentBuildingName = "Ranch"
        elif(self.currentBuildingName == 2):
            self.currentBuildingName = "Fishing Hut"
        elif(self.currentBuildingName == 3):
            self.currentBuildingName = "Lumber Mill"
        elif(self.currentBuildingName == 4):
            self.currentBuildingName = "Quarry"
        elif(self.currentBuildingName == 5):
            self.currentBuildingName = "Mine"
        elif(self.currentBuildingName == 6):
            self.currentBuildingName = "House"
        elif(self.currentBuildingName == 7):
            self.currentBuildingName = "Town"
        elif(self.currentBuildingName == 8):
            self.currentBuildingName = "City"
        elif(self.currentBuildingName == 9):
            self.currentBuildingName = "Bridge"
        elif(self.currentBuildingName == 10):
            self.currentBuildingName = "Castle"
        elif(self.currentBuildingName == 11):
            self.currentBuildingName = "Outpost"
        elif(self.currentBuildingName == 12):
            self.currentBuildingName = "Cannon Tower"
        else:
            self.currentBuildingName = "None"
            
        self.drawInspector()
    def drawResourceBuildings(self, buildingID):
        '''Draws the Resource Tab'''
        self.buildingID = buildingID

        self.switchSelectedBuilding(self.buildingID)

        self.screen.blit(self.farmImage, (1050 + self.buildingPadding, 500 + self.buildingPadding))
        self.screen.blit(self.ranchImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 2 + self.buildingWidth))
        self.screen.blit(self.fishImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 3 + self.buildingWidth * 2))
        self.screen.blit(self.lumberMillImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 4 + self.buildingWidth * 3))
        self.screen.blit(self.quarryImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 5 + self.buildingWidth * 4))
        self.screen.blit(self.mineImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 6 + self.buildingWidth * 5))

        self.farmName = self.buildingFont.render("Farm", True, pg.Color('black'))
        self.screen.blit(self.farmName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (3/4) + self.buildingWidth/2))

        self.ranchName = self.buildingFont.render("Ranch", True, pg.Color('black'))
        self.screen.blit(self.ranchName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (7/4) + self.buildingWidth * (3/2)))

        self.fishName = self.buildingFont.render("Fishing Hut", True, pg.Color('black'))
        self.screen.blit(self.fishName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (11/4) + self.buildingWidth * (5/2)))

        self.lumberMillName = self.buildingFont.render("Lumber Mill", True, pg.Color('black'))
        self.screen.blit(self.lumberMillName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (15/4) + self.buildingWidth * (7/2)))

        self.quarryName = self.buildingFont.render("Quarry", True, pg.Color('black'))
        self.screen.blit(self.quarryName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (19/4) + self.buildingWidth * (9/2)))

        self.mineName = self.buildingFont.render("Mine", True, pg.Color('black'))
        self.screen.blit(self.mineName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (23/4) + self.buildingWidth * (11/2)))

        for i in range(6):
            self.drawResourceCosts(i)
    
    def drawMilitaryBuildings(self, buildingID):
        '''Draws the Military Tab'''
        self.buildingID = buildingID
        self.switchSelectedBuilding(self.buildingID)

        self.screen.blit(self.castleImage, (1050 + self.buildingPadding, 500 + self.buildingPadding))
        self.screen.blit(self.outpostImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 2 + self.buildingWidth))
        self.screen.blit(self.cannonImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 3 + self.buildingWidth * 2))

        self.castleName = self.buildingFont.render("Castle", True, pg.Color('black'))
        self.screen.blit(self.castleName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (3/4) + self.buildingWidth/2))

        self.outpostName = self.buildingFont.render("Outpost", True, pg.Color('black'))
        self.screen.blit(self.outpostName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (7/4) + self.buildingWidth * (3/2)))

        self.cannonName = self.buildingFont.render("Cannon Tower", True, pg.Color('black'))
        self.screen.blit(self.cannonName, (1030 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (11/4) + self.buildingWidth * (5/2)))

        for i in range(10, 13):
            self.drawResourceCosts(i)

    def drawInfrastructureBuildings(self, buildingID):
        self.buildingID = buildingID
        self.switchSelectedBuilding(self.buildingID)

        self.screen.blit(self.houseImage, (1050 + self.buildingPadding, 500 + self.buildingPadding))
        self.screen.blit(self.townImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 2 + self.buildingWidth))
        self.screen.blit(self.cityImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 3 + self.buildingWidth * 2))
        self.screen.blit(self.bridgeImage, (1050 + self.buildingPadding, 500 + self.buildingPadding * 4 + self.buildingWidth * 3))

        self.houseName = self.buildingFont.render("House", True, pg.Color('black'))
        self.screen.blit(self.houseName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (3/4) + self.buildingWidth * (1/2)))

        self.townName = self.buildingFont.render("Town", True, pg.Color('black'))
        self.screen.blit(self.townName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (7/4) + self.buildingWidth * (3/2)))

        self.cityName = self.buildingFont.render("City", True, pg.Color('black'))
        self.screen.blit(self.cityName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (11/4) + self.buildingWidth * (5/2)))

        self.bridgeName = self.buildingFont.render("Bridge", True, pg.Color('black'))
        self.screen.blit(self.bridgeName, (1035 + self.buildingPadding * 2 + self.buildingWidth, 500 + self.buildingPadding * (15/4) + self.buildingWidth * (7/2)))

        for i in range(6, 10):
            self.drawResourceCosts(i)

        # print("Drawing Other Buildings")
        sys.stdout.flush()

    def drawResourceCosts(self, buildingID):
        '''Draws Resource Costs for Specified Building'''
        if(buildingID == 0):
            self.resources = self.tab2Font.render(self.farmCost, True, pg.Color('black'))  
            self.screen.blit(self.resources, (1230, 545))
        if(buildingID == 1):
            self.resources = self.tab2Font.render(self.ranchCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (7/4) + self.buildingWidth * (3/2)))
        if(buildingID == 2):
            self.resources = self.tab2Font.render(self.fishCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (11/4) + self.buildingWidth * (5/2)))
        if(buildingID == 3):
            self.resources = self.tab2Font.render(self.lumberMillCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (15/4) + self.buildingWidth * (7/2)))
        if(buildingID == 4):
            self.resources = self.tab2Font.render(self.quarryCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (19/4) + self.buildingWidth * (9/2)))
        if(buildingID == 5):
            self.resources = self.tab2Font.render(self.mineCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (23/4) + self.buildingWidth * (11/2)))
        if(buildingID == 6):
            self.resources = self.tab2Font.render(self.houseCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 545))
        if(buildingID == 7):
            self.resources = self.tab2Font.render(self.townCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (7/4) + self.buildingWidth * (3/2)))
        if(buildingID == 8):
            self.resources = self.tab2Font.render(self.cityCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (11/4) + self.buildingWidth * (5/2)))
        if(buildingID == 9):
            self.resources = self.tab2Font.render(self.bridgeCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (15/4) + self.buildingWidth * (7/2)))
        if(buildingID == 10):
            self.resources = self.tab2Font.render(self.castleCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 545))
        if(buildingID == 11):
            self.resources = self.tab2Font.render(self.outpostCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (7/4) + self.buildingWidth * (3/2)))
        if(buildingID == 12):
            self.resources = self.tab2Font.render(self.cannonCost, True, pg.Color('black'))
            self.screen.blit(self.resources, (1230, 500 + self.buildingPadding * (11/4) + self.buildingWidth * (5/2)))

        pg.draw.rect(self.screen, pg.Color(183, 183, 183), (1225, 500, 3, 490))

    def switchSelectedBuilding(self, buildingID):
        '''Switches the Currently Selected Building'''
        if(not self.inspector):
            if(buildingID == 0 or buildingID == 10 or buildingID == 6):
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (1050, 496 + self.buildingPadding, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor,(1050, 496 + self.buildingPadding * 2 + self.buildingWidth, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 3 + self.buildingWidth * 2, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0 or self.currentBuildingTab == 2):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 4 + self.buildingWidth * 3, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 5 + self.buildingWidth * 4, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 6 + self.buildingWidth * 5, self.buildingRect1Width, self.buildingRect1Height + 8))
            elif(buildingID == 1 or buildingID == 11 or buildingID == 7):
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonSelectedColor,(1050, 496 + self.buildingPadding * 2 + self.buildingWidth, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 3 + self.buildingWidth * 2, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0 or self.currentBuildingTab == 2):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 4 + self.buildingWidth * 3, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 5 + self.buildingWidth * 4, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 6 + self.buildingWidth * 5, self.buildingRect1Width, self.buildingRect1Height + 8))
            elif(buildingID == 2 or buildingID == 12 or buildingID == 8):
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor,(1050, 496 + self.buildingPadding * 2 + self.buildingWidth, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (1050, 496 + self.buildingPadding * 3 + self.buildingWidth * 2, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0 or self.currentBuildingTab == 2):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 4 + self.buildingWidth * 3, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 5 + self.buildingWidth * 4, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 6 + self.buildingWidth * 5, self.buildingRect1Width, self.buildingRect1Height + 8))
            elif(buildingID == 3 or buildingID == 9):
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor,(1050, 496 + self.buildingPadding * 2 + self.buildingWidth, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 3 + self.buildingWidth * 2, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0 or self.currentBuildingTab == 2):
                    pg.draw.rect(self.screen, self.tabButtonSelectedColor, (1050, 496 + self.buildingPadding * 4 + self.buildingWidth * 3, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 5 + self.buildingWidth * 4, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 6 + self.buildingWidth * 5, self.buildingRect1Width, self.buildingRect1Height + 8))
            elif(buildingID == 4):
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor,(1050, 496 + self.buildingPadding * 2 + self.buildingWidth, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 3 + self.buildingWidth * 2, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 4 + self.buildingWidth * 3, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonSelectedColor, (1050, 496 + self.buildingPadding * 5 + self.buildingWidth * 4, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 6 + self.buildingWidth * 5, self.buildingRect1Width, self.buildingRect1Height + 8))
            elif(buildingID == 5):
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor,(1050, 496 + self.buildingPadding * 2 + self.buildingWidth, self.buildingRect1Width, self.buildingRect1Height + 8))
                pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 3 + self.buildingWidth * 2, self.buildingRect1Width, self.buildingRect1Height + 8))
                if(self.currentBuildingTab == 0):
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 4 + self.buildingWidth * 3, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonColor, (1050, 496 + self.buildingPadding * 5 + self.buildingWidth * 4, self.buildingRect1Width, self.buildingRect1Height + 8))
                    pg.draw.rect(self.screen, self.tabButtonSelectedColor, (1050, 496 + self.buildingPadding * 6 + self.buildingWidth * 5, self.buildingRect1Width, self.buildingRect1Height + 8))

    def detectClick(self, boardCoords):
        '''The True Detect Click Function'''
        if(pg.mouse.get_pressed()[0]):
            if(boardCoords):
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)
                return (self.xCoord, self.yCoord)
            else:
                return pg.mouse.get_pos()
        else:
            return (-1, -1)

    def detectTabChange(self, tabID):
        if(tabID == 0):
            if(not self.detectClick(False) == (-1, -1)):
                if((self.tabButtonXValue < self.detectClick(False)[0] < self.tabButtonXValue + self.tabButtonWidth) and (self.inspector == True) and (self.tabButtonYValue < self.detectClick(False)[1] < self.tabButtonYValue + self.tabButtonHeight)):
                    # print("Tab 1 clicked")
                    sys.stdout.flush()
                    self.goToBuildingTab()
                elif(self.tabButtonXValue + self.tabButtonWidth < self.detectClick(False)[0] < self.tabButtonXValue + 2 * self.tabButtonWidth and self.inspector == False and self.tabButtonYValue < self.detectClick(False)[1] < self.tabButtonYValue + self.tabButtonHeight):
                    # print("Tab 2 clicked")
                    sys.stdout.flush()
                    self.goToInspectorTab()
        elif(tabID == 1):
            if(not self.detectClick(False) == (-1, -1)):
                if(self.tabButton2XValue < self.detectClick(False)[0] < self.tabButton2XValue + self.tabButton2Width and not self.currentBuildingTab == 0 and self.tabButton2YValue < self.detectClick(False)[1] < self.tabButton2YValue + self.tabButton2Height and not self.inspector):
                    # print("Switched to Resource Buildings")
                    sys.stdout.flush()
                    self.goToResourceBuildings()
                elif(self.tabButton2XValue + self.tabButton2Width < self.detectClick(False)[0] < self.tabButton2XValue + self.tabButton2Width * 2 and not self.currentBuildingTab == 1 and self.tabButton2YValue < self.detectClick(False)[1] < self.tabButton2YValue + self.tabButton2Height and not self.inspector):
                    # print("Switched to Military Buildings")
                    sys.stdout.flush()
                    self.goToMilitaryBuildings()
                elif(self.tabButton2XValue + self.tabButton2Width * 2 < self.detectClick(False)[0] < self.tabButton2XValue + self.tabButton2Width * 3 and not self.currentBuildingTab == 2 and self.tabButton2YValue < self.detectClick(False)[1] < self.tabButton2YValue + self.tabButton2Height and not self.inspector):
                    # print("Switched to Infrastructure Buildings")
                    sys.stdout.flush()
                    self.goToInfrastructureBuildings()
                    
    def switchEndTurnButton(self, color):
        self.currentTurn = color
        if(self.currentTurn == "blue"):
            pg.draw.rect(self.screen, self.rectColor, (1050, 350, 150, 35))
            pg.draw.rect(self.screen, pg.Color(159, 163, 206), (1050, 350, 150, 35))
            pg.draw.rect(self.screen, pg.Color(97, 125, 147), (1050, 350, 150, 35), 3)
            self.screen.blit(self.endTurnText, (1065, 355))
        elif(self.currentTurn == "red"):
            pg.draw.rect(self.screen, self.rectColor, (1050, 350, 150, 35))
            pg.draw.rect(self.screen, pg.Color(168, 25, 25), (1050, 350, 150, 35))
            pg.draw.rect(self.screen, pg.Color(112, 15, 15), (1050, 350, 150, 35), 3)
            self.screen.blit(self.endTurnText, (1065, 355))

    def displayError(self, message):
        pg.draw.rect(self.screen, pg.Color('white'), (1230, 347, 220, 38))
        pg.draw.rect(self.screen, pg.Color('black'), (1230, 347, 220, 38), 3)
        errorMessage = self.tab2Font.render(message, True, pg.Color('black'))
        self.screen.blit(errorMessage, (1249, 360))
        
    def getPlayer(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
