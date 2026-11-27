# CHIP-8 Emulator — Technical Research Notes

## 1. Memory and program loading

CHIP-8 has **4 KB (4,096 bytes) of memory**, with addresses ranging from `0x000` to `0xFFF`. Most CHIP-8 programs are loaded at memory address `0x200` (512 in decimal). The program counter (PC) therefore starts at `0x200` so that the CPU begins executing the loaded program.

The original CHIP-8 font contains hexadecimal characters `0` through `F`. Each character is represented by 5 bytes, making the complete font 80 bytes long. In my implementation, I stored the font data at the beginning of memory, from `0x000` to `0x04F`, and loaded ROM data starting at `0x200`.

## 2. Registers and stack

CHIP-8 has 16 general-purpose 8-bit registers, named `V0` through `VF`. These registers store values used by instructions. The `VF` register is also used as a flag register. For example, it can indicate whether an arithmetic operation produces a carry or borrow, or whether drawing a sprite causes a collision.

The `I` register is 16 bits wide and stores a memory address, usually used to locate sprite data. The **program counter (PC)** stores the address of the next instruction to execute.

CHIP-8 also uses a stack to store return addresses when a subroutine is called. When a subroutine finishes, the CPU retrieves the saved address and returns to it. The stack pointer (SP) tracks the stack position. The original CHIP-8 system supports up to 16 levels of nested subroutines.

## 3. Delay and sound timers

CHIP-8 has two 8-bit timers:

- **Delay timer:** Used by programs to measure time and create delays. It counts down until it reaches zero.
- **Sound timer:** Controls the CHIP-8 buzzer. While its value is greater than zero, the buzzer should produce a sound.

Both timers decrease at a rate of **60 times per second (60 Hz)**, independently of the CPU instruction execution speed.

In my emulator, I used Tkinter's `after()` method to schedule timer updates approximately 60 times per second. The delay timer counts down, while the sound timer displays a `BEEP!` message in the terminal when it reaches zero. This is a simple sound indicator rather than an actual audible buzzer.

## 4. Display and sprite drawing

The original CHIP-8 display is a monochrome screen with a resolution of **64 × 32 pixels**. Each pixel can either be on or off. My emulator represents the screen using a two-dimensional grid and uses Tkinter to display enlarged pixels in a window.

The `DXYN` instruction draws a sprite from memory. The sprite's starting address is stored in `I`, while registers `VX` and `VY` provide its screen coordinates. The final part of the instruction, `N`, specifies the sprite height in rows.

Sprite drawing uses the **XOR operation**. Each sprite pixel toggles the corresponding screen pixel. If a pixel that was already on is turned off by drawing, a collision has occurred, and `VF` is set to 1. Otherwise, `VF` is set to 0. Drawing the same sprite twice in the same position therefore erases it.

## 5. Keypad

CHIP-8 uses a hexadecimal keypad with 16 keys, numbered `0` through `F`. An emulator maps these virtual keys to physical keyboard keys.

My implementation uses the following mapping:

| CHIP-8 keypad | Computer keyboard |
|---|---|
| 1 2 3 C | 1 2 3 4 |
| 4 5 6 D | Q W E R |
| 7 8 9 E | A S D F |
| A 0 B F | Z X C V |

The emulator tracks whether each key is pressed or released. This allows instructions to check whether a particular key is currently pressed, or to wait until a key is pressed.

## 6. Fetch, decode and execute

The CPU follows a repeating **fetch-decode-execute cycle**:

1. **Fetch:** Read the next two bytes from memory at the address stored in the PC. Combine them into a 16-bit opcode and advance the PC by two.
2. **Decode:** Separate the opcode into its fields to identify which instruction should run and which values it uses.
3. **Execute:** Carry out the instruction, such as changing a register, jumping to another address, drawing a sprite or checking keyboard input.

CHIP-8 instructions are 16 bits long. The main opcode fields are:

- `NNN`: A 12-bit memory address.
- `NN`: An 8-bit constant value.
- `N`: A 4-bit value, often used to specify sprite height.
- `X`: A 4-bit register identifier, selecting a register from `V0` to `VF`.
- `Y`: A 4-bit register identifier, selecting another register.

For example, `6XNN` loads the value `NN` into register `VX`. `1NNN` jumps to address `NNN`. `DXYN` draws a sprite using coordinates from `VX` and `VY`.

## 7. Sources

1. Tobias V. Langhoff, **Guide to making a CHIP-8 emulator**. A detailed guide to memory, registers, timers, display, input and instruction implementation.  
   https://tobiasvl.github.io/blog/write-a-chip-8-emulator/

2. **Cowgod's CHIP-8 Technical Reference**. A technical reference describing the original CHIP-8 memory layout, registers, stack, timers, keypad and instruction set.  
   http://devernay.free.fr/hacks/chip8/C8TECH10.HTM

3. Timendus, **CHIP-8 Test Suite**. A collection of ROMs for testing CHIP-8 implementations, including the IBM logo and Corax+ opcode tests.  
   https://github.com/Timendus/chip8-test-suite