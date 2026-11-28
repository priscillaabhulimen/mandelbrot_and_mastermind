# Programming Assignment Projects

This repository contains three Python projects developed as part of a programming assignment. Each project is organised in its own folder.

## Repository structure

```text
mandelbrot_and_mastermind/
│
├── chip8/
│   ├── classes/
│   ├── roms/
│   ├── tests/
│   └── main.py
│
├── mandelbrot/
│
├── mastermind/
│   ├── classes/
│   ├── tests/
│   ├── colours.csv
│   ├── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Projects

### 1. CHIP-8 Emulator

A CHIP-8 emulator implemented in Python. The project is organised into separate components to handle memory, CPU instructions and display functionality.

Features include:
- 4 KB of memory and font data.
- CPU registers and instruction execution.
- CHIP-8 opcode decoding and execution.
- A 64 × 32 monochrome display.
- Sprite drawing using XOR and collision detection.
- Keyboard input mapped to the CHIP-8 keypad.
- Delay and sound timers.

**Testing:** The IBM Logo ROM was successfully displayed. The Corax+ test ROM was also run, although execution was slow and further performance improvements are needed.

### 2. Mastermind

An object-oriented implementation of the Mastermind code-breaking game.

The game involves guessing a secret sequence of coloured pegs and receiving feedback about the number of correct colours in the correct and incorrect positions.

The implementation uses classes to separate responsibilities and applies object-oriented programming concepts.

### 3. Mandelbrot

The repository also includes a folder for the Mandelbrot project.

## Requirements

- Python 3 (3.14.10 was used for this, detail necessary for `tkinter` compatibility
- NumPy (version specified in `requirements.txt`)
- Tkinter (for the CHIP-8 graphical display and Mandelbrot)

## Installation

Clone the repository:

```bash
git clone https://github.com/priscillaabhulimen/mandelbrot_and_mastermind.git
```

Navigate into the repository:

```bash
cd mandelbrot_and_mastermind
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Running the projects

Each project is contained in its own folder. Navigate into the relevant folder and run its Python entry-point file.

For example, to run the CHIP-8 emulator:

```bash
cd chip8
python main.py
```
-OR-
```bash
python -m chip8.main
```

Make sure the ROM you want to test is available in the `roms` folder.

## Notes

This repository contains the source code and supporting files for the projects. The CHIP-8 emulator is an ongoing implementation, and its execution speed and opcode coverage could benefit from further testing and improvement.
