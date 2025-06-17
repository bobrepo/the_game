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
        self.pplayer = pygame.sprite.GroupSingle()
        for i, stringg in enumerate(map):
            for j, char in enumerate(stringg):
                if char == "x":
                    y = settings.tile_x * i
                    x = settings.tile_y * j
                    t = Tile.tile((x, y))
                    self.block.add(t)
                elif char == "o":
                    y = settings.tile_x * i
                    x = settings.tile_y * j
                    p = player.Player((x, y))
                    self.pplayer.add(p)

    def run(self):
        self.block.update(0, 0)
        self.block.draw(self.surface)

        self.pplayer.update(self.block)
        self.pplayer.draw(self.surface)
