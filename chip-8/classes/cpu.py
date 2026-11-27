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
        self.display.cpu = self

        self.keypad = [0] * 16
        self.delay_timer = 0
        self.sound_timer = 0

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
            case 0:
                if opcode == 0x00E0:
                    self.display.clear()
                elif opcode == 0x00EE:
                    self.PC = self.stack.pop()
            case 1:
                self.PC = nnn
            case 2:
                self.stack.append(self.PC)
                self.PC = nnn
            case 3:
                if self.V[x] == nn:
                    self.PC += 2
            case 4:
                if self.V[x] != nn:
                    self.PC += 2
            case 5:
                if n == 0 and  self.V[x] == self.V[y]:
                    self.PC += 2
                
            case 6:
                self.V[x] = nn
            case 7:
                self.V[x] = (self.V[x] + nn) & 0xFF
            case 8:
                match n:
                    case 0:
                        self.V[x] = self.V[y]
                    case 1:
                        self.V[x] |= self.V[y]
                    case 2:
                        self.V[x] &= self.V[y]
                    case 3:
                        self.V[x] ^= self.V[y]
                    case 4:
                        result = self.V[x] + self.V[y]
                        self.V[0xF] = int(result > 255)
                        self.V[x] = result & 0xFF
                    case 5:
                        self.V[0xF] = int(self.V[x] >= self.V[y])
                        self.V[x] = (self.V[x] - self.V[y]) & 0xFF
                    case 6:
                        self.V[0xF] = self.V[x] & 1
                        self.V[x] >>= 1
                    case 7:
                        self.V[0xF] = int(self.V[y] >= self.V[x])
                        self.V[x] = (self.V[y] - self.V[x]) & 0xFF
                    case 14:
                        self.V[0xF] = (self.V[x] >> 7) & 1
                        self.V[x] = (self.V[x] << 1) & 0xFF
            case 9:
                if  n == 0 and self.V[x] != self.V[y]:
                    self.PC += 2
            case 10:
                self.I = nnn
            case 11:
                self.PC = nnn + self.V[0]
            case 12:
                import random
                self.V[x] = random.randint(0, 255) & nn
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
            case 14:
                if nn == 0x9E:
                    if self.keypad[self.V[x]]:
                        self.PC += 2
                elif nn == 0xA1:
                    if not self.keypad[self.V[x]]:
                        self.PC += 2
            case 15:
                match nn:
                    case 0x07:
                        self.V[x] = self.delay_timer

                    case 0x15:
                        self.delay_timer = self.V[x]

                    case 0x18:
                        self.sound_timer = self.V[x]

                    case 0x1E:
                        self.I += self.V[x]

                    case 0x0A:
                        pressed = [i for i, key in enumerate(self.keypad) if key]
                        if pressed:
                            self.V[x] = pressed[0]
                        else:
                            self.PC -= 2

                    case 0x29:
                        self.I = self.V[x] * 5

                    case 0x33:
                        value = self.V[x]
                        self.memory.data[self.I] = value // 100
                        self.memory.data[self.I + 1] = (value // 10) % 10
                        self.memory.data[self.I + 2] = value % 10

                    case 0x55:
                        for i in range(x + 1):
                            self.memory.data[self.I + i] = self.V[i]

                    case 0x65:
                        for i in range(x + 1):
                            self.V[i] = self.memory.data[self.I + i]