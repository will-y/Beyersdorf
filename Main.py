import pygame as pg, sys, Health, Terrain, math, UserInterface, MainMenu, Buildings, Player, InspectorGadget

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
        self.inspect = InspectorGadget.Inspector()
        self.player1 = Player.Player()
        self.player2 = Player.Player()
        self.selectedBuilding = 0

    def changeResources(self, player):
        return player.editWood(-self.building.woodCost) and player.editStone(-self.building.stoneCost) and player.editOre(-self.building.oreCost)

    def detectClick(self, boardCoords):
        #for event in pg.event.get():
        if(pg.mouse.get_pressed()[0]):
            if(boardCoords):
                self.realX = pg.mouse.get_pos()[0]
                self.realY = pg.mouse.get_pos()[1]
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)
                #If click is in UI
                if self.xCoord <= 9:
                    #If tile is already built on
                    self.inspect.inspectTile(self.terrainobject.board, self.xCoord, self.yCoord)
                    if not self.terrainobject.board[self.xCoord][self.yCoord].builtOn:
                        self.building = Buildings.Building(self.selectedBuilding, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen)
                        #if player have resources to build
                        if not self.terrainobject.board[self.xCoord][self.yCoord].tileType == 4 or self.selectedBuilding == 9:
                            if self.changeResources(self.player1):
                                self.building.drawBuilding()
                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                    string = str.format("{} {} {}", self.player1.playerWood, self.player1.playerStone, self.player1.playerOre)
                    self.userInterface.updateResources(self.player1)
                    # print(string)
                    sys.stdout.flush()
                else:
                    if(1050 < self.realX < 1450):
                        print("In Range X")
                        sys.stdout.flush()
                        if(516 < self.realY < 584):
                            self.selectedBuilding = 0
                        elif(596 < self.realY < 664):
                            self.selectedBuilding = 1
                        elif(676 < self.realY < 744):
                            self.selectedBuilding = 2
                        elif(756 < self.realY < 824):
                            self.selectedBuilding = 3
                        elif(836 < self.realY < 904):
                            self.selectedBuilding = 4
                        elif(916 < self.realY < 984):
                            self.selectedBuilding = 5
                print(self.selectedBuilding)
                sys.stdout.flush()
                return (self.xCoord, self.yCoord)
            else:
                return pg.mouse.get_pos() 

    def runGame(self):
        #main_menu = MainMenu.Main_Menu()
        #main_menu.runScreen()
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))
        self.screen.fill(pg.Color('white'))
        
        # main_menu.width = self.width
        self.terrainobject = Terrain.Terrain(10, self.width)
        self.terrainobject.generateBoard(self.screen)
        self.userInterface = UserInterface.UserInterface(self.screen)
        self.userInterface.drawInterface()
        self.userInterface.drawResourceBuildings()
        pg.draw.rect(self.screen, pg.Color('black'), (0, 0, 1000, 1000), 5)
        
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