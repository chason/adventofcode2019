from typing import List
from itertools import product


def process_op(opcode: int, x: int, y: int) -> int:
    if opcode == 1:
        return x + y
    if opcode == 2:
        return x * y
    raise ValueError(f"bad opcode: {opcode}")

def intcode(opcodes: List[int]) -> List[int]:
    newop = opcodes[:]
    pos = 0
    while newop[pos] != 99:
        newop[newop[pos+3]] = process_op(newop[pos], newop[newop[pos+1]], newop[newop[pos+2]])
        pos += 4
    return newop

def run_program(memory, noun, verb):
    # make a shallow copy so we don't overwrite original list
    memory = memory[:]
    memory[1] = noun
    memory[2] = verb
    return intcode(memory)[0]

def test_intcode():
    assert intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]


if __name__ == "__main__":
    print("Starting tests...")
    try:
        test_intcode()
    except AssertionError as e:
        print("Tests failed")
        print(e)
        exit(1)

    with open("input") as infile:
        memory = [int(x) for x in infile.readline().split(',')]
        print("Calculating Part 1...")
        print("answer: {}".format(run_program(memory, 12, 2)))
        print("Calculating Part 2...")
        for noun, verb in product(range(100), range(100)):
            if run_program(memory, noun, verb) == 19690720:
                print(100 * noun + verb)
                exit(0)
