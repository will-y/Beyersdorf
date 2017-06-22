import pygame as pg, math, Terrain

class Inspector:

    def __init__(self):
        pass

    def inspectTile(self, board, x, y):
        tile_x = x - 1
        tile_y = y - 1
        currentTile = board[self.tile_x][self.tile_y]
        print(currentTile)