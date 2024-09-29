from resources.world import TILE_SIZE, WorldItem

class Player:
    IMG = 0
    U = 0
    V = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 0.5

    def __init__(self, world) -> None:
        self.x = world.player_grid_x * TILE_SIZE
        self.y = world.player_grid_y * TILE_SIZE
        self.world = world

    def mv_lft(self):
        self.x -= self.DX
    
    def mv_rght(self):
        self.x += self.DX
