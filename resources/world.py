TILE_SIZE = 8

SPRITE_BANK = 0

class WorldItem:
    
     
    FLOOR = (3, 0)
    PLAYER = (0, 0)
    EMPTY = (2, 1)
    STARS = (2,0)
    BUSH = (4, 0)
    GRASS = (3, 1)


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
                elif self.tilemap.pget(x,y) == WorldItem.STARS:
                    self.world_map[y].append(WorldItem.STARS)
                elif self.tilemap.pget(x,y) == WorldItem.BUSH:
                    self.world_map[y].append(WorldItem.BUSH)
                elif self.tilemap.pget(x,y) == WorldItem.GRASS:
                    self.world_map[y].append(WorldItem.GRASS)
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

def sprites_collide(x1, y1, x2, y2):
    
    if x1 + TILE_SIZE <= x2 or x2 + TILE_SIZE <= x1:
        return False
    
    if y1 + TILE_SIZE <= y2 or y2 + TILE_SIZE <= y1:
        return False
    
    return True