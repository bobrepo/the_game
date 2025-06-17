import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

        self.speed = 6
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_force = -15
        self.gravity_force = 1
        self.on_ground = False

    def mov(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_w] and self.on_ground:
            self.jump()
            self.on_ground = False

    def jump(self):
        self.direction.y = self.jump_force
        self.rect.y += self.direction.y

    def apply_gravity(self):
        self.direction.y += self.gravity_force
        self.rect.y += self.direction.y

    def collision_horizontal(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block):
                if self.direction.x == 1:
                    self.rect.right = block.rect.left
                    self.direction.x = 0
                if self.direction.x == -1:
                    self.rect.left = block.rect.right
                    self.direction.x = 0

    def collision_vertical(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block):
                if self.direction.y >= 1:
                    self.rect.bottom = block.rect.top
                    self.on_ground = True
                    self.direction.y = 0
                if self.direction.y <= -1:
                    self.rect.top = block.rect.bottom
                    self.direction.y = 0

    def update(self, blocks):
        self.mov()
        self.rect.x += self.direction.x * self.speed
        self.collision_horizontal(blocks)

        self.apply_gravity()
        self.collision_vertical(blocks)
