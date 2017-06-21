import pygame as pg, time, math, TileCreate as tc, random

class Terrain():
"""Makes the world as we know it"""

    def __init__(self, boardNum, screenWidth):
        self.boardNum = boardNum
        self.screenWidth = screenWidth
        self.tileWidth = math.floor(self.screenWidth/self.boardNum)
        self.board = []
        # Tile Colors
        self.forestColor = (34,139,34)
        self.hillColor = (152,251,152)
        self.plainColor = (247,218,61)
        self.mountainColor = (205,201,201)
        self.waterColor = (30,144,255)

    def generateBoard(self, screen):
        for i in range(self.boardNum):
            row = []
            for j in range(self.boardNum):
                tile = tc.GenerateTile(0)
                tileResourceColor = None
                if j >= 7 and i == 0:
                    self.generateOcean()
                elif j >= 6 and i == 1:
                    self.generateOcean()
                elif j >= 5 and i == 2:
                    self.generateOcean()
                elif j >= 4 and j <= 8 and i == 3:
                    self.generateOcean()
                elif j >= 3 and j <= 7 and i == 4:
                    self.generateOcean()
                elif j >= 2 and j <= 6 and i == 5:
                    self.generateOcean()
                elif j >= 1 and j <= 5 and i == 6:
                    self.generateOcean()
                elif j <= 4 and i == 7:
                    self.generateOcean()
                elif j <= 3 and i == 8:
                    self.generateOcean()
                elif j <= 2 and i == 9:
                    self.generateOcean()
                else:
                    self.generateLand()
                row.append(tile.generate_tile(i,j,self.tileWidth, self.tileResourceColor, screen))
            self.board.append(row)
        print(self.board)
        return self.board
    
    def generateLand(self):
        getType = random.randint(0,6)
        if getType <= 1:
            self.tileResourceColor = self.forestColor
        elif getType == 2:
            self.tileResourceColor = self.mountainColor
        elif getType >= 3 and getType <= 4:
            self.tileResourceColor = self.hillColor
        elif getType >= 5 and getType <= 6:
            self.tileResourceColor = self.plainColor
        
    def generateOcean(self):
        # Change the chance of Ocean appearing
        getType = random.randint(0,8)
        if getType == 0:
            self.tileResourceColor = self.forestColor
        elif getType == 1:
            self.tileResourceColor = self.mountainColor
        elif getType == 2:
            self.tileResourceColor = self.hillColor
        elif getType == 3:
            self.tileResourceColor = self.plainColor
        elif getType >= 4:
            self.tileResourceColor = self.waterColor