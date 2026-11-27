import unittest

from classes.cpu import Cpu
from classes.memory import Memory


def make_cpu() -> Cpu:
    cpu = Cpu(Memory())
    cpu.memory.data[0x300] = 0b11000000
    cpu.decode_execute_opcode(0xA300)
    return cpu


def lit_pixels(cpu: Cpu) -> list[tuple[int, int]]:
    return [
        (px, py)
        for py in range(32)
        for px in range(64)
        if cpu.display.grid[py][px] == 1
    ]


class TestCpu(unittest.TestCase):
    def test_decode_execute(self):
        cpu = Cpu(Memory())

        cpu.decode_execute_opcode(0x6A05)
        assert cpu.V[10] == 5

        cpu.V[0] = 250
        cpu.decode_execute_opcode(0x700A)
        assert cpu.V[0] == 4

    def test_display_opcodes(self):
        cpu = make_cpu()
        cpu.decode_execute_opcode(0x6000)
        cpu.decode_execute_opcode(0x6100)
        cpu.decode_execute_opcode(0xD011)
        assert lit_pixels(cpu) == [(0, 0), (1, 0)]
        cpu.decode_execute_opcode(0x00E0)
        assert lit_pixels(cpu) == [], "00E0 should clear every lit pixel"

        cpu = make_cpu()
        cpu.decode_execute_opcode(0x6005)
        cpu.decode_execute_opcode(0x6103)
        cpu.decode_execute_opcode(0xD011)
        assert lit_pixels(cpu) == [(5, 3), (6, 3)]
        assert cpu.V[0xF] == 0

        cpu = make_cpu()
        cpu.decode_execute_opcode(0x6000)
        cpu.decode_execute_opcode(0x6100)
        cpu.decode_execute_opcode(0xD011)
        assert cpu.V[0xF] == 0
        cpu.decode_execute_opcode(0xD011)
        assert cpu.V[0xF] == 1, "Second draw should set VF = 1"
        assert lit_pixels(cpu) == []
