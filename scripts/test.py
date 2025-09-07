import pygame
import map

pygame.init()
tile_size, amt_tiles = 32, 12
scrn = pygame.display.set_mode((tile_size * amt_tiles, tile_size * amt_tiles))
pygame.display.set_caption("this_is_a_test")

clk = pygame.time.Clock()


def get_pos_of_player(player, map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == player:
                pos = [i, j]
                return pos


def camera_(map, playerchar):
    offset_x, offset_y = 3, 3
    # scc = list()
    player_pos = get_pos_of_player(playerchar, map)
    rx, ry = player_pos[0] - offset_x, player_pos[1] - offset_y
    for i in range(amt_tiles):
        for j in range(amt_tiles):
            pos_x, pos_y = i * tile_size, j * tile_size
            if map[i + rx][j + ry] == "o":
                a = pygame.surface.Surface((tile_size, tile_size))
                a.fill((255, 255, 255))
                scrn.blit(a, (pos_x, pos_y))
                print("d")
            else:
                b = pygame.surface.Surface((tile_size, tile_size))
                b.fill((200, 0, 0))
                scrn.blit(b, (pos_x, pos_y))
            print(i, j, i + rx, j + ry)


camera_(map.m[0], "o")


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            break

    pygame.display.flip()
    clk.tick(60)
