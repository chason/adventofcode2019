from typing import List, Tuple


def read_input() -> int:
    return int(input('Program requires input: '))


def computer(memory: List[int]):
    memory = memory[:]
    pos = 0
    while (opcode := str(memory[pos]).zfill(5)) != '00099':
        opcode = opcode[::-1]
        print(f"Processing: {memory[pos:pos + 4]}")
        if opcode[0] == '1':
            x, y, loc = memory[pos+1:pos+4]
            if opcode[2] == '0':
                x = memory[x]
            if opcode[3] == '0':
                y = memory[y]
            memory[loc] = x + y
            pos += 4
        elif opcode[0] == '2':
            x, y, loc = memory[pos+1:pos+4]
            if opcode[2] == '0':
                x = memory[x]
            if opcode[3] == '0':
                y = memory[y]
            memory[loc] = x * y
            pos += 4
        elif opcode[0] == '3':
            loc = memory[pos+1]
            memory[loc] = read_input()
            pos += 2
        elif opcode[0] == '4':
            loc = memory[pos+1]
            print(memory[loc])
            pos += 2
        elif opcode[0] == '5':
            x, y = memory[pos+1:pos+3]
            if opcode[2] == '0':
                x = memory[x]
            if opcode[3] == '0':
                y = memory[y]
            if bool(x):
                pos = y
            else:
                pos += 3
        elif opcode[0] == '6':
            x, y = memory[pos+1:pos+3]
            if opcode[2] == '0':
                x = memory[x]
            if opcode[3] == '0':
                y = memory[y]
            if bool(x):
                pos += 3
            else:
                pos = y
        elif opcode[0] == '7':
            x, y, loc = memory[pos+1:pos+4]
            if opcode[2] == '0':
                x = memory[x]
            if opcode[3] == '0':
                y = memory[y]
            if x < y:
                memory[loc] = 1
            else:
                memory[loc] = 0
            pos += 4
        elif opcode[0] == '8':
            x, y, loc = memory[pos+1:pos+4]
            if opcode[2] == '0':
                x = memory[x]
            if opcode[3] == '0':
                y = memory[y]
            if x == y:
                memory[loc] = 1
            else:
                memory[loc] = 0
            pos += 4
        else:
            print(f"Illegal opcode: {opcode}")
            exit(1)


def gen(program: str) -> List[int]:
    return [int(x) for x in program.split(',')]


def main():
    with open('input') as infile:
        computer(gen(infile.readline()))


if __name__ == '__main__':
    main()
