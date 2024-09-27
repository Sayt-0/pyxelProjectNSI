class Player:
    IMG = 0
    U = 0
    V = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 0.5

    def __init__(self) -> None:
        self.x = 80
        self.y = 60

    def mv_lft(self):
        self.x -= self.DX
    
    def mv_rght(self):
        self.x += self.DX
