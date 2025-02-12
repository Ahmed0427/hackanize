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
    print(tokens)
    if tokenizer.error: sys.exit(1)
    
if __name__ == '__main__':
    main()
