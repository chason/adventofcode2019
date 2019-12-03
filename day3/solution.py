#!/usr/bin/env python3

from typing import List, Set, Tuple, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


Instruction = Tuple[str, int]
Wire = Set[Point]


def gen(line: str) -> List[Instruction]:
    return [(inst[0], int(inst[1:])) for inst in line.split(',')]


def solution(instructions: List[List[Instruction]]) -> int:
    wires = [create_wire(wire) for wire in instructions]
    intersections: Set[Point] = set()
    start_wire, other_wires = wires[0], wires[1:]
    for wire in other_wires:
        intersections.update(start_wire & wire)

    distances: List[int] = []
    for point in intersections:
        if point != Point(0, 0):
            distance = taxicab_distance(Point(0, 0), point)
            print(f"Point: {point}, Distance: {distance}")
            distances.append(distance)
    return min(distances)


def taxicab_distance(start: Point, end: Point) -> int:
    return abs(start.x - end.x) + abs(start.y - end.y)


def create_wire(instructions: List[Instruction]) -> Wire:
    start = Point(0, 0)
    wire = set()
    for direction, length in instructions:
        if direction == 'U':
            for x in range(length):
                new_point = Point(start.x + x, start.y)
                wire.add(new_point)
        elif direction == 'D':
            for x in range(length):
                new_point = Point(start.x - x, start.y)
                wire.add(new_point)
        elif direction == 'L':
            for y in range(length):
                new_point = Point(start.x, start.y - y)
                wire.add(new_point)
        elif direction == 'R':
            for y in range(length):
                new_point = Point(start.x, start.y + y)
                wire.add(new_point)
        else:
            raise ValueError(f"Invalid direction: {direction}")
        start = new_point

    return wire


def test_solution():
    data1_1 = [('R', 8), ('U', 5), ('L', 5), ('D', 3)]
    data1_2 = [('U', 7), ('R', 6), ('D', 4), ('L', 4)]
    print(solution([data1_1, data1_2]))
    assert solution([data1_1, data1_2]) == 6

    data2_1 = [('R', 75), ('D', 30), ('R', 83), ('U', 83), ('L', 12), ('D', 49), ('R', 71), ('U', 7), ('L', 72)]
    data2_2 = [('U', 62), ('R', 66), ('U', 55), ('R', 34), ('D', 71), ('R', 55), ('D', 58), ('R', 83)]
    print(solution([data2_1, data2_2]))
    assert solution([data2_1, data2_2]) == 159

    data3_1 = [('R', 98), ('U', 47), ('R', 26), ('D', 63), ('R', 33), ('U', 87), ('L', 62), ('D', 20), ('R', 33), ('U', 53), ('R', 51)]
    data3_2 = [('U', 98), ('R', 91),( 'D', 20), ('R', 16), ('D', 67), ('R', 40), ('U', 7), ('R', 15), ('U', 6), ('R', 7)]
    print(solution([data3_1, data3_2]))
    assert solution([data3_1, data3_2]) == 135


if __name__ == '__main__':
    print("Starting tests...")
    try:
        test_solution()
    except AssertionError as e:
        print("Tests failed.")
        print(e)
        exit(1)

    instructions = []
    with open('input') as infile:
        for line in infile.readlines():
            instructions.append(gen(line))

    p1_sol = solution(instructions)
    print(f"Solution for Part 1: {p1_sol}")
