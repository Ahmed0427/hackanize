import sys
from tokenizer import Tokenizer
from parser import Parser

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
    print(len(instructions))
    for inst in instructions:
        print(inst.toString())
    
if __name__ == '__main__':
    main()
