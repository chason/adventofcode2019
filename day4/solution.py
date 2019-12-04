from typing import List


def gen(puzzle_input: str) -> List[str]:
    start, end = puzzle_input.split('-', maxsplit=1)
    return [str(num) for num in range(int(start), int(end))]


def meets_criteria(candidate: str) -> bool:
    if ''.join(sorted(candidate)) != candidate:
        return False
    for digit in candidate:
        if (digit*2) in candidate:
            return True
    return False


def meets_criteria_part_two(candidate: str) -> bool:
    if ''.join(sorted(candidate)) != candidate:
        return False
    for digit in candidate:
        if (digit*2) in candidate and (digit*3) not in candidate:
            return True
    return False


def test_meets_criteria():
    assert meets_criteria('111111') is True
    assert meets_criteria('223450') is False
    assert meets_criteria('123789') is False


def test_meets_criteria_part_two():
    print("1")
    assert meets_criteria_part_two('112233') is True
    print("2")
    assert meets_criteria_part_two('123444') is False
    print("3")
    assert meets_criteria_part_two('111122') is True


def solution_part_one(candidates: List[str]) -> int:
    return sum(meets_criteria(candidate) for candidate in candidates)


def solution_part_two(candidates: List[str]) -> int:
    return sum(meets_criteria_part_two(candidate) for candidate in candidates)


def main():
    print("Running Tests...")
    try:
        test_meets_criteria()
        test_meets_criteria_part_two()
    except AssertionError:
        print("Tests failed.")
        exit(1)

    input_range = "158126-624574"
    candidates = gen(input_range)

    passwords = solution_part_one(candidates)
    print(f"Part 1 Solution: {passwords}")

    passwords_part_two = solution_part_two(candidates)
    print(f"Part 2 Solution: {passwords_part_two}")


if __name__ == "__main__":
    main()
