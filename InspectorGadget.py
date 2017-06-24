import pygame as pg, math, Terrain

class Inspector:

    def __init__(self):
        pass

    def inspectTile(self, board, x, y):
        self.tile_x = x
        self.tile_y = y
        currentTile = board[self.tile_x][self.tile_y]
        return currentTile.tileType, currentTile.wood, currentTile.stone, currentTile.ore
"""
Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go

Inspector Gadget
Whoo-hoo
Inspector Gadget

Inspector Gadget
Whoo-hoo
Inspector Gadget

Go Gadget go
Go Gadget go

Inspector Gadget
Who-hoo
Inspector Gadget

Go Gadget go
"""