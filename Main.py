import pygame as pg, sys, Health, Terrain, math, UserInterface, MainMenu

class Main():
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))
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
        main_menu = MainMenu.Main_Menu()
        main_menu.runScreen()
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))
        self.screen.fill(pg.Color('white'))
        # main_menu.width = self.width
        terrainobject = Terrain.Terrain(10, self.width)
        terrainobject.generateBoard(self.screen)
        userInterface = UserInterface.UserInterface(self.screen)
        userInterface.drawInterface()
        
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