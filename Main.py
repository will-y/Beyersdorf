import pygame as pg
import sys, Health, Terrain, math, UserInterface, MainMenu, Buildings, Player, InspectorGadget, TurnManager,time

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
                self.player1.editMaxPop(self.building.populationAdd)
                return True
        if player == 2:
            if self.player2.canBuy(-self.building.woodCost, -self.building.stoneCost, -self.building.oreCost, self.building.populationCost):
                self.player2.editWood(-self.building.woodCost)
                self.player2.editStone(-self.building.stoneCost)
                self.player2.editOre(-self.building.oreCost)
                self.player2.editCurPop(self.building.populationCost)
                self.player2.editMaxPop(self.building.populationAdd)
                return True

    def detectClick(self, boardCoords, turnManager):
        #for event in pg.event.get():
        if(pg.mouse.get_pressed()[0]):
            if(boardCoords):
                self.realX = pg.mouse.get_pos()[0]
                self.realY = pg.mouse.get_pos()[1]
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)

                #End Turn Stuff
                if self.realX >= 1200 and self.realX <= 1300 and self.realY >= 350 and self.realY <= 450:
                    if turnManager.playerOneTurn == True:
                        self.player1.subtractResourceFromTile(self.terrainobject)
                        self.player1.addResourcesToCache(self.terrainobject)
                        self.player1.popConsumeFood()
                        turnManager.endTurn()
                        time.sleep(1)
                        self.userInterface.updateResources(self.player2)
                        #self.player1.buildings[1].takeDamage(20, self.terrainobject)

                    elif turnManager.playerOneTurn == False:
                        self.player2.subtractResourceFromTile(self.terrainobject)
                        self.player2.addResourcesToCache(self.terrainobject)
                        self.player2.popConsumeFood()
                        turnManager.endTurn()
                        time.sleep(1)
                        self.userInterface.updateResources(self.player1)
                
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

                                        if self.player1.canBuild(self.building,self.terrainobject.board):

                                            #if player have resources to build
                                            if self.changeResources(1):
                                                self.building.drawBuilding(1)
                                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                                                turnManager.useAction(1)
                                                self.player1.addBuilding(self.building)
                                                self.userInterface.updateResources(self.player1)

                                    if turnManager.playerOneTurn == False and not turnManager.playerTwoActions == turnManager.playerTwoActionsUsed:

                                        self.building = Buildings.Building(self.selectedBuilding, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen,2)
                                        # print('testing')
                                        if self.player2.canBuild(self.building,self.terrainobject.board):

                                            #if player have resources to build
                                            if self.changeResources(2):
                                                self.building.drawBuilding(2)
                                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                                                turnManager.useAction(2)
                                                self.player2.addBuilding(self.building)
                                                self.userInterface.updateResources(self.player2)
                        if self.terrainobject.board[self.xCoord][self.yCoord].builtOn == True:
                            for i in range(len(self.player1.buildings)):
                                print(self.xCoord)
                                print(math.floor(self.player1.buildings[i].x/100))
                                if math.floor(self.player1.buildings[i].x/100) == math.floor(self.xCoord) and math.floor(self.player1.buildings[i].y/100) == math.floor(self.yCoord) and self.terrainobject.board[self.xCoord][self.yCoord].builtOn == True and self.player1.buildings[i].canFire == True:
                                    print("clicked on a building")
                    else:
                        self.userInterface.updateInspector(self.xCoord, self.yCoord, self.terrainobject.board)

                else:
                    #if click button
                    if(1050 < self.realX < 1450):
                        if(516 < self.realY < 584):
                            if(self.userInterface.currentBuildingTab == 0):
                                self.selectedBuilding = 0
                            elif(self.userInterface.currentBuildingTab == 1):
                                self.selectedBuilding = 10
                            elif(self.userInterface.currentBuildingTab == 2):
                                self.selectedBuilding = 6
                        elif(596 < self.realY < 664):
                            if(self.userInterface.currentBuildingTab == 0):
                                self.selectedBuilding = 1
                            elif(self.userInterface.currentBuildingTab == 1):
                                self.selectedBuilding = 11
                            elif(self.userInterface.currentBuildingTab == 2):
                                self.selectedBuilding = 7
                        elif(676 < self.realY < 744):
                            if(self.userInterface.currentBuildingTab == 0):
                                self.selectedBuilding = 2
                            elif(self.userInterface.currentBuildingTab == 1):
                                self.selectedBuilding = 12
                            elif(self.userInterface.currentBuildingTab == 2):
                                self.selectedBuilding = 8
                        elif(756 < self.realY < 824):
                            if(self.userInterface.currentBuildingTab == 0):
                                self.selectedBuilding = 3
                            elif(self.userInterface.currentBuildingTab == 2):
                                self.selectedBuilding = 9
                        elif(836 < self.realY < 904):
                            if(self.userInterface.currentBuildingTab == 0):
                                self.selectedBuilding = 4
                        elif(916 < self.realY < 984):
                            if(self.userInterface.currentBuildingTab == 0):
                                self.selectedBuilding = 5
                    if(self.userInterface.currentBuildingTab == 0 and not self.userInterface.inspector):
                        self.userInterface.drawResourceBuildings(self.selectedBuilding)
                    elif(self.userInterface.currentBuildingTab == 1 and not self.userInterface.inspector):
                        self.userInterface.drawMilitaryBuildings(self.selectedBuilding)
                    elif(self.userInterface.currentBuildingTab == 2 and not self.userInterface.inspector):
                        self.userInterface.drawInfrastructureBuildings(self.selectedBuilding)
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
        self.player1.addBuilding(self.building)
        self.terrainobject.board[1][1].builtOn = True

        self.building = Buildings.Building(10, 8*self.tilesize, 8*self.tilesize, self.tilesize, self.screen,2)
        self.building.drawBuilding(2)
        self.player2.addBuilding(self.building)
        self.terrainobject.board[8][8].builtOn = True

        
        self.userInterface.drawInterface()
        #self.userInterface.drawResourceBuildings()
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