import pygame as pg, time, math, TileCreate as tc, random

"""Makes the world as we know it"""
class Terrain():

    def __init__(self, boardNum, screenWidth):
        self.boardNum = boardNum
        self.screenWidth = screenWidth
        self.tileWidth = math.floor(self.screenWidth/self.boardNum)
        self.board = []

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
                row.append(tile.generate_tile(i,j,self.tileWidth, pg.Color(self.tileResourceColor), screen))
            self.board.append(row)
    
    def generateLand(self):
        tileResourceType = random.randint(0,3)
        if tileResourceType == 0:
            self.tileResourceColor = "Forest Green"
        elif tileResourceType == 1:
            self.tileResourceColor = "Snow 3"
        elif tileResourceType == 2:
            self.tileResourceColor = "Spring Green"
        elif tileResourceType == 3:
            self.tileResourceColor = "Pale Green"
        
    def generateOcean(self):
        # Change the chance of Ocean appearing
        tileResourceType = random.randint(0,8)
        if tileResourceType == 0:
            self.tileResourceColor = "Forest Green"
        elif tileResourceType == 1:
            self.tileResourceColor = "Snow 3"
        elif tileResourceType == 2:
            self.tileResourceColor = "Spring Green"
        elif tileResourceType == 3:
            self.tileResourceColor = "Pale Green"
        elif tileResourceType >= 4:
            self.tileResourceColor = "Dodger Blue"

        print(self.board)
        return self.board