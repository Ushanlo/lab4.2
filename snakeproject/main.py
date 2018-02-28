#import modules
import sys, pygame, os, time, threading
from pygame.locals import *

#class snake_head(snake_body):

#class bonus(pygame.sprite.Sprite):

#class wall(pygame.sprite.Sprite):

MODULE_CODE = '001'

ASPECT_RATIO = (4, 3)
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)

logo = pygame.image.load(os.path.join('img\\rummy.png'))
logo_rect = logo.get_rect()
logo8x = pygame.transform.scale(logo, (logo_rect.width * 8, logo_rect.height * 8))
logo_rect = logo8x.get_rect()
logo_rect.center = (int(WIDTH / 2), int(HEIGHT / 2))

#library initialization
pygame.init()

start_ticks=pygame.time.get_ticks()
pygame.mixer.music.load('music\\azaza.mp3')
pygame.mixer.music.play(-1, 0.0)

DISPLAY_SURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quantum Snake: ' + MODULE_CODE)

logo_flag = False
def logo():
    global logo_flag
    logo_flag = True    
timer = threading.Timer(2, logo)
timer.start()

#logo loop
while not logo_flag:
    DISPLAY_SURF.fill((0, 0, 0))
    DISPLAY_SURF.blit(logo8x, logo_rect)
    pygame.display.update()



#main game loop
while True:
    DISPLAY_SURF.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        print(str(event))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP or event.key == 119:
                print("Up")
            elif event.key == K_DOWN or event.key == 115:
                print("Down")
            elif event.key == K_RIGHT or event.key == 100:
                print("Right")
            elif event.key == K_LEFT or event.key == 97:
                print("Left")
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.update()
