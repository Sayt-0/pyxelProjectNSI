from resources.world import TILE_SIZE, WorldItem, sprites_collide
from resources.utils import round_float_if_close

class Player:
    IMG = 0
    U = 0
    V = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 0.5
    ROUNDING_ERROR_DELTA = 0.1


    def __init__(self, world) -> None:
        self.__x = world.player_grid_x * TILE_SIZE
        self.__y = world.player_grid_y * TILE_SIZE
        self.world = world

    def s_m(self):
        self.__x = round_float_if_close(self.__x, self.ROUNDING_ERROR_DELTA)
        self.__y = round_float_if_close(self.__y, self.ROUNDING_ERROR_DELTA)

    def mv_lft(self):
        tile_y = int(self.__y / TILE_SIZE)
        tile_x = int(self.__x / TILE_SIZE)
        
        new_x = self.__x - self.DX
        new_tile_x = tile_x - 1
    
        if new_tile_x < 0:
            return  # Cannot go beyond the map
    
        next_tile_up = self.world.world_map[tile_y][new_tile_x]
        next_tile_bottom = self.world.world_map[tile_y + 1][new_tile_x] 
        
        if (
            next_tile_up == WorldItem.FLOOR
            and sprites_collide(
                new_x, self.__y, new_tile_x * TILE_SIZE, tile_y * TILE_SIZE
            )
        ) or (
            next_tile_bottom == WorldItem.FLOOR
            and sprites_collide(
                new_x, self.__y, new_tile_x * TILE_SIZE, (tile_y + 1) * TILE_SIZE
            )
        ):
            return
        
        self.__x = new_x

    def mv_rght(self):
        tile_y = int(self.__y / TILE_SIZE)
        tile_x = int(self.__x / TILE_SIZE)
        
        new_x = self.__x + self.DX
        new_tile_x = tile_x + 1
    
        if new_tile_x >= len(self.world.world_map[0]):
            return  # Cannot go beyond the map
    
        next_tile_up = self.world.world_map[tile_y][new_tile_x]
        next_tile_bottom = self.world.world_map[tile_y + 1][new_tile_x] 
        
        if (
            next_tile_up == WorldItem.FLOOR
            and sprites_collide(
                new_x, self.__y, new_tile_x * TILE_SIZE, tile_y * TILE_SIZE
            )
        ) or (
            next_tile_bottom == WorldItem.FLOOR
            and sprites_collide(
                new_x, self.__y, new_tile_x * TILE_SIZE, (tile_y + 1) * TILE_SIZE
            )
        ):
            return  
        
        self.__x = new_x

    def mv_up(self):
        tile_y = int(self.__y / TILE_SIZE)
        tile_x = int(self.__x / TILE_SIZE)
        
        new_y = self.__y - self.DX
        new_tile_y = tile_y - 1

        if new_tile_y < 0:
            return  # Cannot go beyond the map

        next_tile_left = self.world.world_map[new_tile_y][tile_x]
        next_tile_right = self.world.world_map[new_tile_y][tile_x + 1] 
        
        if (
            next_tile_left == WorldItem.FLOOR
            and sprites_collide(
                self.__x, new_y, tile_x * TILE_SIZE, new_tile_y * TILE_SIZE
            )
        ) or (
            next_tile_right == WorldItem.FLOOR
            and sprites_collide(
                self.__x, new_y, (tile_x + 1) * TILE_SIZE, new_tile_y * TILE_SIZE
            )
        ):
            return  
        
        self.__y = new_y

    def mv_dwn(self):
       
        
        tile_y = int(self.__y / TILE_SIZE)
        tile_x = int(self.__x / TILE_SIZE)
        
        new_y = self.__y + self.DX
        new_tile_y = tile_y + 1

        if new_tile_y >= len(self.world.world_map):
            return  # Cannot go beyond the map

        next_tile_left = self.world.world_map[new_tile_y][tile_x]
        next_tile_right = self.world.world_map[new_tile_y][tile_x + 1] 
        
        if (
            next_tile_left == WorldItem.FLOOR
            and sprites_collide(
                self.__x, new_y, tile_x * TILE_SIZE, new_tile_y * TILE_SIZE
            )
        ) or (
            next_tile_right == WorldItem.FLOOR
            and sprites_collide(
                self.__x, new_y, (tile_x + 1) * TILE_SIZE, new_tile_y * TILE_SIZE
            )
        ):
            return  
        
        self.__y = new_y

    def gravity(self):
        self.__y -= 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y