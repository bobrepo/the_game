import pygame
import settings
import levels

pygame.init()

scrn = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("test")

clk = pygame.time.Clock()
levl = levels.buildmap(0, scrn)


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    scrn.fill((0, 0, 0))

    levl.run()

    pygame.display.flip()
    clk.tick(60)
