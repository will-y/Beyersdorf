import pygame as pg
import sys
import Health
import Terrain

class Main():
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.screen = pg.display.set_mode((self.width, self.height))
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill(pg.Color('white'))
        self.clock = pg.time.Clock()
        self.xCoord = 0
        self.yCoord = 0

    def detectClick(self):
        #for event in pg.event.get():
        if(pg.mouse.get_pressed()[0]):
            self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
            self.yCoord = (int)(pg.mouse.get_pos()[1]/100)

            return (self.xCoord, self.yCoord)

    def runGame(self):
        terrainobject = Terrain.Terrain(10, self.width)
        terrainobject.generate_board(self.screen)
        
        while(True):
            self.clock.tick(10)
            
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()
            pg.mouse.set_cursor(*pg.cursors.broken_x)
            pg.display.update()
            #print(self.detectClick())
            #sys.stdout.flush()

def main():
    pg.init()
    main = Main()
    main.runGame()

main()