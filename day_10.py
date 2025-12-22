import itertools


def _reader(filename):
    with open(filename, "r") as file:
        machines = []
        for line in file:
            lights_, rest = line.strip("[").split("] (")
            lights = tuple(int(char == "#") for char in lights_)
            buttons_, joltages_ = rest.strip("}\n").split(") {")
            buttons = {
                tuple(int(light) for light in button.split(","))
                for button in buttons_.split(") (")
            }
            joltages = tuple(int(joltage) for joltage in joltages_.split(","))
            machines.append((lights, buttons, joltages))
    return machines


def solver(filename) -> None:
    machines = _reader(filename)
    part_1 = 0
    for lights, buttons, _ in machines:
        for i, combination in (
            (i_, combination_)
            for i_ in range(len(buttons))
            for combination_ in itertools.combinations(buttons, i_)
        ):
            if lights == tuple(
                sum(int(i in button) for button in combination) % 2
                for i in range(len(lights))
            ):
                part_1 += i
                break
    print(f"Part 1: {part_1}")
