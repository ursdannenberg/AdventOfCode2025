def _reader(filename: str) -> tuple[str, ...]:
    with open(filename, "r") as file:
        ranges = tuple(ran.split("-") for ran in file.readlines()[0].split(","))
        ids = tuple(
            str(eid) for begin, end in ranges for eid in range(int(begin), int(end) + 1)
        )
    return ids


def solver(filename: str) -> None:
    ids = _reader(filename)
    part_1, part_2 = 0, 0
    for eid in ids:
        if eid[: len(eid) // 2] == eid[len(eid) // 2 :]:
            part_1 += int(eid)
        for pattern in (
            eid[:l] for l in range(1, len(eid) // 2 + 1) if len(eid) % l == 0
        ):
            if eid == "".join([pattern] * (len(eid) // len(pattern))):
                part_2 += int(eid)
                break
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
