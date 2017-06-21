import pygame as pg
import sys

class UserInterface():
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.SysFont("monospace", 50)
        self.resourceCountFont = pg.font.SysFont("monospace", 30)
        self.resourceText = self.font.render("Resources", True, pg.Color('black'))
        self.woodCount = self.resourceCountFont.render("Wood", True, pg.Color('black'))
        self.stoneCount = self.resourceCountFont.render("Stone", True, pg.Color('black'))
        self.oreCount = self.resourceCountFont.render("Ore", True, pg.Color('black'))
        self.foodCount = self.resourceCountFont.render("Food", True, pg.Color('black'))
        self.popCount = self.resourceCountFont.render("Population", True, pg.Color('black'))

        self.rectXPos = 1000
        self.rectYPos = 0
        self.rectWidth = 500
        self.rectHeight = 1000
        self.rectColor = pg.Color(183, 183, 183)

        self.inspector = False

        self.tabButtonHeight = 35
        self.tabButtonWidth = 200
        self.tabButtonXValue = 1050
        self.tabButtonYValue = 400
        self.tabButtonColor = pg.Color(145, 145, 145)
        self.tabButtonSelectedColor = pg.Color(99, 99, 99)

    def drawInterface(self):
        pg.draw.rect(self.screen, self.rectColor, (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.screen.blit(self.resourceText, (1125, 25))
        self.screen.blit(self.woodCount, (1050, 100))
        self.screen.blit(self.stoneCount, (1050, 150))
        self.screen.blit(self.oreCount, (1050, 200))
        self.screen.blit(self.foodCount, (1050, 250))
        self.screen.blit(self.popCount, (1050, 300))

        if(not self.inspector):
            #LEFT TAB: BUILDING
            pg.draw.rect(self.screen, self.tabButtonSelectedColor, (self.tabButtonXValue, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))
            #RIGHT TAB: INSPECTOR
            pg.draw.rect(self.screen, self.tabButtonColor, (self.tabButtonXValue + self.tabButtonWidth, self.tabButtonYValue, self.tabButtonWidth, self.tabButtonHeight))
            #TODO: DRAW BUILDING OPTIONS
        else:
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

    def detectTabChange(self):
        if(not self.detectClick(False) == (-1, -1)):
            if((self.tabButtonXValue < self.detectClick(False)[0] < self.tabButtonXValue + self.tabButtonWidth) and (self.inspector == True) and (self.tabButtonYValue < self.detectClick(False)[1] < self.tabButtonYValue + self.tabButtonHeight)):
                print("Tab 1 clicked")
                sys.stdout.flush()
                self.goToBuildingTab()
            elif(self.tabButtonXValue + self.tabButtonWidth < self.detectClick(False)[0] < self.tabButtonXValue + 2 * self.tabButtonWidth and self.inspector == False and self.tabButtonYValue < self.detectClick(False)[1] < self.tabButtonYValue + self.tabButtonHeight):
                print("Tab 2 clicked")
                sys.stdout.flush()
                self.goToInspectorTab()