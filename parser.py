class AInstruction:
    def __init__(self, value):
        self.value = value

    def toString(self):
        return f"@{self.value}" 

    def getType(self):
        return 'A'

class LInstruction:
    def __init__(self, value):
        self.value = value

    def toString(self):
        return f"({self.value})" 

    def getType(self):
        return 'L'

class CInstruction:
    def __init__(self, dest, comp, jump):
        self.dest = dest
        self.comp = comp 
        self.jump = jump 
        
    def toString(self):
        return f"{self.dest}={self.comp};{self.jump}" 

    def getType(self):
        return 'C'

class Parser:
    instruction = []
    def __init__(self, tokens):
        self.tokens = tokens
        self.error = False
        self.current = 0

    def isEnd(self):
        return self.tokens[self.current][0] == "EOF"

    def advance(self):
        token = self.peek()
        if not self.isEnd(): self.current += 1
        return token

    def peek(self):
        return self.tokens[self.current]

    def peekNext(self):
        if self.isEnd(): return self.tokens[self.current]
        return self.tokens[self.current + 1]

    def sync(self):
        instStarts = [
            '@', '(',
            '0', '-', 'D',
            'A', '!', 'M',
            'AD', 'AM', 'DM',
            'ADM', 'EOF'
        ]

        while self.peek()[0] not in instStarts:
            self.advance()

    def reportError(self, message):
            print(message)
            self.error = True
            self.sync()

    def parse(self): 
        instructions = []
        while not self.isEnd():
            inst = None
            if self.peek()[0] == '@': inst = self.parseAInstruction()
            elif self.peek()[0] == '(': inst = self.parseLInstruction()
            else: inst = self.parseCInstruction()
            if inst: instructions.append(inst)
                
        return instructions

    
    def parseAInstruction(self):
        self.advance();
        value, line = self.peek()
        if not value[0].isalpha() and not value.isdigit():
            self.reportError(f"Error: Expect symbol '{value}' found at line '{line}'")
            return None

        self.advance()
        return AInstruction(value) 

    def parseLInstruction(self):
        self.advance();
        value, line = self.peek()
        if not value[0].isalpha() and not value.isdigit():
            self.reportError(f"Error: Expect symbol '{value}' found at line {line}")
            return None

        self.advance()

        right_paren, line = self.peek()
        if right_paren != ')':
            self.reportError(f"Error: Expect ')' for label end at line {line}")
            return None
        
        self.advance()
        return LInstruction(value) 

    def parseComp(self):
        comp, instLine = self.advance()
        if comp  == '0' or comp  == '1': return comp

        if comp == '-':
            c, line = self.peek()
            if c != '1' and c != 'A' and c != 'D' and c != 'M':
                msg = f"Error: Expact (1 | A | D | M) after '-' at line {line}"
                self.reportError(msg)
                return None

            comp += c
            self.advance()
            return comp

        if comp == '!':
            c, line = self.peek()
            if c != 'A' and c != 'D' and c != 'M':
                msg = f"Error: Expact (A | D | M) after '!' at line {line}"
                self.reportError(msg)
                return None

            comp += c
            self.advance()
            return comp
        
        if comp == 'D':
            c, line = self.peek()
            if c != '-' and c != '+' and c != '&' and c != '|':
                return comp 

            comp += c
            self.advance()

            c, line = self.peek()
            if c != '1' and c != 'A' and c != 'M':
                msg = f"Error: Expact (1 | A | M) after '{comp[-1]}' at line {line}"
                self.reportError(msg)
                return None

            comp += c
            self.advance()
            return comp

        if comp == 'A':
            c, line = self.peek()
            if c != '-' and c != '+':
                return comp 

            comp += c
            self.advance()

            c, line = self.peek()
            if c != '1' and c != 'D':
                msg = f"Error: Expact (1 | D) after '{comp[-1]}' at line {line}"
                self.reportError(msg)
                return None

            comp += c
            self.advance()
            return comp

        if comp == 'M':
            c, line = self.peek()
            if c != '-' and c != '+':
                return comp 

            comp += c
            self.advance()

            c, line = self.peek()
            if c != '1' and c != 'D':
                msg = f"Error: Expact (1 | D) after '{comp[-1]}' at line {line}"
                self.reportError(msg)
                return None

            comp += c
            self.advance()
            return comp
        
        msg = f"Error: no valid computation starts with '{comp}' at line {instLine}"
        self.reportError(msg)
        return None

    def parseCInstruction(self):
        dest, comp, jump = None, None, None
        if self.peekNext()[0] == '=':
            dest = self.advance()[0]
            self.advance()

        comp = self.parseComp()
        if comp == None: return None

        if self.peek()[0] == ';':
            self.advance()
            jump = self.advance()[0]

        return CInstruction(dest, comp, jump)

