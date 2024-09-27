import pyxel
from resources.player import Player


class App:
    def __init__(self) -> None:
        pyxel.init(160, 120, fps=120, title='Aura' )
        pyxel.load('./resources/resource1.pyxres')

        self.player = Player()

        pyxel.run(self.update, self.draw)
    


    def update(self):


        if pyxel.btn(pyxel.KEY_Q):
            self.player.mv_lft()

        if pyxel.btn(pyxel.KEY_D):
            self.player.mv_rght()



    def draw(self):
        pyxel.cls(0)
        pyxel.blt(
            self.player.x,
            self.player.y,
            self.player.IMG,
            self.player.U,
            self.player.V,
            self.player.WIDTH,
            self.player.HEIGHT,
        )


App()