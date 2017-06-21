import pygame as pg, time, math, TileCreate as tc

"""Makes the world as we know it"""
class Terrain():

    def __init__(self, boardNum, screenWidth):
        self.boardNum = boardNum
        self.screenWidth = screenWidth
        self.tileWidth = math.floor(self.screenWidth/self.boardNum)
        self.board = []

    def generateBoard(self, screen):
        for i in range(self.boardNum):
            row = []
            for j in range(self.boardNum):
                tile = tc.GenerateTile(0)
                row.append(tile.generate_tile(i,j,self.tileWidth, screen))
            self.board.append(row)

        print(self.board)
        return self.board