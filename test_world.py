import unittest
from unittest.mock import MagicMock
from resources.world import world_item_draw, TILE_SIZE, SPRITE_BANK, WorldItem

class TestWorldItemDraw(unittest.TestCase):
    def setUp(self):
        self.pyxel = MagicMock()

    def test_world_item_draw_floor(self):
        world_item_draw(self.pyxel, 1, 2, WorldItem.FLOOR)
        self.pyxel.blt.assert_called_with(
            1 * TILE_SIZE,
            2 * TILE_SIZE,
            SPRITE_BANK,
            WorldItem.FLOOR[0] * TILE_SIZE,
            WorldItem.FLOOR[1] * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )

    def test_world_item_draw_player(self):
        world_item_draw(self.pyxel, 3, 4, WorldItem.PLAYER)
        self.pyxel.blt.assert_called_with(
            3 * TILE_SIZE,
            4 * TILE_SIZE,
            SPRITE_BANK,
            WorldItem.PLAYER[0] * TILE_SIZE,
            WorldItem.PLAYER[1] * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )

    def test_world_item_draw_empty(self):
        world_item_draw(self.pyxel, 5, 6, WorldItem.EMPTY)
        self.pyxel.blt.assert_called_with(
            5 * TILE_SIZE,
            6 * TILE_SIZE,
            SPRITE_BANK,
            WorldItem.EMPTY[0] * TILE_SIZE,
            WorldItem.EMPTY[1] * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )

if __name__ == '__main__':
    unittest.main()