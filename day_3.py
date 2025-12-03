import itertools


NUM_PART_1 = 2
NUM_PART_2 = 12


def _reader(filename: str) -> list[str]:
    with open(filename, "r") as file:
        banks = file.readlines()
    return banks


def _finder(string: str) -> tuple[str, int]:
    battery = str(max(int(char) for char in string))
    return battery, string.index(battery)


def _maximiser(bank: str) -> int:
    batteries, index = "", 0
    while len(batteries) < NUM_PART_2:
        battery, shift = _finder(bank[index : -NUM_PART_2 + len(batteries)])
        batteries += battery
        index += shift + 1
    return int(batteries)


def solver(filename: str) -> None:
    banks = _reader(filename)
    print(
        f"Part 1: {
            sum(
                max(
                    int(''.join(batteries))
                    for batteries in itertools.combinations(bank, NUM_PART_1)
                )
                for bank in banks
            )
        }"
    )
    print(f"Part 1: {sum(_maximiser(bank) for bank in banks)}")
