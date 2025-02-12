class AInstruction:
    def __init__(self, value):
        self.value = value

    def toString(self):
        print(f"@{value}") 

    def type(self):
        return 'A'

class Parser:
    instruction = []
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def isEnd(self):
        return self.tokens[self.current][0] == "EOF"

    def advance(self):
        if self.isEnd(): return None
        token = self.peek()
        self.current += 1
        return token

    def peek(self):
        if self.isEnd(): return None
        return self.tokens[self.current]

    def parse(self): 
        instructions = []
        while not self.isEnd():
            if self.peek()[0] == '@': 
                inst = self.parseAInstraction()
                if inst: instructions.append(inst)

        return instructions

    
    def parseAInstraction(self):
        self.advance();
        value, line = self.advance()
        if not value[0].isdigit():
            print(f"Error: Expect Number '{value}' found at line '{line}'")
            self.error = True
            return None

        return AInstruction(value) 
