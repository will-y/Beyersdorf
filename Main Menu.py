from pygame.locals import *
import pygame as pg, eztext, sys

class Main_Menu:

    def __init__(self):
        # Screen Settings
        self.width = 800
        self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height))
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen_color = (255,255,255)
        self.clock = pg.time.Clock()
        # Font
        self.font = pg.font.SysFont("monospace", 50)
        # Game Screen
        self.title_width = None
        self.tile_height = None
    
    def ask(self, screen, question):
      pass  

    def runScreen(self):
        pg.init()
        textBox = eztext.Input(maxlength=45, color=(0,0,0), prompt="Board Size: ")
        while True:
            self.clock.tick(30)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    sys.exit()
            self.screen.fill(self.screen_color)
            textBox.update(events)
            textBox.draw(self.screen)
            pg.display.update()
            print(events)

def main():
    pg.init()
    my_game = Main_Menu()
    my_game.runScreen()

main()