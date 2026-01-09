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
    start: str,
    end: str,
    excluded: tuple[str, ...],
) -> int:
    if start in excluded:
        return 0
    if start == end:
        return 1
    return sum(
        _searcher(start=connection, end=end, excluded=excluded)
        for connection in CONNECTIONS[start]
    )


def solver(filename: str) -> None:
    _reader(filename)
    print(f"Part 1: {_searcher(start='you', end='out', excluded=())}")
    paths_svr_dac = _searcher(start="svr", end="dac", excluded=("fft", "out"))
    paths_svr_fft = _searcher(start="svr", end="fft", excluded=("dac", "out"))
    paths_dac_fft = _searcher(start="dac", end="fft", excluded=("svr", "out"))
    paths_fft_dac = _searcher(start="fft", end="dac", excluded=("svr", "out"))
    paths_dac_out = _searcher(start="dac", end="out", excluded=("svr", "fft"))
    paths_fft_out = _searcher(start="fft", end="out", excluded=("svr", "dac"))
    print(
        f"Part 2: {paths_svr_dac * paths_dac_fft * paths_fft_out + paths_svr_fft * paths_fft_dac * paths_dac_out}"
    )
