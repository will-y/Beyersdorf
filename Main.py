import pygame as pg, sys, Health, Terrain, math, UserInterface, MainMenu, Buildings, Player

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
        self.tilesize = 100

    def changeResources(self, player):
        player.editWood(-self.building.woodCost)
        player.editStone(-self.building.stoneCost)
        player.editOre(-self.building.oreCost)

    def detectClick(self, boardCoords):
        #for event in pg.event.get():
        if(pg.mouse.get_pressed()[0]):
            if(boardCoords):
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)
                if self.xCoord <= 9:
                    self.building = Buildings.Building(0, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen)
                    self.changeResources(self.player1)
                    string = str.format("{} {} {}", self.player1.playerWood, self.player1.playerStone, self.player1.playerOre)
                    self.userInterface.updateResources(self.player1)
                    print(string)
                    sys.stdout.flush()
                return (self.xCoord, self.yCoord)
            else:
                return pg.mouse.get_pos() 

    def runGame(self):
        self.player1 = Player.Player()
        self.player2 = Player.Player()
        #main_menu = MainMenu.Main_Menu()
        #main_menu.runScreen()
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))
        self.screen.fill(pg.Color('white'))
        # main_menu.width = self.width
        terrainobject = Terrain.Terrain(10, self.width)
        terrainobject.generateBoard(self.screen)
        self.userInterface = UserInterface.UserInterface(self.screen)
        self.userInterface.drawInterface()
        self.userInterface.drawResourceBuildings()
        
        
        while(True):
            self.clock.tick(10)
            
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()
            pg.mouse.set_cursor(*pg.cursors.broken_x)
            pg.display.update()
            self.detectClick(True)
            self.userInterface.detectTabChange(0)
            self.userInterface.detectTabChange(1)
            #sys.stdout.flush()

def main():
    pg.init()
    main = Main()
    main.runGame()

main()