import unittest

from classes.display import Display


class TestDisplay(unittest.TestCase):
    def test_draw_toggles_pixels_and_reports_collision(self):
        display = Display()
        assert len(display.grid) == 32
        assert all(len(row) == 64 for row in display.grid)
        assert all(pixel == 0 for row in display.grid for pixel in row)

        memory = [0b10000000]
        collision = display.draw(memory, x=0, y=0, height=1, i=0)
        assert collision is False, "Drawing onto a blank display must not collide"
        assert display.grid[0][0] == 1, "Pixel (0, 0) should be turned on"
        assert sum(pixel for row in display.grid for pixel in row) == 1

        collision = display.draw(memory, x=0, y=0, height=1, i=0)
        assert collision is True, "Redrawing over a lit pixel must report a collision"
        assert display.grid[0][0] == 0, "XOR should turn the pixel back off"
        assert all(pixel == 0 for row in display.grid for pixel in row)
