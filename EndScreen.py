import pygame as pg, InspectorGadget as god, sys

class End_Screen:

    def __init__(self, winner):
        pg.font.init()
        # Screen Settings
        self.width = 800
        self.height = 800
        self.endscreen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Beyersdörf")
        self.background = pg.Surface(self.endscreen.get_size())
        self.background = self.background.convert()
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
        # Info Text
        self.bigfont = pg.font.Font("OptimusPrinceps.ttf", 60)
        self.font = pg.font.Font("OptimusPrinceps.ttf", 30)
        self.text1 = self.bigfont.render(winner + " is Victorious!", 1, pg.Color("Black"))
        self.text2 = self.font.render(winner + " was able outsmart their opponent and", 1, pg.Color("Black"))
        self.text3 = self.font.render("destroy their castle. The land of Beyersdörf is", 1, pg.Color("Black"))
        self.text4 = self.font.render("all yours now.", 1, pg.Color("Black"))
        self.text5 = self.font.render("(Press Enter to quit the game)", 1, pg.Color("Black"))
    
    def runScreen(self):
        while True:
            self.clock.tick(30)
            events = pg.event.get()
            key = pg.key.get_pressed()
            for event in events: #If X is clicked, don't crash the window.
                if event.type == pg.QUIT:
                    sys.exit()
            if key[pg.K_RETURN]: #If Return key is pressed, end game.
                break
            self.endscreen.fill(self.screen_color)
            self.endscreen.blit(self.text1, (133, 200))
            self.endscreen.blit(self.text2, (110, 280))
            self.endscreen.blit(self.text3, (110, 310))
            self.endscreen.blit(self.text4, (110, 340))
            self.endscreen.blit(self.text5, (210, 400))
            pg.display.update()


def main():
    pg.init
    endScreen = End_Screen("Player 1")
    endScreen.runScreen()

main()