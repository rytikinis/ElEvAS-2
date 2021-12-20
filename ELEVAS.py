import pygame
import sys
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

#Music

#pygame.mixer.music.load('Crepuscular Rays.wav')
#pygame.mixer.music.play(-1)

#Veriables

font = pygame.font.SysFont('ARIAL', 20)
in_ = 'menu'
clock = pygame.time.Clock()
maxgass = random.randint(10**2, 10**6)
gass = maxgass
pulsars = list()

#Winodw

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ELEVAS')
pygame.display.set_icon(pygame.image.load('ElEvAS.png'))
lns = 0

#Menu

class menu():
    class elevas():
        def __init__(self):
            self.elevas = pygame.image.load('ElEvAS.png')
        def loop(self):
            global in_
            key = pygame.key.get_pressed()
            win.blit((self.elevas), (0, 0))
            if key[pygame.K_SPACE]:
                in_ = 'simulator'
                
#ELEVAS

class elevas():
    class stars():
        def __init__(self):
            self.num5 = 0
            self.num6 = 0
            self.num11 = 0
            self.num12 = 0
            self.blue = pygame.image.load('elevas_blue.png')
            self.darkblue = pygame.image.load('elevas_darkblue.png')
            self.red = pygame.image.load('elevas_red.png')
            self.yellow = pygame.image.load('elevas_yellow.png')
            self.white = pygame.image.load('elevas_white.png')
            self.binary = pygame.image.load('elevas_binary.png')
            self.binary2 = pygame.image.load('elevas_binary2.png')
            self.binary3 = pygame.image.load('elevas_SNIa.png')
            self.orange = pygame.image.load('elevas_orange.png')
            self.nova = pygame.image.load('supernova.png')
            self.exploding = [pygame.image.load('SN0.png'), pygame.image.load('SN1.png'), pygame.image.load('supernova.png')]
            self.nebulosas = [pygame.image.load('nebulosa.png'), pygame.image.load('nebulosa2.png')]
            self.bh = pygame.image.load('elevas_BH.png')
            self.x = list()
            self.y = list()
            self.starded = list()
            self.staraleve = list()
            self.color = list()
            self.sd = list()
            self.gbb = 0
            self.gby = 0
            self.gbw = 0
            self.gbo = 0
            self.gbdb = 0
        def loop(self):
            self.num = 0
            self.num2 = 0
            self.num3 = 0
            self.num4 = 0
            self.num7 = 0
            self.num8 = 0
            self.num9 = 0
            self.num10 = 0
            self.num13 = 0
            for a in range(len(self.x)):
                if not self.starded[a] < time.num - 6 and self.color[a] == 'blue': self.num += 1
                if not self.starded[a] < time.num - 6 and self.color[a] == 'darkblue': self.num += 1
                if not self.starded[a] < time.num - 6 and self.color[a] == 'yellow': self.num2 += 1
                if not self.starded[a] < time.num - 6 and self.color[a] == 'yellow binary': self.num2 += 1
                if not self.starded[a] < time.num - 6 and self.color[a] == 'white': self.num7 += 1
                if not self.starded[a] < time.num - 6 and self.color[a] == 'orange': self.num8 += 1
                if self.starded[a] < time.num and self.color[a] == 'blue': self.num3 += 1
                if self.starded[a] < time.num and self.color[a] == 'darkblue': self.num3 += 1
                if self.starded[a] < time.num and self.color[a] == 'yellow': self.num4 += 1
                if self.starded[a] < time.num and self.color[a] == 'yellow binary': self.num4 += 1
                if self.starded[a] < time.num and self.color[a] == 'white': self.num9 += 1
                if self.starded[a] < time.num and self.color[a] == 'orange': self.num10 += 1
                if self.starded[a] < time.num and self.color[a] == 'darkblue': self.num13 += 1
                global gass
                if self.gbb < self.num3:
                    for a in range(self.gbb - self.num3):
                        gass += 800
                if self.gby < self.num4:
                    for a in range(self.gby - self.num4):
                        gass += 200
                if self.gbw < self.num9:
                    for a in range(self.gbw - self.num9):
                        gass += 700
                if self.gbo < self.num10:
                    for a in range(self.gbo - self.num10):
                        gass += 100
                if self.gbdb < self.num13:
                    for a in range(self.gbdb - self.num13):
                        gass += 1000
            self.gbb = self.num3
            self.gby = self.num4
            self.gbw = self.num9
            self.gbo = self.num10
            self.gdbb = self.num13
            if self.color:
                #Stars in screen#
                for a in range(len(self.x)):
                    if self.starded[a] < time.num and not self.starded[a] < time.num - 2 and self.staraleve[a] < time.num and self.color[a] != 'yellow binary':
                        win.blit(pygame.transform.scale(self.red, (70, 70)), (self.x[a] - 35 - moving.cx, self.y[a] - 35 - moving.cy))
                    elif self.color[a] == 'yellow binary':
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 5 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.binary3, (16, 16)), (self.x[a] - 8 - moving.cx, self.y[a] - 8 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 3 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.binary2, (16, 16)), (self.x[a] - 8 - moving.cx, self.y[a] - 8 - moving.cy))
                    elif self.color[a] == 'yellow':
                         if self.starded[a] < time.num - 5 and self.starded[a]:
                            win.blit(pygame.transform.scale(self.white, (10, 10)), (self.x[a] - 5 - moving.cx, self.y[a] - 5 - moving.cy))
                         elif self.starded[a] < time.num - 2:
                            win.blit(pygame.transform.scale(self.nebulosas[1], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                         elif self.starded[a] < time.num:
                            win.blit(pygame.transform.scale(self.nebulosas[0], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                    elif self.color[a] == 'blue':
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 5 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[2], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 4 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[1], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 3 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[0], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                    elif self.color[a] == 'darkblue':
                        if self.starded[a] < time.num - 7 and self.starded[a]:
                            win.blit(pygame.transform.scale(self.bh, (20, 20)), (self.x[a] - 10 - moving.cx, self.y[a] - 10 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 5:
                            win.blit(pygame.transform.scale(self.exploding[2], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 4:
                            win.blit(pygame.transform.scale(self.exploding[1], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 3:
                            win.blit(pygame.transform.scale(self.exploding[0], (50, 50)), (self.x[a] - 25 - moving.cx, self.y[a] - 5 - moving.cy))
                    elif self.color[a] == 'white':
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 5 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[2], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 4 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[1], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 3 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[0], (30, 30)), (self.x[a] - 15 - moving.cx, self.y[a] - 15 - moving.cy))
                    if not self.starded[a] < time.num and self.staraleve[a] < time.num:
                        if self.color[a] == 'blue':
                            win.blit(pygame.transform.scale(self.blue, (20, 20)), (self.x[a] - 10 - moving.cx, self.y[a] - 10 - moving.cy))
                        elif self.color[a] == 'yellow binary':
                            win.blit(pygame.transform.scale(self.binary, (16, 16)), (self.x[a] - 8 - moving.cx, self.y[a] - 8 - moving.cy))
                        elif self.color[a] == 'yellow':
                            win.blit(pygame.transform.scale(self.yellow, (10, 10)), (self.x[a] - 5 - moving.cx, self.y[a] - 5 - moving.cy))
                        elif self.color[a] == 'orange':
                            win.blit(pygame.transform.scale(self.orange, (10, 10)), (self.x[a] - 5 - moving.cx, self.y[a] - 5 - moving.cy))
                        elif self.color[a] == 'white':
                            win.blit(pygame.transform.scale(self.white, (18, 18)), (self.x[a] - 9 - moving.cx, self.y[a] - 9 - moving.cy))
                        elif self.color[a] == 'darkblue':
                            win.blit(pygame.transform.scale(self.darkblue, (50, 50)), (self.x[a] - 25 - moving.cx, self.y[a] - 25 - moving.cy))
            if random.randint(1, 200) == 1:
                if random.randint(1, 3) <= 2:
                    if gass > 400:
                        self.color.append('orange')
                        self.x.append(random.randint(-800, 1600))
                        self.y.append(random.randint(-600, 1200))
                        self.staraleve.append(time.num)
                        self.num12 += 1
                        self.starded.append(random.randint(round(time.num) + 100000000000, round(time.num) + 100000000000))
                        gass -= 400
                elif random.randint(1, 3) == 1:
                    if random.randint(1, 2) == 1:
                        if random.randint(1, 3) <= 2:
                            if gass > 1000:
                                self.color.append('blue')
                                self.x.append(random.randint(-800, 1600))
                                self.y.append(random.randint(-600, 1200))
                                self.staraleve.append(time.num)
                                self.num5 += 1
                                self.starded.append(random.randint(round(time.num) + 10, round(time.num) + 30))
                                gass -= 1000
                        else:
                            if gass > 1200:
                                self.color.append('darkblue')
                                self.x.append(random.randint(-800, 1600))
                                self.y.append(random.randint(-600, 1200))
                                self.staraleve.append(time.num)
                                self.num5 += 1
                                self.starded.append(random.randint(round(time.num) + 5, round(time.num) + 10))
                                gass -= 1200
                    else:
                        if gass > 900:
                            self.color.append('white')
                            self.x.append(random.randint(-800, 1600))
                            self.y.append(random.randint(-600, 1200))
                            self.staraleve.append(time.num)
                            self.num11 += 1
                            self.starded.append(random.randint(round(time.num) + 30, round(time.num) + 100))
                            gass -= 900
                elif random.randint(1, 2) == 1 and gass > 500:
                    self.color.append('yellow')
                    self.starded.append(random.randint(round(time.num) + 1000, round(time.num) + 10000))
                    self.x.append(random.randint(-800, 1600))
                    self.y.append(random.randint(-600, 1200))
                    self.staraleve.append(time.num)
                    self.num6 += 1
                    gass -= 500
                elif gass > 1000:
                    self.color.append('yellow binary')
                    self.starded.append(random.randint(round(time.num) + 1000, round(time.num) + 10000))
                    self.x.append(random.randint(-800, 1600))
                    self.y.append(random.randint(-600, 1200))
                    self.staraleve.append(time.num)
                    self.num6 += 1
                    gass -= 1000
    class time():
        def __init__(self):
            self.num = 0
        def loop(self):
            self.fps = clock.get_fps()
            self.text = font.render(str(round(self.num)) + ' Mry ' + str(stars.num) + '  ' + str(stars.num2)\
            + '  ' + str(stars.num7) + '  ' + str(stars.num8) + '  ' + str(stars.num + stars.num2 + stars.num7 + stars.num8) +\
            '  ' + str(stars.num3) + '  ' + str(stars.num4) + '  ' + str(stars.num9) + '  ' + str(stars.num10) + '  ' +\
            str(stars.num3 + stars.num4 + stars.num9 + stars.num10) +\
            '  ' + str(stars.num5) + '  ' + str(stars.num6) + '  ' + str(stars.num11) + '  ' + str(stars.num12) + '  '\
            + str(stars.num5 + stars.num6 + stars.num11 + stars.num12) +\
            '  ' + str(gass) + '  ' + str(round(self.fps)), True, (255, 255, 255))
            win.blit((self.text), (20, 20))
            self.num += 0.005
    class moving():
        def __init__(self):
            self.key = pygame.key.get_pressed()
            self.cx = 0
            self.cy = 0
        def loop(self):
            self.key = pygame.key.get_pressed()
            if self.key[pygame.K_UP]:
                self.cy -= 1
            elif self.key[pygame.K_DOWN]:
                self.cy += 1
            if self.key[pygame.K_RIGHT]:
                self.cx += 1
            elif self.key[pygame.K_LEFT]:
                self.cx -= 1
        
#Sprites

stars = elevas.stars()
time = elevas.time()
menuimg = menu.elevas()
moving = elevas.moving()

#Loop

while True:
    clock.tick(100)
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if in_ == 'simulator':
        stars.loop()
        time.loop()
        moving.loop()
    else:
        menuimg.loop()
    pygame.display.update()
