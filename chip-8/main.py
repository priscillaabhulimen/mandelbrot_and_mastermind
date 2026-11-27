from classes.memory import Memory
from classes.cpu import Cpu

with open("roms/2-ibm-logo.ch8", "rb") as file:
    rom = file.read()

memory = Memory()
assert memory.data[0] == 0xF0
assert memory.data[5] == 0x20
assert memory.data[0x4F] == 0x80
print("Font loaded successfully!")

memory.load_rom(rom)

cpu = Cpu(memory)

def run_cycle():
    opcode = cpu.fetch_opcode()
    cpu.decode_execute_opcode(opcode)
    cpu.display.render()

    cpu.display.root.after(10, run_cycle)

cpu.display.root.after(0, run_cycle)

cpu.display.root.mainloop()