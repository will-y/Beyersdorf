import math

"""Player class keeps track of that players wood, stone, ore, and food stores"""
class Player():
    def __init__(self):
        self.team = 0
        self.playerWood = 1000
        self.playerStone = 200
        self.playerOre = 100
        self.playerFood = 0
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
    def setCurPop(self,amount):
        self.playerMaxPop+=amount
    
    def addBuilding(self,building):
        self.buildings.append(building)
        print(self.buildings)

    def canBuild(self,building):
        for i in range(len(self.buldings)):
            if building.x+1 == self.buildings[i].x or building.x-1 == self.buildings[i].x or building.y+1 == self.buildings[i].y or building.y-1 == self.buldings[i].y:
                return True
        return False