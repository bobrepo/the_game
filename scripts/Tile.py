import pygame


class grass(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("../sprites/grass.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y


class dirt(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("../sprites/dirt.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y
