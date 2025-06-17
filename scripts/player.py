import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

        self.speed = 6
        self.direction = 0
        self.vel_y = 0
        self.jump_force = -15
        self.gravity = 1
        self.on_ground = True  

    def mov(self):
        keys = pygame.key.get_pressed()
        self.direction = 0
        if keys[pygame.K_d]:
            self.direction = 1
        elif keys[pygame.K_a]:
            self.direction = -1

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.bottom >= 650:
            self.rect.bottom = 650
            self.vel_y = 0
            self.on_ground = True

    def update(self):
        self.mov()
        self.jump()
        self.rect.x += self.direction * self.speed
        self.apply_gravity()
