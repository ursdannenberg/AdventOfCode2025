def _reader(filename: str) -> tuple[int, ...]:
    with open(filename, "r") as file:
        instructions = tuple(
            -int(instruction[1:]) if instruction[0] == "L" else int(instruction[1:])
            for instruction in file.readlines()
        )
    return instructions


def solver(filename: str) -> None:
    dial, part_1, part_2 = 50, 0, 0
    for instruction in _reader(filename):
        part_2 += abs((dial + instruction) // 100 - dial // 100)
        if instruction < 0:
            part_2 -= dial % 100 == 0
        dial += instruction
        part_1 += dial % 100 == 0
        if instruction < 0:
            part_2 += dial % 100 == 0
    print(f"Part 1: {part_1}")
    print(f"Part 1: {part_2}")
