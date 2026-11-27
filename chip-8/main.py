from classes.memory import Memory
from classes.cpu import Cpu

with open("roms/2-ibm-logo.ch8", "rb") as file:
    rom = file.read()

memory = Memory()
memory.load_rom(rom)

cpu = Cpu(memory)

def run_cycle():
    opcode = cpu.fetch_opcode()
    cpu.decode_execute_opcode(opcode)
    cpu.display.render()

    cpu.display.root.after(2, run_cycle)

cpu.display.root.after(0, run_cycle)
cpu.display.root.mainloop()