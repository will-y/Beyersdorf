import math

"""Player class keeps track of that players wood, stone, ore, and food stores"""
class Player():
    def __init__(self):
        self.playerWood = 0
        self.playerStone = 0
        self.playerOre = 0
        self.playerFood = 0
        self.playerCurPop = 0
        self.playerMaxPop = 0
        
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
    def editWood(self,amount):
        self.playerFood+=amount

    def setCurPop(self,amount):
        self.playerCurPop=amount
    def editCurPop(self,theFood):
        self.playerCurPop+=amount

    def setMaxPop(self,amount):
        self.playerMaxPop=amount
    def setCurPop(self,amount):
        self.playerMaxPop+=amount