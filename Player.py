import math

"""Player class keeps track of that players wood, stone, ore, and food stores"""
class Player():
    def __init__(self):
        self.playerWood = 0
        self.playerStone = 0
        self.playerOre = 0
        self.playerFood = 0        
        
    def setWood(self,theWood):
        self.playerWood=theWood
    def editWood(self,theWood):
        self.playerWood+=theWood

    def setStone(self,theStone):
        self.playerStone=theStone
    def editStone(self,theStone):
        self.playerStone+=theStone

    def setOre(self,theOre):
        self.playerOre=theOre
    def editOre(self,theOre):
        self.playerOre+=theOre

    def setFood(self,theFood):
        self.playerFood=theFood
    def editWood(self,theFood):
        self.playerFood+=theFood