from functools import cache


def _reader(filename: str) -> tuple[tuple[int, int], frozenset[tuple[int, int]]]:
    with open(filename, "r") as file:
        lines = file.readlines()

    splitter = frozenset(
        (x, y)
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "^"
    )
    [start] = [
        (x, y)
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "S"
    ]
    return start, splitter


def _next(
    beam: tuple[int, int], splitter: frozenset[tuple[int, int]]
) -> list[tuple[int, int]]:
    next_splitter = []
    for x in (beam[0] - 1, beam[0] + 1):
        try:
            next_splitter.append(
                (x, min(y_ for x_, y_ in splitter if x_ == x and y_ >= beam[1]))
            )
        except ValueError:
            continue
    return next_splitter


@cache
def _recursor(beam: tuple[int, int], splitter: frozenset[tuple[int, int]]) -> int:
    next_splitter = _next(beam, splitter)
    return (
        2
        - len(next_splitter)
        + sum(_recursor(beam=beam, splitter=splitter) for beam in next_splitter)
    )


def solver(filename: str) -> None:
    start, splitter = _reader(filename)

    # BFS
    splits = 0
    beams = [start]
    visited_splitter = set()
    while beams:
        beam = beams.pop()
        if beam in visited_splitter:
            continue
        visited_splitter.add(beam)
        splits += 1
        beams.extend(_next(beam=beam, splitter=splitter))
    print(f"Part 1: {splits}")

    # DFS as recursive function
    print(
        f"Part 2: {
            _recursor(
                beam=(
                    start[0],
                    min(y for x, y in splitter if x == start[0] and y >= start[1]),
                ),
                splitter=splitter,
            )
        }"
    )
