import pygame as pg
import sys
import Player

class UserInterface():
    def __init__(self, screen):
        #Init stuff
        self.screen = screen
        self.font = pg.font.SysFont("monospace", 50)
        self.resourceCountFont = pg.font.SysFont("monospace", 30)

        #Resources List
        self.resourceText = self.font.render("Resources", True, pg.Color('black'))
        self.woodCountText = self.resourceCountFont.render("Wood", True, pg.Color('black'))
        self.stoneCountText = self.resourceCountFont.render("Stone", True, pg.Color('black'))
        self.oreCountText = self.resourceCountFont.render("Ore", True, pg.Color('black'))
        self.foodCountText = self.resourceCountFont.render("Food", True, pg.Color('black'))
        self.popCountText = self.resourceCountFont.render("Population", True, pg.Color('black'))

        #Resource Images
        self.woodImage = pg.image.load("Images/log.png")
        self.woodImage = pg.transform.scale(self.woodImage, (70, 45))

        self.stoneImage = pg.image.load("Images/stone.png")
        self.stoneImage = pg.transform.scale(self.stoneImage, (70, 45))

        self.oreImage = pg.image.load("Images/ore.png")
        self.oreImage = pg.transform.scale(self.oreImage, (70, 45))

        self.foodImage = pg.image.load("Images/food.png")
        self.foodImage = pg.transform.scale(self.foodImage, (60, 45))

        self.populationImage = pg.image.load("Images/pop.png")
        self.populationImage = pg.transform.scale(self.populationImage, (45, 45))

        #Resource Amounts
        self.woodCount = self.resourceCountFont.render("0", True, pg.Color('black'))
        self.stoneCount = self.resourceCountFont.render("0", True, pg.Color('black'))
        self.oreCount = self.resourceCountFont.render("0", True, pg.Color('black'))
        self.foodCount = self.resourceCountFont.render("0", True, pg.Color('black'))
        self.populationCount = self.resourceCountFont.render("0", True, pg.Color('black'))

        #Background rectangle dimensions
        self.rectXPos = 1000
        self.rectYPos = 0
        self.rectWidth = 500
        self.rectHeight = 1000
        self.rectColor = pg.Color(183, 183, 183)

        self.inspector = False

        #First Tab Dimensions
        self.tabButtonHeight = 35
        self.tabButtonWidth = 200
        self.tabButtonXValue = 1050
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

        self.wood = 0
        self.stone = 0
        self.food = 0
        self.ore = 0
        self.maxPopulation = 0
        self.currentPopulation = 0

    def drawInterface(self):
        self.drawResourceBuildings()
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))

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

            elif(self.currentBuildingTab == 1):
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))

            elif(self.currentBuildingTab == 2):
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
                pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, self.tabButton2Width, self.tabButton2Height))
            #DRAW DIVIDERS
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width, self.tabButton2YValue, 2, self.tabButton2Height))
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButton2XValue + self.tabButton2Width * 2, self.tabButton2YValue, 2, self.tabButton2Height))
            #TODO: DRAW BUILDING OPTIONS
        else:
            #INSPECTOR SELECTED
            #LEFT TAB: BUILDING
            pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButtonXValue, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))
            #RIGHT TAB: INSPECTOR
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButtonXValue + self.tabButtonWidth, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))

    def goToBuildingTab(self):
        self.inspector = False
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()

    def goToInspectorTab(self):
        self.inspector = True
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()

    def goToResourceBuildings(self):
        self.currentBuildingTab = 0
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        self.drawResourceBuildings()

    def goToMilitaryBuildings(self):
        self.currentBuildingTab = 1
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        self.drawMilitaryBuildings()

    def goToInfrastructureBuildings(self):
        self.currentBuildingTab = 2
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.drawInterface()
        self.drawInfrastructureBuildings()

    def updateResources(self, player):
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.woodCount = self.resourceCountFont.render(str(player.playerWood), True, pg.Color('black'))
        self.stoneCount = self.resourceCountFont.render(str(player.playerStone), True, pg.Color('black'))
        self.oreCount = self.resourceCountFont.render(str(player.playerOre), True, pg.Color('black'))
        self.foodCount = self.resourceCountFont.render(str(player.playerFood), True, pg.Color('black'))
        self.populationCount = self.resourceCountFont.render(str(player.playerCurPop + " / " +str(player.playerMaxPop)), True, pg.Color('black'))


    def drawResourceBuildings(self):
        print("Drawing Resource Buildings")
        sys.stdout.flush()
    
    def drawMilitaryBuildings(self):
        print("Drawing Military Buildings")
        sys.stdout.flush()

    def drawInfrastructureBuildings(self):
        print("Drawing Infrastructure Buildings")
        sys.stdout.flush()

    def detectClick(self, boardCoords):
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
                    print("Tab 1 clicked")
                    sys.stdout.flush()
                    self.goToBuildingTab()
                elif(self.tabButtonXValue + self.tabButtonWidth < self.detectClick(False)[0] < self.tabButtonXValue + 2 * self.tabButtonWidth and self.inspector == False and self.tabButtonYValue < self.detectClick(False)[1] < self.tabButtonYValue + self.tabButtonHeight):
                    print("Tab 2 clicked")
                    sys.stdout.flush()
                    self.goToInspectorTab()
        elif(tabID == 1):
            if(not self.detectClick(False) == (-1, -1)):
                if(self.tabButton2XValue < self.detectClick(False)[0] < self.tabButton2XValue + self.tabButton2Width and not self.currentBuildingTab == 0 and self.tabButton2YValue < self.detectClick(False)[1] < self.tabButton2YValue + self.tabButton2Height):
                    print("Switched to Resource Buildings")
                    sys.stdout.flush()
                    self.goToResourceBuildings()
                elif(self.tabButton2XValue + self.tabButton2Width < self.detectClick(False)[0] < self.tabButton2XValue + self.tabButton2Width * 2 and not self.currentBuildingTab == 1 and self.tabButton2YValue < self.detectClick(False)[1] < self.tabButton2YValue + self.tabButton2Height):
                    print("Switched to Military Buildings")
                    sys.stdout.flush()
                    self.goToMilitaryBuildings()
                elif(self.tabButton2XValue + self.tabButton2Width * 2 < self.detectClick(False)[0] < self.tabButton2XValue + self.tabButton2Width * 3 and not self.currentBuildingTab == 2 and self.tabButton2YValue < self.detectClick(False)[1] < self.tabButton2YValue + self.tabButton2Height):
                    print("Switched to Infrastructure Buildings")
                    sys.stdout.flush()
                    self.goToInfrastructureBuildings()
