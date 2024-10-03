import pyxel

##Importation class Joueur
from resources.player import Player
##Importation monde
from resources.world import World, WorldItem, world_item_draw, TILE_SIZE


class App:
    def __init__(self) -> None:
        pyxel.init(160, 120, fps=120, title='Aura' )
        pyxel.load('./resources/resource1.pyxres')

        self.world = World(pyxel.tilemaps[0])

        self.player = Player(self.world)

        pyxel.run(self.update, self.draw)
    


    def update(self):


        if pyxel.btn(pyxel.KEY_Q):
            self.player.mv_lft()

        elif pyxel.btn(pyxel.KEY_D):
            self.player.mv_rght()
            
        elif pyxel.btn(pyxel.KEY_Z):
            self.player.mv_up()
        
        elif pyxel.btn(pyxel.KEY_S):
            self.player.mv_dwn()
        



    def draw(self):
        pyxel.cls(0)
        
        for y in range(self.world.HEIGHT):
            for x in range(self.world.WIDTH):
                world_item = self.world.world_map[y][x]
                world_item_draw(pyxel, x, y, world_item)
        
        pyxel.blt(
            self.player.x,
            self.player.y,
            self.player.IMG,
            WorldItem.PLAYER[0] * TILE_SIZE,
            WorldItem.PLAYER[1] * TILE_SIZE,
            self.player.WIDTH,
            self.player.HEIGHT,
        )


App()
