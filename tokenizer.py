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
        return self.token("ERROR")


    def token(self, lexeme):
        return (lexeme, self.line)

    def getNextToken(self):
        self.skipWhiteSpaces()

        if self.isEnd(): return self.token("EOF")

        c = self.advance();

        if c == '@': return self.token(c)
        elif c == '(': return self.token(c)
        elif c == ')': return self.token(c)
        elif c == '-': return self.token(c)
        elif c == '+': return self.token(c)
        elif c == '&': return self.token(c) 
        elif c == '|': return self.token(c) 
        elif c == '!': return self.token(c) 
        elif c == '=': return self.token(c) 
        elif c == ';': return self.token(c) 
        elif c == '$': return self.token(c) 
        elif c == '.': return self.token(c) 
        elif c == 'M': return self.token(c)
        elif c == 'D':
            reg = c
            if self.peek() == 'M':
                reg += self.advance()

            return self.token(reg)

        elif c == 'A':
            reg = c
            if self.peek() == 'D':
                reg += self.advance();
                if self.peek() == 'M':
                    reg += self.advance();
            elif self.peek() == 'M':
                reg += self.advance()

            return self.token(reg)

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
            return self.token(jump)
            
        elif c.isdigit():
            number = c
            while not self.isEnd() and self.peek().isdigit():
                number += self.advance()

            return self.token(number)

        elif c.isalpha():
            ident = c
            while not self.isEnd() and (self.peek().isalnum() or self.peek() == '_'):
                ident += self.advance()

            return self.token(ident)

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

