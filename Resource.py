import math
import time

class Resource():
    def __init__(self,type,amount):
        self.type = type #TYPE OF RESOURCE IE: WOOD, STONE, IRON, etc
        self.amount = amount
    
    def edit(self,theAmount): #ADDS RESOURCES TO AMOUNT STORED AS THE CURRENT RESOURCE
        self.amount+=theAmount