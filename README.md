
# Hack Assembler

A Python program that converts Hack assembly code into Hack binary code. The Hack computer is a simple, educational machine designed as part of the **NAND to Tetris** course, where you build a complete computer system from scratch. This program helps by translating human-readable Hack assembly language into the machine code that the Hack computer can execute.

To learn more about how the Hack computer is designed and how the assembler works, you can explore the **NAND to Tetris** course: [NAND to Tetris](https://www.nand2tetris.org/).



### Example

```
Hack Assembly Code                                   Hack Binary Code
--------------------------------------------------------------------------------
@i                                                  0000 0000 0001 0000
M=1                                                 1110 1111 1100 1000
@sum                                                0000 0000 0001 0001
M=0                                                 1111 1100 0001 0000

(LOOP)                                       (No binary representation for labels)

@i                                                  0000 0000 0001 0000
D=M                                                 1110 0100 1101 0000
@100                                                0000 0000 0110 0100
D=D-A                                               1110 0100 1101 0000
@END                                                0000 0000 0001 0010
D;JGT                                               1110 0011 0000 0001

@i                                                  0000 0000 0001 0000
D=M                                                 1110 0100 1101 0000
@sum                                                0000 0000 0001 0001
M=D+M                                               1111 0000 1000 1000
@i                                                  0000 0000 0001 0000
M=M+1                                               1111 1101 1100 1000
@LOOP                                               0000 0000 0000 0100
0;JMP                                               1110 1010 1000 0111

(END)                                        (No binary representation for labels)

@END                                                0000 0000 0001 0010
0;JMP                                               1110 1010 1000 0111

```
