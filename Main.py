import pygame as pg
import sys, Health, Terrain, math, UserInterface, MainMenu, Buildings, Player, InspectorGadget, TurnManager

class Main():
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))
        pg.display.set_caption("Beyersdörf")
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
        if player == 1:
            if self.player1.canBuy(-self.building.woodCost, -self.building.stoneCost, -self.building.oreCost, self.building.populationCost):
                self.player1.editWood(-self.building.woodCost)
                self.player1.editStone(-self.building.stoneCost)
                self.player1.editOre(-self.building.oreCost)
                self.player1.editCurPop(self.building.populationCost)
                return True
        if player == 2:
            if self.player2.canBuy(-self.building.woodCost, -self.building.stoneCost, -self.building.oreCost, self.building.populationCost):
                self.player2.editWood(-self.building.woodCost)
                self.player2.editStone(-self.building.stoneCost)
                self.player2.editOre(-self.building.oreCost)
                self.player2.editCurPop(self.building.populationCost)
                return True

    def detectClick(self, boardCoords, turnManager):
        #for event in pg.event.get():
        if(pg.mouse.get_pressed()[0]):
            if(boardCoords):
                self.realX = pg.mouse.get_pos()[0]
                self.realY = pg.mouse.get_pos()[1]
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)

                if self.realX >= 1200 and self.realX <= 1300 and self.realY >= 350 and self.realY <= 450:
                    if turnManager.playerOneTurn == True:
                        turnManager.endTurn(self.player1)

                    elif turnManager.playerOneTurn == False:
                        turnManager.endTurn(self.player2)
                
                #If click is outside UI
                if self.xCoord <= 9:

                
                    if (not self.userInterface.inspector):
                        self.inspect.inspectTile(self.terrainobject.board, self.xCoord, self.yCoord)

                        #If tile is already built on
                        if self.terrainobject.board[self.xCoord][self.yCoord].builtOn == False:

                            #if not on water or bridge
                            if (not self.terrainobject.board[self.xCoord][self.yCoord].tileType == 4) or self.selectedBuilding == 9:

                                    #if it is correct player's turn and they have enough actions
                                    if turnManager.playerOneTurn == True and not turnManager.playerOneActions == turnManager.playerOneActionsUsed:
                                        self.building = Buildings.Building(self.selectedBuilding, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen,1)

                                        if self.player1.canBuild(self.building):

                                            #if player have resources to build
                                            if self.changeResources(1):
                                                self.building.drawBuilding(1)
                                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                                                turnManager.useAction(1)
                                                self.player1.addBuilding(self.building)

                                    if turnManager.playerOneTurn == False and not turnManager.playerTwoActions == turnManager.playerTwoActionsUsed:

                                        self.building = Buildings.Building(self.selectedBuilding, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen,2)
                                        if self.player2.canBuild(self.building):

                                            #if player have resources to build
                                            if self.changeResources(2):
                                                self.building.drawBuilding(2)
                                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                                                turnManager.useAction(2)
                                                self.player2.addBuilding(self.building)

                        string = str.format("{} {} {}", self.player1.playerWood, self.player1.playerStone, self.player1.playerOre)
                        self.userInterface.updateResources(self.player1)
                        # print(string)
                        sys.stdout.flush()
                    else:
                        self.userInterface.updateInspector(self.xCoord, self.yCoord, self.terrainobject.board)

                else:
                    #if click button
                    if(1050 < self.realX < 1450):
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
                    self.userInterface.switchSelectedBuilding(self.selectedBuilding)
                    sys.stdout.flush()
                    return (self.xCoord, self.yCoord)
            else:
                return pg.mouse.get_pos() 

    def runGame(self):
        self.main_menu = MainMenu.Main_Menu()
        self.main_menu.runScreen()
        turnManager = TurnManager.Manager()
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height))
        self.screen.fill(pg.Color('white'))
        
        # main_menu.width = self.width
        self.userInterface = UserInterface.UserInterface(self.screen)
        self.terrainobject = Terrain.Terrain(10, self.width, self.tilesize)
        self.terrainobject.generateBoard(self.screen)
        
        self.building = Buildings.Building(10, 1*self.tilesize, 1*self.tilesize, self.tilesize, self.screen,1)
        self.building.drawBuilding(1)
        self.player1.buildings.append(self.building)
        self.building = Buildings.Building(10, 8*self.tilesize, 8*self.tilesize, self.tilesize, self.screen,2)
        self.building.drawBuilding(2)
        self.player2.buildings.append(self.building)
        print(self.player1.buildings[0])
        
        self.userInterface.drawInterface()
        self.userInterface.drawResourceBuildings()
        pg.draw.rect(self.screen, pg.Color('black'), (0, 0, 1000, 1000), 5)
        
        file = 'Sound/Music2.wav'
        pg.mixer.init()
        pg.mixer.music.load(file)
        pg.mixer.music.play(-1)

        while(True):
            self.clock.tick(10)
            
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()
            pg.mouse.set_cursor(*pg.cursors.broken_x)
            pg.display.update()
            self.detectClick(True, turnManager)
            self.userInterface.detectTabChange(0)
            self.userInterface.detectTabChange(1)
            #sys.stdout.flush()

def main():
    pg.init()
    main = Main()
    main.runGame()

main()