import pygame

pygame.init()
width,height=600,800
screen=pygame.display.set_mode((width,height))

done=False

while not done:
    pygame.draw.rect(screen,pygame.Color("blue"),pygame.Rect(300,400,100,200))
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            done=True
    pygame.display.flip()
