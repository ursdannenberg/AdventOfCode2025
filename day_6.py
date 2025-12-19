import math


def _reader(filename: str) -> tuple[list[int], ...]:
    with open(filename, "r") as file:
        lines = file.readlines()
    problems = tuple([0 if char == "+" else 1] for char in lines[-1].strip().split())
    for line in lines[:-1]:
        for i, char in enumerate(line.strip().split()):
            problems[i].append(char)
    return problems


def solver(filename: str) -> None:
    problems = _reader(filename)
    print(
        f"Part 1: {
            sum(
                sum(int(number) for number in problem[1:])
                for problem in problems
                if problem[0] == 0
            )
            + sum(
                math.prod(int(number) for number in problem[1:])
                for problem in problems
                if problem[0] == 1
            )
        }"
    )
