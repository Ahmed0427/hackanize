class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.error = False
        self.current = 0
        self.line = 1 

    def isEnd(self):
        return self.current == len(self.source)

    def advance(self):
        if self.isEnd(): return None
        curChar = self.peek()
        self.current += 1
        return curChar

    def peek(self):
        if self.isEnd(): return None
        return self.source[self.current]

    def skipWhiteSpaces(self):
        while(True):
            c = self.peek()
            if (c == ' ' or c == '\r' or c == '\t'): self.advance()
            elif (c == '\n'):
                self.line += 1
                self.advance()
            elif (c == '/'):
                self.advance()
                if self.peek() == '/':
                    while self.peek() != '\n': self.advance()
                else:
                    return self.makeError(c)

            else: return

    def makeError(self, c):
        self.error = True
        print(f"Error: unknown symbol '{c}' at Line {self.line}")
        return self.makeToken("ERROR")


    def makeToken(self, lexeme):
        return (lexeme, self.line)

    def getNextToken(self):
        self.skipWhiteSpaces()

        if self.isEnd(): return self.makeToken("EOF")

        c = self.advance();

        if c == '@': return self.makeToken(c)
        elif c == '(': return self.makeToken(c)
        elif c == ')': return self.makeToken(c)
        elif c == '-': return self.makeToken(c)
        elif c == '+': return self.makeToken(c)
        elif c == '&': return self.makeToken(c) 
        elif c == '|': return self.makeToken(c) 
        elif c == '!': return self.makeToken(c) 
        elif c == '=': return self.makeToken(c) 
        elif c == ';': return self.makeToken(c) 
        elif c == '$': return self.makeToken(c) 
        elif c == '.': return self.makeToken(c) 
        elif (c == 'D' or c == 'M' or c == 'A'):
            reg = c
            if self.peek() == 'A':
                reg += self.advance()
            if self.peek() == 'M':
                reg += self.advance()
            if self.peek() == 'D':
                reg += self.advance()
            if self.peek() == 'A':
                reg += self.advance()
            if self.peek() == 'M':
                reg += self.advance()
            if self.peek() == 'D':
                reg += self.advance()

            return self.makeToken(reg)

        elif c == 'J':
            jump = c
            if self.peek() == 'G':
                jump += self.advance()
                if self.peek() == 'T':
                    jump += self.advance()
                elif self.peek() == 'E':
                    jump += self.advance()

            elif self.peek() == 'L': 
                jump += self.advance()
                if self.peek() == 'T':
                    jump += self.advance()
                elif self.peek() == 'E':
                    jump += self.advance()

            elif self.peek() == 'E':
                jump += self.advance()
                if self.peek() == 'Q':
                    jump += self.advance()

            elif self.peek() == 'N':
                jump += self.advance()
                if self.peek() == 'E':
                    jump += self.advance()

            elif self.peek() == 'M':
                jump += self.advance()
                if self.peek() == 'P':
                    jump += self.advance()

            if len(jump) != 3: return self.makeError(jump)
            return self.makeToken(jump)
            
        elif c.isdigit():
            number = c
            while not self.isEnd() and self.peek().isdigit():
                number += self.advance()

            return self.makeToken(number)

        elif c.isalpha():
            ident = c
            while not self.isEnd() and (self.peek().isalnum() or
                                        self.peek() == '_' or
                                        self.peek() == '$' or
                                        self.peek() == '.'):
                ident += self.advance()

            return self.makeToken(ident)

        else:
            return self.makeError(c)
        
    
    def getTokens(self):
        tokens = []
        # (lexeme, line)
        token = (None, None)
        while token[0] != "EOF":
            token = self.getNextToken()
            tokens.append(token)
            if token == "EOF":
                break


        return tokens

