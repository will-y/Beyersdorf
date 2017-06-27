import math as m

"""Player class keeps track of that players wood, stone, ore, and food stores"""
class Player():
    def __init__(self):
        self.team = 0
        self.playerWood = 1000
        self.playerStone = 500
        self.playerOre = 75
        self.playerFood = 20
        self.playerCurPop = 0
        self.playerMaxPop = 10
        self.buildings = []

    def canBuy(self, amountwood, amountstone, amountore, amountpop):
        return self.playerWood + amountwood >= 0 and self.playerStone + amountstone >= 0 and self.playerOre + amountore >= 0 and self.playerCurPop + amountpop <= self.playerMaxPop

    def setWood(self,amount):
        self.playerWood=amount
    def editWood(self,amount):
        self.playerWood+=amount

    def setStone(self,amount):
        self.playerStone=amount
    def editStone(self,amount):
        self.playerStone+=amount

    def setOre(self,amount):
        self.playerOre=amount
    def editOre(self,amount):
        self.playerOre+=amount

    def setFood(self,amount):
        self.playerFood=amount
    def editFood(self,amount):
        self.playerFood+=amount

    def setCurPop(self,amount):
        self.playerCurPop=amount
    def editCurPop(self,amount):
        self.playerCurPop+=amount

    def setMaxPop(self,amount):
        self.playerMaxPop=amount
    def editMaxPop(self,amount):
        self.playerMaxPop+=amount
    
    def addBuilding(self,building):
        self.buildings.append(building)
        print(self.buildings)

    def canBuild(self,building,tileMap):

        if building.buildingType == 2:
            hasWater = False

<<<<<<< HEAD
            hasLeft = building.x/100>0
            hasRight = building.x/100<9
            hasUp = building.y/100>0
            hasDown = building.y/100<9
=======
            hasLeft =building.x>0
            hasRight = building.x<9
            hasUp = building.y>0
            hasDown = building.y<9
>>>>>>> eda4093e407814600f549e8419e7afc15cf41fa6
            if hasLeft and not hasWater:
                hasWater = (tileMap[(int)((building.x/100)-1)][(int)(building.y/100)].tileType == 4)
            if hasRight and not hasWater:
                hasWater = (tileMap[(int)((building.x/100)+1)][(int)(building.y/100)].tileType == 4)
            if hasUp and not hasWater:
                hasWater = (tileMap[(int)(building.x/100)][(int)((building.y/100)-1)].tileType == 4)
            if hasDown and not hasWater:
                hasWater = (tileMap[(int)((building.x/100))][(int)((building.y/100)+1)].tileType == 4)
            
            if hasWater:
                for i in range(len(self.buildings)):
                    if (m.fabs(self.buildings[i].x-building.x)/100==1 and self.buildings[i].y/100==building.y/100) or (m.fabs(self.buildings[i].y-building.y)/100==1 and self.buildings[i].x/100==building.x/100):
                        return True
            else:
                return False
        
        for i in range(len(self.buildings)):
            if (m.fabs(self.buildings[i].x-building.x)/100==1 and self.buildings[i].y/100==building.y/100) or (m.fabs(self.buildings[i].y-building.y)/100==1 and self.buildings[i].x/100==building.x/100):
                return True
        return False

    def addResourcesToCache(self, terrain):
        for i in range (len(self.buildings)):
            if self.buildings[i].buildingType == 0 or self.buildings[i].buildingType == 1 or self.buildings[i].buildingType == 2:
                self.playerFood = self.playerFood + self.buildings[i].productionRate
            if self.buildings[i].buildingType == 3 and not terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood == 0:
                self.playerWood = self.playerWood + self.buildings[i].productionRate
            if self.buildings[i].buildingType == 4 and not terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone == 0:
                self.playerStone = self.playerStone + self.buildings[i].productionRate
            if self.buildings[i].buildingType == 5 and not terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].ore == 0:
                self.playerOre = self.playerOre + self.buildings[i].productionRate
        
    def popConsumeFood(self):
        self.playerFood = self.playerFood - self.playerCurPop

    def subtractResourceFromTile(self, terrain):
        
        for i in range (len(self.buildings)):
            if self.buildings[i].buildingType == 3 and terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood >= self.buildings[i].productionRate:
                terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood = terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood - self.buildings[i].productionRate
            if terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood < self.buildings[i].productionRate:
                self.playerWood = self.playerWood + terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood
                terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].wood = 0

            if self.buildings[i].buildingType == 4 and terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone >= self.buildings[i].productionRate:
                terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone = terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone - self.buildings[i].productionRate
            if terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone < self.buildings[i].productionRate:
                self.playerStone = self.playerStone + terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone
                terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone = 0

            if self.buildings[i].buildingType == 5 and terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].ore >= self.buildings[i].productionRate:
                terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].ore = terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].ore - self.buildings[i].productionRate
            if terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].stone < self.buildings[i].productionRate:
                self.playerOre = self.playerOre + terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].ore
                terrain.board[m.floor(self.buildings[i].x/100)][m.floor(self.buildings[i].y/100)].ore = 0