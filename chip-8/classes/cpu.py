from .memory import Memory
from .display import Display

class Cpu():
    def __init__(self, memory:Memory):
        self.memory = memory
        self.V = bytearray(16)
        self.I = 0
        self.PC = 0x200
        self.stack: list[int] = []
        self.SP = 0
        self.display = Display()

    def fetch_opcode(self):
        opcode = (self.memory.data[self.PC] << 8) | self.memory.data[self.PC + 1]
        self.PC += 2
        return opcode

    def decode_execute_opcode(self, opcode):
        instruction = (opcode & 0xF000) >> 12
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        n = opcode & 0x000F
        nn = opcode & 0x00FF
        nnn = opcode & 0x0FFF


        match instruction:
            case 6:
                self.V[x] = nn
            case 7:
                self.V[x] = (self.V[x] + nn) & 0xFF
            case 10:
                self.I = nnn
            case 1:
                self.PC = nnn
            case 0:
                if opcode == 0x00E0:
                    self.display.clear()
            case 13:
                self.V[0xF] = 0
                collision = self.display.draw(
                    self.memory.data,
                    self.V[x],
                    self.V[y],
                    n,
                    self.I
                )
                self.V[0xF] = int(collision)