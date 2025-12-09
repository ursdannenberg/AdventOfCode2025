import math
from itertools import combinations, count


NUM_CONNECTIONS = 1000


def _reader(filename: str) -> set[tuple[int, ...]]:
    with open(filename, "r") as file:
        boxes = {
            tuple(int(position) for position in line.strip().split(","))
            for line in file.readlines()
        }
    return boxes


def _dist(pair: tuple[tuple[int, int, int], tuple[int, int, int]]) -> float:
    # The actual straight-line distance would be the square root of the returned value,
    # but this doesn't affect the order.
    return sum((pair[0][i] - pair[1][i]) ** 2 for i in range(3))


def solver(filename: str) -> None:
    boxes = _reader(filename)
    pairs = sorted(combinations(boxes, 2), key=lambda x: _dist(x), reverse=True)
    circuits = {(box,) for box in boxes}
    for i in count():
        first, second = pairs.pop()
        [circuit_first] = [circuit for circuit in circuits if first in circuit]
        [circuit_second] = [circuit for circuit in circuits if second in circuit]
        if circuit_first != circuit_second:
            circuits -= {circuit_first, circuit_second}
            circuits.add((*circuit_first, *circuit_second))
        if i == NUM_CONNECTIONS:
            print(
                f"Part 1: {
                    math.prod(
                        len(circuit)
                        for circuit in sorted(
                            circuits, key=lambda x: len(x), reverse=True
                        )[:3]
                    )
                }"
            )
        if len(circuits) == 1:
            print(f"Part 2: {first[0] * second[0]}")
            break
