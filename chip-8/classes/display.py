import tkinter as tk

class Display():
    def __init__(self):
        self.clear()

        self.scale = 10
        self.root = tk.Tk()
        self.root.title("CHIP-8 Emulator")
        self.root.geometry("640x320")
        self.root.resizable(False, False)

        self.key_map = {
            "1": 0x1, "2": 0x2, "3": 0x3, "4": 0xC,
            "q": 0x4, "w": 0x5, "e": 0x6, "r": 0xD,
            "a": 0x7, "s": 0x8, "d": 0x9, "f": 0xE,
            "z": 0xA, "x": 0x0, "c": 0xB, "v": 0xF
        }

        self.root.bind("<KeyPress>", self.key_down)
        self.root.bind("<KeyRelease>", self.key_up)

        self.canvas = tk.Canvas(
            self.root,
            width=64 * self.scale,
            height=32 * self.scale,
            bg="black"
        )
        self.canvas.pack()

    def key_down(self, event):
        key = event.keysym.lower()
        if key in self.key_map:
            self.cpu.keypad[self.key_map[key]] = 1

    def key_up(self, event):
        key = event.keysym.lower()
        if key in self.key_map:
            self.cpu.keypad[self.key_map[key]] = 0

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

    def render(self):
        self.canvas.delete("all")
        for y in range(32):
            for x in range(64):
                if self.grid[y][x] == 1:
                    left = x * self.scale
                    top = y * self.scale
                    right = left + self.scale
                    bottom = top + self.scale

                    self.canvas.create_rectangle(
                        left, top, right, bottom,
                        fill="white",
                        outline="white"
                    )


# if __name__ == "__main__":
#     display = Display()
#     display.root.update_idletasks()

#     display.grid[0][0] = 1
#     display.render()

#     display.root.mainloop()