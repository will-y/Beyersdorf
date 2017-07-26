import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
import pygame as pg, sys, math, time, ctypes
from source import MainMenu, EndScreen, UserInterface, Terrain, TileCreate, Health, Buildings, Player, InspectorGadget, TurnManager, DamageManager

class Main():

    def __init__(self):
        # Screen Size
        self.width = 1000
        self.height = 1000
        # Tile Size
        self.tilesize = 100
        # Creates the game clock
        self.clock = pg.time.Clock()
        self.xCoord = 0
        self.yCoord = 0
        # Initilizes Inspector
        self.inspect = InspectorGadget.Inspector()
        # Initilizes Player objects
        self.player1 = Player.Player()
        self.player2 = Player.Player()
        self.selectedBuilding = 0
        # Sound Settings
        self.sounds = []
        self.farmSound = pg.mixer.Sound('Sound/FarmSound.wav')
        self.ranchSound = pg.mixer.Sound('Sound/RanchSound.wav')
        self.fishSound = pg.mixer.Sound('Sound/MineSound.wav')
        self.lumberSound = pg.mixer.Sound('Sound/LumberSound.wav')
        self.quarrySound = pg.mixer.Sound('Sound/MineSound.wav')
        self.mineSound = pg.mixer.Sound('Sound/MineSound.wav')
        self.houseSound = pg.mixer.Sound('Sound/MineSound.wav')
        self.townSound = pg.mixer.Sound('Sound/MineSound.wav')
        self.citySound = pg.mixer.Sound('Sound/MineSound.wav')
        self.bridgeSound = pg.mixer.Sound('Sound/MineSound.wav')
        self.castleSound = pg.mixer.Sound('Sound/MineSound.wav')
        self.outpostSound = pg.mixer.Sound('Sound/ClangSound.wav')
        self.cannonSound = pg.mixer.Sound('Sound/ClangSound.wav')
        self.sounds.extend((self.farmSound,self.ranchSound,self.fishSound,self.lumberSound,self.quarrySound,self.mineSound,self.houseSound,self.townSound,self.citySound,self.bridgeSound,self.castleSound,self.outpostSound,self.cannonSound))

    def changeResources(self, player):
        '''Updates a player's resources'''
        if player == 1:
            if self.player1.canBuy(-self.building.woodCost, -self.building.stoneCost, -self.building.oreCost, -self.building.populationCost):
                self.player1.editWood(-self.building.woodCost)
                self.player1.editStone(-self.building.stoneCost)
                self.player1.editOre(-self.building.oreCost)
                self.player1.editCurPop(self.building.populationCost)
                self.player1.editCurPop(-self.building.populationAdd)
                self.player1.editMaxPop(self.building.populationAdd)
                return True
        if player == 2:
            if self.player2.canBuy(-self.building.woodCost, -self.building.stoneCost, -self.building.oreCost, -self.building.populationCost):
                self.player2.editWood(-self.building.woodCost)
                self.player2.editStone(-self.building.stoneCost)
                self.player2.editOre(-self.building.oreCost)
                self.player2.editCurPop(self.building.populationCost)
                self.player2.editCurPop(-self.building.populationAdd)
                self.player2.editMaxPop(self.building.populationAdd)
                return True

    def detectClick(self, boardCoords, turnManager):
        '''The worst function'''
        if(pg.mouse.get_pressed()[0]):
            if(boardCoords):
                self.realX = pg.mouse.get_pos()[0]
                self.realY = pg.mouse.get_pos()[1]
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)

                #End Turn Stuff
                if 1050 <= self.realX <= 1200 and 350 <= self.realY <= 385:
                    
                    if turnManager.playerOneTurn == True:
                        self.player1.subtractResourceFromTile(self.terrainobject)
                        self.player1.addResourcesToCache(self.terrainobject)
                        self.player1.popConsumeFood()
                        turnManager.endTurn()
                        time.sleep(1)
                        self.userInterface.updateResources(self.player2)
                        self.userInterface.switchEndTurnButton("blue")
                        self.userInterface.displayError("")

                    elif turnManager.playerOneTurn == False:
                        self.player2.subtractResourceFromTile(self.terrainobject)
                        self.player2.addResourcesToCache(self.terrainobject)
                        self.player2.popConsumeFood()
                        turnManager.endTurn()
                        time.sleep(1)
                        self.userInterface.updateResources(self.player1)
                        self.userInterface.switchEndTurnButton("red")
                        self.userInterface.displayError("")
                
                #If click is outside UI
                if self.xCoord <= 9:

                    if (not self.userInterface.inspector):
                        self.inspect.inspectTile(self.terrainobject.board, self.xCoord, self.yCoord)

                        #If tile is already built on
                        if self.terrainobject.board[self.xCoord][self.yCoord].builtOn == False:

                            #if not on water or bridge
                            if (not self.terrainobject.board[self.xCoord][self.yCoord].tileType == 4) or self.selectedBuilding == 9:
                                    if self.selectedBuilding == 9:
                                        if self.terrainobject.board[self.xCoord][self.yCoord].tileType == 4:
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
                                                        self.userInterface.displayError("")
                                                        if self.building.buildingType == 10:
                                                            turnManager.addActionToPlayer(1)
                                        else:
                                            self.userInterface.displayError("Cannot Build This Here")                    
                                    #if it is correct player's turn and they have enough actions
                                    elif turnManager.playerOneTurn == True and not turnManager.playerOneActions == turnManager.playerOneActionsUsed:

                                        self.building = Buildings.Building(self.selectedBuilding, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen,1)

                                        if self.player1.canBuild(self.building,self.terrainobject.board):

                                            #if player have resources to build
                                            if self.changeResources(1):
                                                self.building.drawBuilding(1)
                                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                                                turnManager.useAction(1)
                                                self.player1.addBuilding(self.building)
                                                self.userInterface.updateResources(self.player1)
                                                self.userInterface.displayError("")
                                                if self.building.buildingType == 10:
                                                    turnManager.addActionToPlayer(1)
                                                self.sounds[self.building.buildingType].play()
                                            else:
                                                self.userInterface.displayError("Not Enough Resources")
                                        else:
                                            self.userInterface.displayError("Cannot Build This Here")
                                    if turnManager.playerOneActions == turnManager.playerOneActionsUsed:
                                        self.userInterface.displayError("No More Actions")

                                    if turnManager.playerOneTurn == False and not turnManager.playerTwoActions == turnManager.playerTwoActionsUsed:

                                        self.building = Buildings.Building(self.selectedBuilding, self.xCoord*self.tilesize, self.yCoord*self.tilesize, self.tilesize, self.screen,2)
                                        if self.player2.canBuild(self.building,self.terrainobject.board):

                                            #if player have resources to build
                                            if self.changeResources(2):
                                                self.building.drawBuilding(2)
                                                self.terrainobject.board[self.xCoord][self.yCoord].builtOn = True
                                                turnManager.useAction(2)
                                                self.player2.addBuilding(self.building)
                                                self.userInterface.updateResources(self.player2)
                                                self.userInterface.displayError("")
                                                if self.building.buildingType == 10:
                                                    turnManager.addActionToPlayer(2)
                                                self.sounds[self.building.buildingType].play()

                                            else:
                                                self.userInterface.displayError("Not Enough Resources")
                                        else:
                                            self.userInterface.displayError("Cannot Build This Here")
                        #handles all attacking
                        elif turnManager.playerOneTurn == True and turnManager.playerOneActionsUsed < turnManager.playerOneActions:
                            self.Handler.findShooter(self.xCoord, self.yCoord, self.player1, self.player2, self.terrainobject)
                            if self.Handler.manageDamageDelt(self.xCoord, self.yCoord, self.player1, self.player2, self.terrainobject):
                                turnManager.useAction(1)
                        elif turnManager.playerOneTurn == False and turnManager.playerTwoActionsUsed < turnManager.playerTwoActions:
                            self.Handler.findShooter(self.xCoord, self.yCoord, self.player2, self.player1, self.terrainobject)
                            if self.Handler.manageDamageDelt(self.xCoord, self.yCoord, self.player2, self.player1, self.terrainobject):
                                turnManager.useAction(2)
                        else:
                            self.userInterface.displayError("No More Actions")
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
        
        if(pg.mouse.get_pressed()[2]):
            if(boardCoords):
                self.realX = pg.mouse.get_pos()[0]
                self.realY = pg.mouse.get_pos()[1]
                self.xCoord = (int)(pg.mouse.get_pos()[0]/100)
                self.yCoord = (int)(pg.mouse.get_pos()[1]/100)

    def runGame(self):
        """Runs the game"""
        # Starts the main menu
        self.main_menu = MainMenu.Main_Menu()
        self.main_menu.runScreen()
        # Sets the screen to game screen
        self.screen = pg.display.set_mode((math.floor(self.width* 3/2), self.height),pg.NOFRAME)
        # Initilizes TurnManager
        turnManager = TurnManager.Manager()
        # Initilizes UserInterface
        self.userInterface = UserInterface.UserInterface(self.screen)
        # Initilizes DamageHandler
        self.Handler = DamageManager.DamageHandler()
        # Initilizes Tiles
        self.terrainobject = Terrain.Terrain(10, self.width, self.tilesize)
        # Generates the board
        self.terrainobject.generateBoard(self.screen)
        # Spawns Player 1's Castle
        self.building = Buildings.Building(10, 1*self.tilesize, 1*self.tilesize, self.tilesize, self.screen,1)
        self.building.drawBuilding(1)
        self.player1.addBuilding(self.building)
        self.terrainobject.board[1][1].builtOn = True
        # Spawns Player 2's Castle
        self.building = Buildings.Building(10, 8*self.tilesize, 8*self.tilesize, self.tilesize, self.screen,2)
        self.building.drawBuilding(2)
        self.player2.addBuilding(self.building)
        self.terrainobject.board[8][8].builtOn = True
        # Draws UserInterface
        self.userInterface.drawInterface()
        pg.draw.rect(self.screen, pg.Color('black'), (0, 0, 1000, 1000), 5)
        # Starts game music
        file = 'Sound/Music2.wav'
        pg.mixer.init()
        pg.mixer.music.load(file)
        pg.mixer.music.play(-1)
        # Main game loop
        while(True):
            # Game clock
            self.clock.tick(10)
            key = pg.key.get_pressed()
            for event in pg.event.get():
                if(event.type == pg.QUIT): #If window is quit, doesn't crash python
                    sys.exit()
            if key[pg.K_ESCAPE]: #If Return key is pressed, start game.
                sys.exit()
            pg.mouse.set_cursor(*pg.cursors.broken_x) #Sets cursor image
            self.detectClick(True, turnManager)
            self.userInterface.getPlayer(self.player1, self.player2)
            # Detects tab change in UserInterface
            self.userInterface.detectTabChange(0)
            self.userInterface.detectTabChange(1)
            # Detects if a player's castle is destroyed
            if self.player1.buildings[0].destroyed == True or self.player1.playerFood<0:
                winner = "Player 2"
                break
            elif self.player2.buildings[0].destroyed == True or self.player2.playerFood<0:
                winner = "Player 1"
                break
            pg.display.update() #Updates the screen
        # Starts the EndScreen
        self.end_screen = EndScreen.End_Screen(winner)
        self.end_screen.runScreen()
        pg.display.update()

def main():
    pg.init()
    while True:
        main = Main()
        main.runGame()
main()