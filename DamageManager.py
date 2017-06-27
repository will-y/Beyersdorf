

class Main():

    __init__(self):
        self.shooter = None
        self.reciever = None

    def findShooter(self,attackBuilding, recieveBuilding, xCoord, yCoord, player1, player2):
        if self.terrainobject.board[xCoord][yCoord].builtOn == True:

            for b in range(len(self.player1.buildings)):

                #if clicked on a fireable building
                if math.floor(self.player1.buildings[b].x/100) == math.floor(xCoord): 

                    if math.floor(self.player1.buildings[b].y/100) == math.floor(yCoord):

                        if self.terrainobject.board[xCoord][yCoord].builtOn == True:

                            if self.player1.buildings[b].canFire == True:

                                self.shooter = self.player1.buildings[b]
                                print("clicked on a building")
                                
    def manageDamageDelt(self):
        #switch to targeting mode
        while(True):

            if(pg.mouse.get_pressed()[0]):

                if(boardCoords):

                    self.realX = pg.mouse.get_pos()[0]
                    self.realY = pg.mouse.get_pos()[1]
                    self.xint = (int)(pg.mouse.get_pos()[0]/100)
                    self.yint = (int)(pg.mouse.get_pos()[1]/100)

                    if self.terrainobject.board[self.xint][self.yint].builtOn == True:

                        for i in range(len(self.player2.buildings)):

                            #if target is opponents tile
                            if math.floor(self.player2.buildings[i].x/100) == math.floor(self.xint): 

                                if math.floor(self.player2.buildings[i].y/100) == math.floor(self.yint):

                                    self.target = self.player2.buildings[i]
                                    self.Damage = self.targeter.damageF
                                    self.target.takeDamage(Damage, self.terrainobject)
                                    break