# AI Development Log

## How I used AI

I used ChatGPT as a learning and troubleshooting resource while developing my CHIP-8 emulator. Most of my questions were about understanding what the assignment required, what particular concepts meant, and what I needed to implement next. I also used it to help me understand errors and work through parts of the implementation when I got stuck.

I tried to build the emulator myself rather than simply asking AI to generate the entire project. I asked follow-up questions when I did not understand an explanation and tested the code as I went.

## Examples of the help I asked for

My questions were generally along these lines:

- What do I need to implement for this part of the CHIP-8 assignment?
- What does a particular CHIP-8 component or instruction do?
- How is memory organised, and why does a ROM start at address `0x200`?
- What is the purpose of the CPU registers, stack, and program counter?
- What does XOR mean in the context of drawing sprites?
- How should keyboard input and timers work in an emulator?
- How can I tell whether a particular part of my implementation is working?

These questions helped me break a fairly large assignment into smaller parts that I could understand and implement individually.

## Debugging and corrections

AI explanations were useful, but I still had to test things myself and correct problems.

One issue was how the emulator's main loop interacted with Tkinter. A continuously running CPU loop would prevent Tkinter from processing window events properly. I needed to use Tkinter's `after()` method to schedule CPU execution and timer updates without blocking the event loop.

Another issue came up while testing keyboard input. A temporary test handler showed that key events were being detected, but it did not actually update the CHIP-8 keypad array. The keys appeared to be working at the window level, but the emulator was not receiving their states. I corrected the handlers so key presses set the corresponding keypad value and key releases reset it.

These experiences reinforced that getting something to run is not the same as confirming that it works correctly.

## Testing

I tested the emulator using the following:

- **IBM Logo ROM:** Successfully displayed the IBM logo.
- **Corax+ test ROM:** Ran, but execution was slow, so I cannot claim that the test passed.
- **Keyboard input:** Confirmed that key presses and releases updated the keypad array.
- **Timers:** Confirmed that the delay and sound timers counted down, and that the sound timer produced a terminal `BEEP!` indicator when it reached zero.
- **Sprite drawing:** Tested XOR drawing and collision detection, including drawing the same sprite twice to erase it.

## Reflection

Working on this project helped me understand how the different parts of an emulator fit together. I learned more about memory, registers, the fetch-decode-execute cycle, sprite drawing, keyboard input, and timers.

I also found that implementing something and understanding why it works are two different challenges. I often needed to ask what a concept meant before I could confidently use it in my code. Testing each feature separately made the project easier to manage and helped me catch mistakes.

The emulator is not perfect. In particular, the Corax+ test ran slowly, and I would need more testing and performance improvements to be confident in the implementation. Still, I was able to get the IBM Logo ROM working and test several of the emulator's core components.