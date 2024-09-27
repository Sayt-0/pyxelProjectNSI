class World:

    FLOOR = (0, 14)
    PLAYER = (0, 13)
    EMPTY = (1, 13)


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
                if self.tilemap.pget(x,y) == WorldItem.WALL:
                    self.world_map[y].append