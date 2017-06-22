import pygame as pg, math, Terrain

class Inspector:

    def __init__(self):
        pass

    def inspectTile(self, board, x, y):
        self.tile_x = x
        self.tile_y = y
        currentTile = board[self.tile_x][self.tile_y]
        # print(currentTile)
        return currentTile