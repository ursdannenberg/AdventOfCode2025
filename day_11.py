from functools import cache

CONNECTIONS: dict[str, tuple[str, ...]] = {}

def _reader(filename: str) -> None:
    global CONNECTIONS
    with open(filename, "r") as file:
        CONNECTIONS = {
            (devices := line.strip().split(": "))[0]: tuple(devices[1].split())
            for line in file
        }


@cache
def _searcher(
    start,
    end,
    paths: tuple[tuple[str, ...], ...],
) -> tuple[tuple[str, ...], ...]:
    paths = tuple((*path, start) for path in paths)
    if start == end:
        return paths
    return tuple(
        path
        for connection in CONNECTIONS[start]
        for path in _searcher(connection, end, paths)
    )


def solver(filename: str) -> None:
    _reader(filename)
    print(f"Part 1: {len(_searcher("you", "out", ((),)))}")
    # paths = _searcher("svr", "out", ((),))
    # print(f"Part 2: {len(tuple(path for path in paths if all(device in path for device in ('dac', 'fft'))))}")
