import pygame
from aster import asteroid
pygame.init()

win = pygame.display.set_mode((400,500))
pygame.display.set_caption("Space Game")

walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'),pygame.image.load('right_3.png'),
pygame.image.load('right_4.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'),pygame.image.load('left_3.png'),
pygame.image.load('left_4.png')]

playerStand = [pygame.image.load('stand_1.png'),pygame.image.load('stand_2.png'),
pygame.image.load('stand_3.png')]
bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()
x = 250
y = 400
width = 60
hight = 84
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

asteroid_y = 0
lastMove = "right"



class shot():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

def drawWindow():
    global animCount
    global asteroid_y
    win.blit(bg,(0,0))
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount % 4],(x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount % 4],(x,y))
        animCount += 1
    else:
        win.blit(playerStand[animCount % 3],(x,y))
        animCount += 1

    for bullet in bullets:
        bullet.draw(win)
        if abs(bullet.y - asteroid_y) < 5:
            asteroid_y = 0
            bullets.pop(bullets.index(bullet))
    if asteroid_y < 500:
        asteroid_y += 1 * speed
    else:
        asteroid_y = 0
    aster = asteroid(x,asteroid_y)
    aster.draw(win)
    if abs(y - asteroid_y) < 8:
        pygame.draw.circle(win,(255,0,0),(round(x),round(y)),40)
        asteroid_y = 0

    pygame.display.update()
run = True
bullets = []
asteroids = []
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y < 500 and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if len(bullets) > 0:
            if bullets[-1].y < 350:
                bullets.append(shot(round(x + width // 2),
                round (y),5,(255,0,0),1))
        else:
                bullets.append(shot(round(x + width // 2),
                round (y),5,(255,0,0),1))

    if keys[pygame.K_r]:
        bullets.append(shot(round(x + width // 2),
        round (y),5,(0,0,255),1))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"

    elif keys[pygame.K_RIGHT] and x < 395 - width:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        #animCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount **2 )/2
            else:
                y -= (jumpCount **2 )/2
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    drawWindow()



pygame.quit()
