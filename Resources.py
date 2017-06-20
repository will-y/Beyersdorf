import math
import time

class Resources():
    def __init__(self,type,amount):
        self.type = type #TYPE OF RESOURCE IE: WOOD, STONE, IRON, etc
        self.amount = amount
    
    def stuff(self,theAmount): #ADDS RESOURCES TO AMOUNT STORED AS THE CURRENT RESOURCE
        self.amount+=theAmount