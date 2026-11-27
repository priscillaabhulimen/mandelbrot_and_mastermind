class Memory():
    def __init__(self):
        self.data = bytearray(4096)

    def load_rom(self, rom: bytes):
        start = 0x200
        for i in range(len(rom)):
            self.data[start + i] = rom[i]