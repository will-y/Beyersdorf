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
        self.screen_color = (255,255,255)
        self.clock = pg.time.Clock()
        # Game Screen
        self.title_width = None
        self.tile_height = None
        # Keys Pressed
        self.keys = []

    def runScreen(self):
        pg.init()
        textBox = eztext.Input(maxlength=45, color=(0,0,0), prompt="Board Size: ")
        while True:
            self.clock.tick(10)
            events = pg.event.get()
            key = pg.key.get_pressed()
            # Stores the key inputs
            if key[pg.K_0]:
                self.keys.append("0")
                time.sleep(0.1)
            if key[pg.K_1]:
                self.keys.append("1")
                time.sleep(0.1)
            if key[pg.K_2]:
                self.keys.append("2")
                time.sleep(0.1)
            if key[pg.K_3]:
                self.keys.append("3")
                time.sleep(0.1)
            if key[pg.K_4]:
                self.keys.append("4")
                time.sleep(0.1)
            if key[pg.K_5]:
                self.keys.append("5")
                time.sleep(0.1)
            if key[pg.K_6]:
                self.keys.append("6")
                time.sleep(0.1)
            if key[pg.K_7]:
                self.keys.append("7")
                time.sleep(0.1)
            if key[pg.K_8]:
                self.keys.append("8")
                time.sleep(0.1)
            if key[pg.K_9]:
                self.keys.append("9")
                time.sleep(0.1)
            if key[pg.K_RETURN]:
                # self.startscreen.fill(self.screen_color)
                # sys.exit()
                break
            for event in events:
                if event.type == pg.QUIT:
                    sys.exit()
            self.startscreen.fill(self.screen_color)
            textBox.update(events)
            textBox.draw(self.startscreen)
            pg.display.update()