import pygame

pygame.init()
width,height=500,500
d=pygame.display.set_mode((width,height))



done=False

while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True


    pygame.display.flip()