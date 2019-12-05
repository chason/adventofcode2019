from typing import List, Tuple


def read_input() -> str:
    return input('Program requires input: ')


def get_parameters(modes: str, params: List[str], memory: List[str]) -> List[str]:
    result = ['', '']
    for idx, mode in enumerate(modes):
        if mode == '1':
            result[idx] = params[idx]
        try:
            result[idx] = memory[int(params[idx])]
        except IndexError:
            # This is probably a '4' so we quit early
            return result

    return result


def computer(memory: List[str]):
    memory = memory[:]
    pos = 0
    while (opcode := memory[pos].zfill(5)) != '00099':
        opcode = opcode[::-1]
        print(f"Processing: {memory[pos:pos + 4]}")
        if opcode[0] == '1':
            x, y, loc = [int(val) for val in memory[pos+1:pos+4]]
            if opcode[2] == '0':
                x = int(memory[x])
            if opcode[3] == '0':
                y = int(memory[y])
            memory[loc] = str(x + y)
            pos += 4
        elif opcode[0] == '2':
            x, y, loc = [int(val) for val in memory[pos+1:pos+4]]
            if opcode[2] == '0':
                x = int(memory[x])
            if opcode[3] == '0':
                y = int(memory[y])
            memory[loc] = str(x * y)
            pos += 4
        elif opcode[0] == '3':
            loc = int(memory[pos+1])
            memory[loc] = read_input()
            pos += 2
        elif opcode[0] == '4':
            loc = int(memory[pos+1])
            print(memory[loc])
            pos += 2
        elif opcode[0] == '5':
            x, y = [int(val) for val in memory[pos+1:pos+3]]
            if opcode[2] == '0':
                x = int(memory[x])
            if opcode[3] == '0':
                y = int(memory[y])
            if bool(x):
                pos = y
            else:
                pos += 3
        elif opcode[0] == '6':
            x, y = [int(val) for val in memory[pos+1:pos+3]]
            if opcode[2] == '0':
                x = int(memory[x])
            if opcode[3] == '0':
                y = int(memory[y])
            if bool(x):
                pos += 3
            else:
                pos = y
        elif opcode[0] == '7':
            x, y, loc = [int(val) for val in memory[pos+1:pos+4]]
            if opcode[2] == '0':
                x = int(memory[x])
            if opcode[3] == '0':
                y = int(memory[y])
            if x < y:
                memory[loc] = '1'
            else:
                memory[loc] = '0'
            pos += 4
        elif opcode[0] == '8':
            x, y, loc = [int(val) for val in memory[pos+1:pos+4]]
            if opcode[2] == '0':
                x = int(memory[x])
            if opcode[3] == '0':
                y = int(memory[y])
            if x == y:
                memory[loc] = '1'
            else:
                memory[loc] = '0'
            pos += 4
        else:
            print(f"Illegal opcode: {opcode}")
            exit(1)

        # ignore the first mode for now
        # modes, instruction = opcode[1:3], opcode[-2:]
        #
        # loc = memory[pos+3]
        #
        # if instruction == '01':
        #     memory[int(loc)] = str(int(x) + int(y))
        #     pos += 4
        #
        # elif instruction == '02':
        #     memory[int(loc)] = str(int(x) * int(y))
        #     pos += 4
        #
        # elif instruction == '03':
        #     memory[int(loc)] = read_input()
        #     pos += 2
        #
        # elif instruction == '04':
        #     import pdb; pdb.set_trace()
        #     print(x)
        #     pos += 2


def gen(program: str) -> List[str]:
    return program.split(',')


def main():
    with open('input') as infile:
        computer(gen(infile.readline()))


if __name__ == '__main__':
    main()
