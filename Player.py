import math

"""Player class keeps track of that players wood, stone, ore, and food stores"""
class Player():
    def __init__(self):
        self.team = 0
        self.playerWood = 1000
        self.playerStone = 1000
        self.playerOre = 100
        self.playerFood = 0
        self.playerCurPop = 0
        self.playerMaxPop = 0
        
    def setWood(self,amount):
        self.playerWood=amount
    def editWood(self,amount):
        if self.playerWood + amount < 0:
            return False 
        self.playerWood+=amount
        return True

    def setStone(self,amount):
        self.playerStone=amount
    def editStone(self,amount):
        if self.playerStone + amount < 0:
            return False 
        self.playerStone+=amount
        return True
        self.playerStone+=amount

    def setOre(self,amount):
        self.playerOre=amount
    def editOre(self,amount):
        self.playerOre+=amount
        if self.playerOre + amount < 0:
            return False 
        self.playerOre+=amount
        return True

    def setFood(self,amount):
        self.playerFood=amount
    def editFood(self,amount):
        self.playerFood+=amount

    def setCurPop(self,amount):
        self.playerCurPop=amount
    def editCurPop(self,theFood):
        self.playerCurPop+=amount

    def setMaxPop(self,amount):
        self.playerMaxPop=amount
    def setCurPop(self,amount):
        self.playerMaxPop+=amount