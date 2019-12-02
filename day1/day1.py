def calculate_fuel(mass: int, with_fuel=True) -> int:
    fuel = 0
    new_mass = (mass // 3) - 2
    if not with_fuel:
        return new_mass
    while new_mass >= 0:
        fuel += new_mass
        new_mass = (new_mass // 3) - 2
    return fuel

def test_calculate_fuel():
    assert calculate_fuel(12, False) == 2
    assert calculate_fuel(14, False) == 2
    assert calculate_fuel(1969, False) == 654
    assert calculate_fuel(100756, False) == 33583
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 966
    assert calculate_fuel(100756) == 50346

if __name__ == "__main__":
    print("Starting tests...")
    try:
        test_calculate_fuel()
    except AssertionError as e:
        print("Tests failed.")
        print(e)
        exit(1)
    print("Calculating Part 1")
    with open("input") as infile:
        fuel = [calculate_fuel(int(line), False) for line in infile]
    print(sum(fuel))
    print("Calculating Part 2")
    with open("input") as infile:
        fuel = [calculate_fuel(int(line)) for line in infile]
    print(sum(fuel))
