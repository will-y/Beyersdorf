import math
import time

"""Class resource takes in a type of resource and the amount it has to store"""
class Resource():
    def __init__(self,type,amount):
        self.type = type
        self.amount = amount
    """Edits the amount of the resource that it is currently holding"""
    def edit(self,theAmount):
        self.amount+=theAmount
    """Overwrites the current # of resources ont he tile"""
    def set(self,theAmount):
        self.amount=theAmount