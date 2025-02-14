class Generator:
    def __init__(self, instructions):
        self.instructions = instructions
        self.dest = {}
        self.comp = {}
        self.jump = {}
        self.initTables()

    def initTables(self):
        self.dest[None] = '000' 
        self.dest['M'] = '001' 
        self.dest['D'] = '010' 
        self.dest['MD'] = '011' 
        self.dest['DM'] = '011' 
        self.dest['A'] = '100' 
        self.dest['AM'] = '101' 
        self.dest['MA'] = '101' 
        self.dest['AD'] = '110' 
        self.dest['DA'] = '110' 
        self.dest['MDA'] = '111' 
        self.dest['MAD'] = '111' 
        self.dest['AMD'] = '111' 
        self.dest['ADM'] = '111' 
        self.dest['DAM'] = '111' 
        self.dest['DMA'] = '111'

        self.comp['0'] = '0101010'
        self.comp['1'] = '0111111'
        self.comp['-1'] = '0111010'
        self.comp['D'] = '0001100'
        self.comp['A'] = '0110000'
        self.comp['M'] = '1110000'
        self.comp['!D'] = '0001101'
        self.comp['!A'] = '0110001'
        self.comp['!M'] = '1110001'
        self.comp['-D'] = '0001111'
        self.comp['-A'] = '0110011'
        self.comp['-M'] = '1110011'
        self.comp['D+1'] = '0011111'
        self.comp['A+1'] = '0110111'
        self.comp['M+1'] = '1110111'
        self.comp['D-1'] = '0001110'
        self.comp['A-1'] = '0110010'
        self.comp['M-1'] = '1110010'
        self.comp['D+A'] = '0000010'
        self.comp['A+D'] = '0000010'
        self.comp['D+M'] = '1000010'
        self.comp['M+D'] = '1000010'
        self.comp['D-A'] = '0010011'
        self.comp['D-M'] = '1010011'
        self.comp['A-D'] = '0000111'
        self.comp['M-D'] = '1000111'
        self.comp['D&A'] = '0000000'
        self.comp['A&D'] = '0000000'
        self.comp['D&M'] = '1000000'
        self.comp['M&D'] = '1000000'
        self.comp['D|A'] = '0010101'
        self.comp['A|D'] = '0010101'
        self.comp['D|M'] = '1010101'
        self.comp['M|D'] = '1010101'

        self.jump[None] = '000'
        self.jump['JGT'] = '001'
        self.jump['JEQ'] = '010'
        self.jump['JGE'] = '011'
        self.jump['JLT'] = '100'
        self.jump['JNE'] = '101'
        self.jump['JLE'] = '110'
        self.jump['JMP'] = '111'

    def generate(self):
        binList = []
        for inst in self.instructions:
            if inst.getType() == 'A':
                binList.append(bin(int(inst.value))[2:].zfill(16))
            elif inst.getType() == 'C':
                res = '111' 
                res += self.comp[inst.comp]
                res += self.dest[inst.dest]
                res += self.jump[inst.jump]
                binList.append(res)

        return binList
