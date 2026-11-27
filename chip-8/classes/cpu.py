from .memory import Memory

class Cpu():
    def __init__(self, memory:Memory):
        self.memory = memory
        self.V = bytearray(16)
        self.I = 0
        self.PC = 0x200
        self.stack: list[int] = []
        self.SP = 0

    def fetch_opcode(self):
        opcode = (self.memory.data[self.PC] << 8) | self.memory.data[self.PC + 1]
        self.PC += 2
        return opcode

    def decode_execute_opcode(self, opcode):
        instruction = (opcode & 0xF000) >> 12
        x = (opcode & 0x0F00) >> 8
        nn = opcode & 0x00FF

        if instruction == 6:
            self.V[x] = nn

def test_decode_execute():
    memory = Memory()
    cpu = Cpu(memory)

    cpu.decode_execute_opcode(0x6A05)
    assert cpu.V[10] == 5

test_decode_execute()