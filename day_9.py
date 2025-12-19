import math
from itertools import combinations


def _reader(filename: str) -> set[tuple[int, ...]]:
    with open(filename, "r") as file:
        tiles = {
            tuple(int(position) for position in line.strip().split(","))
            for line in file.readlines()
        }
    return tiles


def _area(pair: tuple[tuple[int, ...], tuple[int, ...]]) -> float:
    return math.prod(abs(pair[0][i] - pair[1][i]) + 1 for i in range(2))


def solver(filename: str) -> None:
    tiles = _reader(filename)
    print(f"Part 1: {max(_area(pair) for pair in combinations(tiles, 2))}")
