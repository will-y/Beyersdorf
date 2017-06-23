import pygame as pg, math

class Manager:

    def __init__(self):
        self.playerOneTurn = True
        self.playerOneActions = 1
        self.playerTwoActions = 1
        self.playerOneActionsUsed = 0
        self.playerTwoActionsUsed = 0

    def addActionToPlayer(self, player):
        if player == 1:
            self.playerOneActions = self.playerOneActions + 1
        if player == 2:
            self.playerTwoActions = self.playerTwoActions + 1

    def useAction(self, player):
        if player == 1:
            self.playerOneActionsUsed = self.playerOneActionsUsed + 1
        if player == 2:
            self.playerTwoActionsUsed = self.playertwoActionsUsed + 1

    def endTurn(self):
        if self.playerOneTurn == True:
            self.playerOneTurn = False
            self.playerTwoActionsUsed = 0
            print("Player Two Turn Starts!")
        if self.playerOneTurn == False:
            self.playerOneTurn = True
            self.playerOneActionsUsed = 0
            print("Player One Turn Starts!")