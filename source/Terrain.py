import pygame as pg, time, math, random
from source import TileCreate as tc

class Terrain():
    """Makes the world as we know it"""

    def __init__(self, boardNum, screenWidth, tilesize):
        self.boardNum = boardNum
        self.screenWidth = screenWidth
        self.tileWidth = math.floor(self.screenWidth/self.boardNum)
        self.tilesize = tilesize
        # Tile Colors
        # self.forestColor = (34,139,34)
        # self.hillColor = (152,251,152)
        # self.plainColor = (247,218,61)
        # self.mountainColor = (205,201,201)
        # self.waterColor = (30,144,255)
        # Tile Images
        
        # hd = True
        hd = False

        if hd:
            self.forestTile = pg.image.load("Images/forestTileHiRes.png")
            self.forestTile = pg.transform.scale(self.forestTile, (int(self.tilesize), int(self.tilesize)))
            self.mountainTile = pg.image.load("Images/mountainTileHiRes.png")
            self.mountainTile = pg.transform.scale(self.mountainTile, (int(self.tilesize), int(self.tilesize)))
            self.hillTile = pg.image.load("Images/hillTileHiRes.png")
            self.hillTile = pg.transform.scale(self.hillTile, (int(self.tilesize), int(self.tilesize)))
            self.plainTile = pg.image.load("Images/plainTileHiRes.png")
            self.plainTile = pg.transform.scale(self.plainTile, (int(self.tilesize), int(self.tilesize)))
            self.waterTile = pg.image.load("Images/waterTileHiRes.png")
            self.waterTile = pg.transform.scale(self.waterTile, (int(self.tilesize), int(self.tilesize)))
            self.tileType = None
        else:
            self.forestTile = pg.image.load("Images/forestTile.png")
            self.forestTile = pg.transform.scale(self.forestTile, (int(self.tilesize), int(self.tilesize)))
            self.mountainTile = pg.image.load("Images/mountainTile.png")
            self.mountainTile = pg.transform.scale(self.mountainTile, (int(self.tilesize), int(self.tilesize)))
            self.hillTile = pg.image.load("Images/hillTile.png")
            self.hillTile = pg.transform.scale(self.hillTile, (int(self.tilesize), int(self.tilesize)))
            self.plainTile = pg.image.load("Images/plainTile.png")
            self.plainTile = pg.transform.scale(self.plainTile, (int(self.tilesize), int(self.tilesize)))
            self.waterTile = pg.image.load("Images/waterTile.png")
            self.waterTile = pg.transform.scale(self.waterTile, (int(self.tilesize), int(self.tilesize)))
            self.tileType = None
            
    def generateBoard(self, screen):
        """Generates the board with different tiles"""
        self.board = []
        for i in range(self.boardNum):
            row = []
            for j in range(self.boardNum):
                tileResourceColor = None
                if 6<i+j<12:     #IF BOARD SIZE IS NOT 10 THEN THIS WILL NOT WORK AS EXPECTED
                    self.generateOcean()    #CREATES THE CENTER AREA
                else:
                    self.generateLand()
                tile = tc.GenerateTile(self.tileType, i, j, screen)
                tile.generate_tile()
                tile.drawTile(self.tileWidth, self.tileImage)
                row.append(tile)
            self.board.append(row)

            # SETS TILE UNDER CASTLE TO BE PLAINS
        newTile = tc.GenerateTile(3, 1, 1, screen)
        self.tileImage = self.plainTile
        newTile.generate_tile()
        newTile.drawTile(self.tileWidth, self.tileImage)
        self.board[1][1] = newTile

        #COUNTS THE TYPES OF TILES IN THE TOP PLAYERS SIDE
        count = [0,0,0,0] #FOREST, MOUNTAIN, HILL, PLAIN
        for i in range(7):
            for j in range(7):
                if i==1 and j==1:
                    pass
                elif i+j<7: #IF ABOVE THE WEIRD ARBITRARY LINE THAT SEPARAES NO MAN LAND FROM PLAYER LAND
                    count[self.board[i][j].tileType]+=1
                    
        for i in range(3,self.boardNum):
            for j in range (3,self.boardNum):
                if i+j>11:  #IF ON P2'S SIDE
                    if i==self.boardNum-2 and j==self.boardNum-2:   #IF UNDER THE CASTLE
                        newTile = tc.GenerateTile(3, 8, 8, screen)
                        self.tileImage = self.plainTile
                        newTile.generate_tile()
                        newTile.drawTile(self.tileWidth, self.tileImage)
                        self.board[self.boardNum-2][self.boardNum-2] = newTile
                    else:
                        tryAgain = True
                        while tryAgain:
                            rand = random.randint(0,3) 
                            if count[rand]>0:
                                tryAgain = False
                                count[rand]-=1
                                newTile = tc.GenerateTile(rand, i, j, screen)
                                if rand==0:
                                    self.tileImage = self.forestTile
                                elif rand==1:
                                    self.tileImage = self.mountainTile
                                elif rand==2:
                                    self.tileImage = self.hillTile
                                else:#IF RAND==3
                                    self.tileImage = self.plainTile
                                newTile.generate_tile()
                                newTile.drawTile(self.tileWidth, self.tileImage)
                                self.board[i][j] = newTile

        return self.board

    def generateLand(self): #ID'S: FOREST=0, MOUNTAIN=1, HILL=2, PLAIN=3
        """Generates the land"""
        getType = random.randint(0,6)
        if getType <= 1: #IF 0 OR 1
            self.tileImage = self.forestTile
            self.tileType = 0
        elif getType == 2: #IF 2
            self.tileImage = self.mountainTile
            self.tileType = 1
        elif getType >= 3 and getType <= 4: #IF 3 OR 4
            self.tileImage = self.hillTile
            self.tileType = 2
        elif getType >= 5 and getType <= 6: #IF 5 OR 6
            self.tileImage = self.plainTile
            self.tileType = 3
        
    def generateOcean(self):
        """Generates the ocean zone"""
        # Change the chance of Ocean appearing
        getType = random.randint(0,6)
        if getType == 0:
            self.tileImage = self.forestTile
            self.tileType = 0
        elif getType == 1:
            self.tileImage = self.mountainTile
            self.tileType = 1
        elif getType == 2:
            self.tileImage = self.hillTile
            self.tileType = 2
        elif getType == 3:
            self.tileImage = self.plainTile
            self.tileType = 3
        elif getType >= 4:
            self.tileImage = self.waterTile
            self.tileType = 4