from pygame.locals import *
import pygame as pg, eztext, sys, time

class Main_Menu:

    def __init__(self):
        # Screen Settings
        self.width = 800
        self.height = 800
        self.startscreen = pg.display.set_mode((self.width, self.height))
        self.background = pg.Surface(self.startscreen.get_size())
        self.background = self.background.convert()
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
        # Game Screen
        self.title_width = None
        self.tile_height = None
        # Keys Pressed
        self.keys = []
        # Title
        self.title = pg.image.load("Images/beyersdorfTitle.png")
        self.title = pg.transform.scale(self.title, (533, 133))
        # Info Text
        self.font = pg.font.Font("OptimusPrinceps.ttf", 30)
        self.text1 = self.font.render("Welcome to Beyersdörf!", 1, pg.Color("Black"))
        self.text2 = self.font.render("Beyersdörf is a tile based strategy game.", 1, pg.Color("Black"))
        self.text3 = self.font.render("The object of the game is to destroy the enemies base.", 1, pg.Color("Black"))
        self.text4 = self.font.render("Gather resources by building buildings on tiles.", 1, pg.Color("Black"))
        self.text5 = self.font.render("Use resources to build other buildings and create you empire.", 1, pg.Color("Black"))
        self.text6 = self.font.render("Control the board and push into your enemies territory.", 1, pg.Color("Black"))
        self.text7 = self.font.render("Take down thier base to win the game.", 1, pg.Color("Black"))
        self.text8 = self.font.render("Good Luck!", 1, pg.Color("Black"))
        self.text9 = self.font.render("(Press Enter to start the game)", 1, pg.Color("Black"))

    def runScreen(self):
        pg.init()
        pg.font.init()
        # textBox = eztext.Input(maxlength=45, color=(0,0,0), prompt="Board Size: ")
        while True:
            self.clock.tick(10)
            events = pg.event.get()
            key = pg.key.get_pressed()
            if key[pg.K_RETURN]:
                break
            for event in events:
                if event.type == pg.QUIT:
                    sys.exit()
            self.startscreen.fill(self.screen_color)
            self.startscreen.blit(self.title, (133, 50))
            self.startscreen.blit(self.text1, (50,200))
            self.startscreen.blit(self.text2, (50,230))
            self.startscreen.blit(self.text3, (50,260))
            self.startscreen.blit(self.text4, (50,290))
            self.startscreen.blit(self.text5, (50,320))
            self.startscreen.blit(self.text6, (50,350))
            self.startscreen.blit(self.text7, (50,380))
            self.startscreen.blit(self.text8, (50,410))
            self.startscreen.blit(self.text9, (50,470))
            pg.display.update()