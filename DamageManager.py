import math
import pygame as pg
import time

class DamageHandler():

    def __init__(self):
        self.needToDealDam = False
        # self.shooter = None
        # self.receiver = None
        0

    def manageDamageDelt(self, x, y, playerAttacking, playerDefending, terrain):
        #switch to targeting mode
        #if player clicks on enemy tile to attack
        if not math.floor(self.shooter.x/100) == x and not math.floor(self.shooter.y/100) == y:
            print("found building")

            if terrain.board[self.xint][self.yint].builtOn == True:

                for i in range(len(playerDefending.buildings)):

                    #if target is opponents tile
                    if math.floor(playerDefending.buildings[i].x/100) == math.floor(self.xint): 

                        if math.floor(playerDefending.buildings[i].y/100) == math.floor(self.yint):
                            if (math.fabs(self.xCoord - (x/100)) + math.fabs(self.yCoord - (y/100))) <= self.shooter.range:
                                print("found enemy")
                                self.receiver = playerDefending.buildings[i]
                                print(self.receiver)
                                self.Damage = self.shooter.damage
                                print(self.Damage)
                                self.receiver.takeDamage(self.Damage, terrain)
                                self.needToDealDam = False


    def findShooter(self, xCoord, yCoord, playerAttacking, playerDefending,terrain):
        self.xCoord =xCoord
        self.yCoord = yCoord
        if terrain.board[xCoord][yCoord].builtOn == True:

            for b in range(len(playerAttacking.buildings)):

                #if clicked on a fireable building
                if math.floor(playerAttacking.buildings[b].x/100) == math.floor(xCoord): 

                    if math.floor(playerAttacking.buildings[b].y/100) == math.floor(yCoord):

                        if terrain.board[xCoord][yCoord].builtOn == True:

                            if playerAttacking.buildings[b].canFire == True:

                                self.shooter = playerAttacking.buildings[b]
                                print("clicked on a building")
                                self.needToDealDam = True
                                print(str(self.needToDealDam) + "here")
