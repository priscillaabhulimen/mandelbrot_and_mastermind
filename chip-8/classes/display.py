class Display():
    def __init__(self):
        self.clear()

    def clear(self):
        self.grid = [[0 for _ in range(64)] for _ in range(32)]

    def draw(self, memory, x, y, height, i):
        collision = False
        for r in range(height):
            sprite_b = memory[i + r]
            for b in range(8):
                bit = (sprite_b >> (7 - b)) & 1

                pixel_x = (x + b) % 64
                pixel_y = (y + r) % 32

                if self.grid[pixel_y][pixel_x] == 1 and bit == 1:
                    collision = True

                self.grid[pixel_y][pixel_x] ^= bit
        return collision