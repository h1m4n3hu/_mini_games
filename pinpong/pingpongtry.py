import pygame
import random
import os

pygame.init()
pygame.mixer.init()

allsprites=pygame.sprite.Group()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1000,575))
vec=pygame.math.Vector2
bg=pygame.image.load("ground.png")
imgfolder=os.path.join(os.path.dirname(__file__),"")
pongsound=pygame.mixer.Sound(os.path.join(imgfolder,"plop.ogg"))

class WSplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,100))
        self.rect=self.image.get_rect()
        self.image.fill((0,0,0))
        self.pos=vec(60,300)
        self.vel=vec(0,0)
    def update(self):
        self.pos+=self.vel
        self.rect.center=self.pos
        if self.pos.y>600 or self.pos.y<0:
            self.vel.y=0
wsplay=WSplay()
allsprites.add(wsplay)

class MKplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,100))
        self.rect=self.image.get_rect()
        self.image.fill((255,255,255))
        self.pos=vec(940,300)
        self.vel=vec(0,0)
    def update(self):
        self.pos+=self.vel
        self.rect.center=self.pos
        if self.pos.y>600 or self.pos.y<0:
            self.vel.y=0
mkplay=MKplay()
allsprites.add(mkplay)

class Upper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((1000,30))
        self.rect=self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.pos=vec(500,15)
    def update(self):
        self.rect.center=self.pos
upper=Upper()
allsprites.add(upper)
class Lower(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((1000,30))
        self.rect=self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.pos=vec(500,560)
    def update(self):
        self.rect.center=self.pos
lower=Lower()
allsprites.add(lower)

class WSScore(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(imgfolder,"football.png"))
        self.image=pygame.transform.scale(self.image,(20,40))
        self.rect=self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.pos=vec(500,560)
    def update(self):
        self.rect.center=self.pos

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(imgfolder,"football.png"))
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect=self.image.get_rect()
        self.pos=vec(500,300)
        self.vel=vec(0,0)
    def update(self):
        self.pos+=self.vel
        self.rect.center=self.pos
        coldown=pygame.sprite.collide_rect(ball,lower)
        if coldown==True:
            self.vel.y=random.randrange(-11,-8)
        colup=pygame.sprite.collide_rect(ball,upper)
        if colup==True:
            self.vel.y=random.randrange(8,11)
        colmk=pygame.sprite.collide_rect(ball,mkplay)
        if colmk==True:
            pongsound.play()
            self.vel.x=random.randrange(-11,-8)
        colws=pygame.sprite.collide_rect(ball,wsplay)
        if colws==True:
            pongsound.play()
            self.vel.x=random.randrange(8,11)
            
        if ball.pos.x<0:
            ball.vel.x=0
            ball.vel.y=0
        if ball.pos.x>1000:
            ball.vel.x=0
            ball.vel.y=0
            
        if ball.vel==vec(0,0):
            ball.pos=vec(500,300)
            
ball=Ball()
allsprites.add(ball)
            
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if ball.vel==vec(0,0):
                if event.key==pygame.K_SPACE:
                    ball.vel.x=random.randrange(6,9) if random.getrandbits(1) else random.randrange(-9,-6)
                    ball.vel.y=random.randrange(6,9) if random.getrandbits(1) else random.randrange(-9,-6)
            if event.key==pygame.K_w:
                wsplay.vel.y=-11
            if event.key==pygame.K_s:
                wsplay.vel.y=11
            if event.key==pygame.K_k:
                mkplay.vel.y=-11
            if event.key==pygame.K_m:
                mkplay.vel.y=11
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                wsplay.vel.y=0
            if event.key==pygame.K_s:
                wsplay.vel.y=0
            if event.key==pygame.K_k:
                mkplay.vel.y=0
            if event.key==pygame.K_m:
                mkplay.vel.y=0
    
    clock.tick(30)
    screen.blit(bg,(0,0))
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()
