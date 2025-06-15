import pygame
import settings
import player

pygame.init()

scrn = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("test")

clk = pygame.time.Clock()
se = pygame.sprite.Group()
se.add(player.play((23, 23)))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    scrn.fill((0, 0, 0))

    se.update()
    se.draw(scrn)

    pygame.display.flip()
    clk.tick(60)
