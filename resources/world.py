TILE_SIZE = 8

SPRITE_BANK = 0

class WorldItem:
    
     
    FLOOR = (3, 0)
    PLAYER = (0, 0)
    EMPTY = (2, 1)


class World:

    


    HEIGHT = 16
    WIDTH = 16


    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.world_map = []
        self.player_grid_x = 0
        self.player_grid_y = 0
        for y in range(self.HEIGHT):
            self.world_map.append([])
            for x in range(self.WIDTH):
                if self.tilemap.pget(x,y) == WorldItem.FLOOR:
                    self.world_map[y].append(WorldItem.FLOOR)
                elif self.tilemap.pget(x,y) == WorldItem.PLAYER:
                    self.world_map[y].append(WorldItem.EMPTY)
                    self.player_grid_x = x
                    self.player_grid_y = y
                else:
                    self.world_map[y].append(WorldItem.EMPTY)
                    
                    
def world_item_draw(pyxel, x, y, world_item):
    pyxel.blt(
        x * TILE_SIZE,
        y * TILE_SIZE,
        SPRITE_BANK,
        world_item[0] * TILE_SIZE,
        world_item[1] * TILE_SIZE,
        TILE_SIZE,
        TILE_SIZE
    )
    