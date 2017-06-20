import pygame as pg
import time
import math

"""Makes the world as we know it"""
class Terrain():

    def __init__(self, boardNum, screenWidth, screen):
        self.boardNum = boardNum
        self.screenWidth = screenWidth
        self.tileWidth = screenWidth/boardNum
        self.board = []

    def generate_board(self):
        for i in range(self.boardNum):
            row = []
            for j in range(self.boardNum):
                tile = GenerateTile(0)
                row.append(tile.generate_tile(i,j,self.tileWidth))
            self.board.append(row)