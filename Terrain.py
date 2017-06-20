import pygame as pg
import time
import math

"""Makes the world as we know it"""
class Terrain():

    def __init__(self, boardNum, screenWidth, screen):
        self.boardNum = boardNum
        self.screenWidth = screenWidth
        self.tileWidth = screenWidth/boardNum

    def generate_board(self):
        board = []
        for i in range(self.boardNum):
            row = []
            for j in range(boardSize):
                row.append(GenerateTile.)
            board.append(row)

class GenerateTile:

    def __init__(self, tileType,):
        self.tileType = tileType
        self.tileResource1
        self.tileResource2
        self.tileResource3

    def generate_tile(self):