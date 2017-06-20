import pygame as pg
import sys

class Main():
    def __init__(self):
        self.width = 1024
        self.height = 1024
        self.screen = pg.display.set_mode((self.width, self.height))
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill(pg.Color('white'))
        self.clock = pg.time.Clock()

    def runGame(self):
        while(True):
            self.clock.tick(10)

            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()
            pg.mouse.set_cursor(*pg.cursors.broken_x)
            pg.display.update()

def main():
    pg.init()
    main = Main()
    main.runGame()

main()