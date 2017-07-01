import math
import pygame as pg
import time

class DamageHandler():

    def __init__(self):
        self.shouldFire = False

    def manageDamageDelt(self, x, y, playerAttacking, playerDefending, terrain):
        #switch to targeting mode
        #if player clicks on enemy tile to attack
        if terrain.board[x][y].builtOn == True:
                for i in range(len(playerDefending.buildings)):
                    if math.floor(playerDefending.buildings[i].x/100) == math.floor(x):
                        if math.floor(playerDefending.buildings[i].y/100) == math.floor(y):
                            if (math.fabs(math.floor(self.attacker.x/100) - x) + math.fabs(math.floor(self.attacker.y/100) - y)) <= self.attacker.range:
                                if self.shouldFire == True:
                                    self.defender = playerDefending.buildings[i]
                                    self.defender.takeDamage(self.Damage, terrain, playerDefending, self.defender)
                                    self.shouldFire = False
                                    return True
                            else:
                                pass

    def findShooter(self, xCoord, yCoord, playerAttacking, playerDefending,terrain):
        if terrain.board[xCoord][yCoord].builtOn == True:
            for b in range(len(playerAttacking.buildings)):
                if math.floor(playerAttacking.buildings[b].x/100) == math.floor(xCoord):
                    if math.floor(playerAttacking.buildings[b].y/100) == math.floor(yCoord):
                        if terrain.board[xCoord][yCoord].builtOn == True:
                            if playerAttacking.buildings[b].canFire == True:
                                self.attacker = playerAttacking.buildings[b]
                                self.Damage = self.attacker.damage
                                self.shouldFire = True
