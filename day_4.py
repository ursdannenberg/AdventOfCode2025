from typing import TypeAlias


DIRS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

Rolls: TypeAlias = set[tuple[int, int]]


def _reader(filename: str) -> Rolls:
    with open(filename, "r") as file:
        rolls = {
            (x, y)
            for y, line in enumerate(file.readlines())
            for x, char in enumerate(line)
            if char == "@"
        }
    return rolls


def _finder(rolls: Rolls) -> Rolls:
    return {
        roll
        for roll in rolls
        if sum(
            tuple(r + d for r, d in zip(roll, di, strict=True)) in rolls for di in DIRS
        )
        < 4
    }


def solver(filename: str) -> None:
    rolls = _reader(filename)
    rolls_remove = _finder(rolls)
    print(f"Part 1: {len(rolls_remove)}")
    part_2 = len(rolls_remove)
    while len(rolls_remove) > 0:
        rolls -= rolls_remove
        rolls_remove = _finder(rolls)
        part_2 += len(rolls_remove)
    print(f"Part 2: {part_2}")
