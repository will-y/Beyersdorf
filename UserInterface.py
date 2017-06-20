import pygame as pg

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

        self.inspector = False

    def drawInterface(self):
        pg.draw.rect(self.screen, pg.Color(183, 183, 183), (self.rectXPos, self.rectYPos, self.rectWidth, self.rectHeight))
        self.screen.blit(self.resourceText, (1125, 25))
        self.screen.blit(self.woodCount, (1050, 100))
        self.screen.blit(self.stoneCount, (1050, 150))
        self.screen.blit(self.oreCount, (1050, 200))
        self.screen.blit(self.foodCount, (1050, 250))
        self.screen.blit(self.popCount, (1050, 300))

        if(not self.inspector):
            pg.draw.rect(self.screen, pg.Color(255, 142, 255), (1050, 500, 200, 50))
            pg.draw.rect(self.screen, pg.Color(145, 145, 145), (1250, 500, 200, 50))
        else:
            pg.draw.rect(self.screen, pg.Color(145, 145, 145), (1450, 500, 200, 50))

    def goToBuildingTab(self):
        self.inspector = False

    def goToInspectorTab(self):
        self.inspector = True