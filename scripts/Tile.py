import pygame


class grass(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("../sprites/blocks/grass.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y


class dirt(grass):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("../sprites/blocks/dirt.png")
        self.rect = self.image.get_rect(topleft=pos)


# def update(self, x, y):
#     self.rect.x += x
#     self.rect.y += y


# entity


class grass_leaf(grass):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("../sprites/entity/bush.png")
        self.rect = self.image.get_rect(topleft=pos)


# def update(self, x, y):
#     self.rect.x += x
#     self.rect.y += y
