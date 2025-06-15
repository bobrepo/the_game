import pygame


class play(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 6
        self.direction = 0

    def mov(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction = 1
        elif keys[pygame.K_a]:
            self.direction = -1
        else:
            self.direction = 0

    def update(self):
        self.mov()
        self.rect.x += self.direction * self.speed
