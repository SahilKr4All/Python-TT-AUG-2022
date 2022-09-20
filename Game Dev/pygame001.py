import pygame
import random
pygame.init()
H = 600
W = 1000
gameBoard = pygame.display.set_mode((W,H))
color = 255,255,255
red = 255,0,0
movex=0
movey=0
rectx=0
recty=0
frogImg=pygame.image.load("frog.png")
frogImg = pygame.transform.scale(frogImg,(70,100))
frogx = random.randint(0,W-70)
frogy = random.randint(0,H-100)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movex = 0
                movey = -1
            elif event.key == pygame.K_DOWN:
                movex = 0
                movey = 1
            elif event.key == pygame.K_LEFT:
                movex = -1
                movey = 0
            elif event.key == pygame.K_RIGHT:
                movex = 1
                movey = 0
        
                
    gameBoard.fill(color)
    snake = pygame.draw.rect(gameBoard,red,[rectx,recty,25,25])
    #pygame.draw.circle(gameBoard,red,(200,200),20)
    gameBoard.blit(frogImg,(frogx,frogy))
    frog = pygame.Rect(frogx,frogy,25,25)
    rectx+=movex
    recty+=movey
    
    if snake.colliderect(frog):
        print("collision occured")
        frogx = random.randint(0,W-70)
        frogy = random.randint(0,H-100)


    if rectx>W:
        rectx=0
    elif rectx<0:
        rectx=W
    if recty>H :
        recty=0
    elif recty<0:
        recty=H
        
    pygame.display.update()
    
