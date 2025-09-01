import pygame
import random

pygame.init ()

background = pygame.image.load ('images/background.png')
bird = pygame.image.load ('images/bird.png')
base = pygame.image.load ('images/base.png')
gameover = pygame.image.load ('images/gameover.png')
tubeDown = pygame.image.load ('images/tube.png')
tubeUp = pygame.transform.flip (tubeDown, False, True)
icon = pygame.image.load('images/icon.ico')

window = pygame.display.set_mode ((288,512))
fps = 60
vel_avaz = 3
font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

class tubeClass:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
    def goAndWrite(self):
        self.x -= vel_avaz
        window.blit(tubeDown, (self.x, self.y+210))
        window.blit(tubeUp, (self.x, self.y-210))
    def collisions(self, bird, birdx, birdy):
        tollerence = 5
        birdLateDx = birdx+bird.get_width()-tollerence
        birdLateSx = birdx+tollerence
        tubeLateDx = self.x + tubeDown.get_width()
        tubeLateSx = self.x
        birdLateDown = birdy+bird.get_width()-tollerence
        birdLateUp = birdy+tollerence
        tubeLateUp = self.y+110
        tubeLateDown = self.y+210
        if birdLateDx > tubeLateSx and birdLateSx < tubeLateDx:
            if birdLateUp < tubeLateUp or birdLateDown > tubeLateDown:
                GameOver()
    def inTubes(self, bird, birdx):
                    tollerence = 5
                    birdLateDx = birdx+bird.get_width()-tollerence
                    birdLateSx = birdx+tollerence
                    tubeLateDx = self.x + tubeDown.get_width()
                    tubeLateSx = self.x
                    if birdLateDx > tubeLateSx and birdLateSx < tubeLateDx:
                        return True

def writeThings ():
    window.blit(background, (0,0))
    for t in tubes:
        t.goAndWrite()
    window.blit(bird, (birdx,birdy))
    window.blit(base, (basex, 400))
    puntiRender = font.render(str(punti), 1, (255,255,255))
    window.blit(puntiRender, (144,0))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def iniliate ():
    global birdx, birdy, birdVelY
    global basex
    global tubes
    global punti
    global inTubes
    birdx, birdy = 60, 150
    birdVelY = 0
    basex = 0
    tubes = []
    tubes.append(tubeClass())
    punti = 0
    inTubes = False
    pygame.display.set_caption('Flappy Bird')
    pygame.display.set_icon(icon)

def GameOver():
    window.blit(gameover, (50,180))
    update()
    restart = False
    while not restart:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
            if ( event.type == pygame.KEYDOWN 
            and event.key == pygame.K_LALT):
                iniliate()
                restart = True


iniliate ()

while True:
    basex -= vel_avaz
    if basex < -45: basex = 0
    birdVelY += 1
    birdy += birdVelY
    for event in pygame.event.get ():
        if ( event.type == pygame.KEYDOWN 
            and event.key == pygame.K_SPACE):
            birdVelY = -10
        if event.type == pygame.QUIT:
            pygame.quit ()
    if tubes[-1].x < 100: tubes.append(tubeClass())
    for t in tubes:
        t.collisions(bird, birdx, birdy) 
    if not inTubes:
        for t in tubes:
            if t.inTubes(bird, birdx):
                inTubes = True
                break
    if inTubes:
        inTubes = False
        for t in tubes:
            if t.inTubes(bird, birdx):
                inTubes = True
                break
        if not inTubes:
            punti += 1
    if birdy > 390:
        GameOver()
    writeThings ()
    update ()