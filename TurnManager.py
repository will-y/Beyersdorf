import pygame as pg, math

class Manager:

    def __init__(self):
        self.playerOneTurn = True
        self.playerOneActions = 4
        self.playerTwoActions = 4
        self.playerOneActionsUsed = 0
        self.playerTwoActionsUsed = 0

    def addActionToPlayer(self, player):
        """Adds and extra action per turn to a specified player"""
        if player == 1:
            self.playerOneActions = self.playerOneActions + 1
        if player == 2:
            self.playerTwoActions = self.playerTwoActions + 1

    def useAction(self, player):
        """Uses an action per turn"""
        if player == 1:
            self.playerOneActionsUsed = self.playerOneActionsUsed + 1
        if player == 2:
            self.playerTwoActionsUsed = self.playerTwoActionsUsed + 1

    def endTurn(self):
        """Ends the current players turn"""
        if self.playerOneTurn == True:
            self.playerOneTurn = False
            self.playerTwoActionsUsed = 0
            # print("Player Two Turn Starts!")
        else:
            self.playerOneTurn == False
            self.playerOneTurn = True
            self.playerOneActionsUsed = 0
            # print("Player One Turn Starts!")