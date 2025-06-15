import pygame


class tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y
