import pygame
from settings import *

pygame.init()

scrn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("test")

clk = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    scrn.fill((255, 0, 255))

    pygame.display.flip()
    clk.tick(60)
