import pygame as pg, sys, time, ctypes, math

class Main_Menu:

    def __init__(self):
        # Screen Settings
        self.width = ctypes.windll.user32.GetSystemMetrics(0)
        self.height = ctypes.windll.user32.GetSystemMetrics(0)
        self.startscreen = pg.display.set_mode((self.width, self.height),pg.NOFRAME)
        pg.display.set_caption("Beyersdörf")
        self.background = pg.Surface(self.startscreen.get_size())
        self.background = self.background.convert()
        self.screen_color = (128, 0, 0)
        self.clock = pg.time.Clock()
        # Title
        self.titleWidth = math.floor(self.width*0.5)
        self.titleHeight = math.floor(self.height*0.15)
        self.title = pg.image.load("Images/beyersdorfTitle.png")
        self.title = pg.transform.scale(self.title, (self.titleWidth, self.titleHeight))
        # Info Text
        self.textWidth = math.floor(self.width*0.45)
        self.textHeight = math.floor(self.height*0.3)
        self.text = pg.image.load("Images/mainmenuText.png")
        self.text = pg.transform.scale(self.text, (self.textWidth, self.textHeight))

    def runScreen(self):
        '''Starts the main menu screen'''
        pg.init()
        self.startscreen.fill(self.screen_color)
        self.startscreen.blit(self.title, (math.floor(self.width/2-self.titleWidth/2), math.floor(self.height*0.07)))
        self.startscreen.blit(self.text,  (math.floor(self.width/2-self.textWidth/2), math.floor(self.titleHeight+self.height*0.07+10)))
        pg.display.update()
        while True:
            self.clock.tick(10)
            events = pg.event.get()
            key = pg.key.get_pressed()
            for event in events: #If X is clicked, don't crash the window.
                if event.type == pg.QUIT:
                    sys.exit()
            if key[pg.K_RETURN]: #If Return key is pressed, start game.
                break