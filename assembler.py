import sys
from tokenizer import Tokenizer
from parser import Parser
from generator import Generator 

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <in> <out>");
        sys.exit(1);

    file = open(sys.argv[1], 'r')
    source = file.read()
    file.close()

    tokenizer = Tokenizer(source)
    tokens = tokenizer.getTokens()
    if tokenizer.error: sys.exit(1)
    parser = Parser(tokens)
    
    instructions = parser.parse()
    if parser.error: sys.exit(1)

    # init symbols
    symbolTable = {}
    for i in range(16):
        symbolTable['R' + str(i)] = i

    symbolTable["SCREEN"] = 16384
    symbolTable["KBD"] = 24576
    symbolTable["SP"] = 0
    symbolTable["LCL"] = 1
    symbolTable["ARG"] = 2 
    symbolTable["THIS"] = 3 
    symbolTable["THAT"] = 4 
    
    removedLabels = 0 
    for i, inst in enumerate(instructions[:]):
        if inst.getType() == 'L':
            symbolTable[inst.value] = i - removedLabels;
            instructions.remove(inst)
            removedLabels += 1

    nextVar = 16
    for inst in instructions:
        if inst.getType() == 'A':
            if inst.value.isdigit(): continue
            if inst.value not in symbolTable:
                symbolTable[inst.value] = nextVar;
                nextVar += 1

            inst.value = str(symbolTable[inst.value])



    generator = Generator(instructions)
    binary_instructions = generator.generate()

    with open(sys.argv[2], 'a') as f:
        for element in binary_instructions:
            f.write(element + '\n') 
    
if __name__ == '__main__':
    main()
