import sys
import pygame

pygame.init()
FPS = 30
fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps_clock.tick(FPS)