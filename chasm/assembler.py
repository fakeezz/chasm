import re

symbols = [
    { 'pattern': r'SYS0x([\d\a-fA-F]{3})', 'opcode': '0NNN' },
    { 'pattern': 'CLS', 'opcode': '00E0'},
    { 'pattern': 'RET', 'opcode': '00EE'},
    { 'pattern': r'JMP0x([\d\a-fA-F]{3}),V[\da-fA-F]{1}', 'opcode': 'BNNN' },
    { 'pattern': r'JMP0x([\d\a-fA-F]{3})', 'opcode':  '1NNN' },
    { 'pattern': r'CALL0x([\d\a-fA-F]{3})', 'opcode': '2NNN' },
    { 'pattern': r'SEV([\da-fA-F]{1}),0x([\da-fA-F]{2})', 'opcode': '3XNN' },
    { 'pattern': r'SEV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '5XY0' },
    { 'pattern': r'SNEV([\da-fA-F]{1}),0x([\da-fA-F]{2})', 'opcode': '4XNN' },
    { 'pattern': r'SNEV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '9XY0' },
    { 'pattern': r'ADDV([\da-fA-F]{1}),0x([\da-fA-F]{2})', 'opcode': '7XNN' },
    { 'pattern': r'ADDV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY4' },
    { 'pattern': r'ORV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY1' },
    { 'pattern': r'ANDV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY2' },
    { 'pattern': r'XORV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY3' },
    { 'pattern': r'SUBV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY5' },
    { 'pattern': r'SHRV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY6' },
    { 'pattern': r'SUBCV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY7' },
    { 'pattern': r'SHLV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XYE' },
    { 'pattern': r'LDI0x([\d\a-fA-F]{3})', 'opcode': 'ANNN' },
    { 'pattern': r'RNDV([\da-fA-F]{1}),0x([\da-fA-F]{2})', 'opcode': 'CXNN' },
    { 'pattern': r'DRWV([\da-fA-F]{1}),V([\da-fA-F]{1}),0x([\da-fA-F]{1})', 'opcode': 'DXYN' },
    { 'pattern': r'SKPV([\da-fA-F]{1})', 'opcode': 'EX9E' },
    { 'pattern': r'SKNPV([\da-fA-F]{1})', 'opcode': 'EXA1' },
    { 'pattern': r'STRV([\da-fA-F]{1})', 'opcode': 'FX55' },
    { 'pattern': r'FILLV([\da-fA-F]{1})', 'opcode': 'FX65' },

    { 'pattern': r'LDV([\da-fA-F]{1}),0x([\da-fA-F]{2})', 'opcode': '6XNN' },
    { 'pattern': r'LDV([\da-fA-F]{1}),V([\da-fA-F]{1})', 'opcode': '8XY0' },
    { 'pattern': r'LDV([\da-fA-F]{1}),DT', 'opcode': 'FX07' },
    { 'pattern': r'LDV([\da-fA-F]{1}),K', 'opcode': 'FX0A' },
    { 'pattern': r'LDDT,V([\da-fA-F]{1})', 'opcode': 'FX15' },
    { 'pattern': r'LDST,V([\da-fA-F]{1})', 'opcode': 'FX18' },
    { 'pattern': r'LDI,V([\da-fA-F]{1})', 'opcode': 'FX1E' },
    { 'pattern': r'LDF,V([\da-fA-F]{1})', 'opcode': 'FX29' },
    { 'pattern': r'LDB,V([\da-fA-F]{1})', 'opcode': 'FX33' },
]


def compile(ast):
    opcodes = []
    for node in ast.nodes:
        instruction = ''.join([i['value'] for i in node])
        for symbol in symbols:
            match = re.match(symbol['pattern'], instruction)
            if match:
                opcode = symbol['opcode']
                if 'NNN' in symbol['opcode']:
                    opcode = opcode.replace('NNN', match.group(1))
                elif 'NN' in symbol['opcode']:
                    opcode = opcode.replace('NN', match.group(2))
                elif 'N' in symbol['opcode']:
                    opcode = opcode.replace('N', match.group(3))

                if 'X' in symbol['opcode']:
                    opcode = opcode.replace('X', match.group(1))
                if 'Y' in symbol['opcode']:
                    opcode = opcode.replace('Y', match.group(2))
                opcodes.append(opcode.upper())
    return opcodes
