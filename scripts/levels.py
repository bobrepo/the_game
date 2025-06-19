import pygame
import map as mapp
import settings
import player
import Tile


class buildmap:
    def __init__(self, map_no, seu):
        self.map_no = map_no
        self.surface = seu
        self.create_map(map_no)

    def create_map(self, num):
        map = mapp.m[num]
        self.block = pygame.sprite.Group()
        self.entity = pygame.sprite.Group()
        self.pplayer = pygame.sprite.GroupSingle()
        for i, stringg in enumerate(map):
            for j, char in enumerate(stringg):
                if char == "x":
                    y = settings.tile_x * i
                    x = settings.tile_y * j
                    t = Tile.grass((x, y))
                    self.block.add(t)
                elif char == "d":
                    y = settings.tile_x * i
                    x = settings.tile_y * j
                    t = Tile.dirt((x, y))
                    self.block.add(t)
                elif char == "o":
                    y = settings.tile_x * i
                    x = settings.tile_y * j
                    p = player.Player((x, y))
                    self.pplayer.add(p)
                elif char == "g":
                    y = settings.tile_x * i
                    x = settings.tile_y * j
                    e = Tile.grass_leaf((x, y))
                    self.entity.add(e)

    def run(self):
        self.block.update(0, 0)
        self.block.draw(self.surface)

        self.pplayer.update(self.block)
        self.pplayer.draw(self.surface)

        self.entity.update(0, 0)
        self.entity.draw(self.surface)
