from classes.memory import Memory
from classes.cpu import Cpu

with open("roms/3-corax+.ch8", "rb") as file:
    rom = file.read()

memory = Memory()
assert memory.data[0] == 0xF0
assert memory.data[5] == 0x20
assert memory.data[0x4F] == 0x80
print("Font loaded successfully!")

memory.load_rom(rom)

cpu = Cpu(memory)

# cpu.sound_timer = 5
# cpu.delay_timer = 5

def update_timers():
    cpu.update_timers()
    cpu.display.root.after(1000 // 60, update_timers)

cpu.display.root.after(1000 // 60, update_timers)

def run_cycle():
    for _ in range(10):
        opcode = cpu.fetch_opcode()
        cpu.decode_execute_opcode(opcode)

    cpu.display.render()
    cpu.display.root.after(10, run_cycle)

cpu.display.root.after(0, run_cycle)

cpu.display.root.mainloop()