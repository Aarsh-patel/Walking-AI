import pygame
def simulate(screen,sim,clock,org,bg):
    while sim:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        pygame.draw.line(screen,(255,0,0),(0,649),(1280,649),1)
        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT:
                pygame.quit()
        org.draw()
        org.update()
        pygame.display.update()
    return 0