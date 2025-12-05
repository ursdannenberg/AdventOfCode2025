def _reader(filename: str) -> tuple[set[tuple[int, ...]], set[int]]:
    with open(filename, "r") as file:
        fresh, ingredients_ = file.read().split("\n\n")
    fresh_ranges = {
        tuple(int(bound) for bound in fresh_range.split("-"))
        for fresh_range in fresh.strip().split("\n")
    }
    ingredients = {int(ingredient) for ingredient in ingredients_.strip().split("\n")}
    return fresh_ranges, ingredients


def _remover(fresh_ranges: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """Remove ranges that completely overlap with another range."""
    return {
        fresh_range
        for fresh_range in fresh_ranges
        if not any(
            (lower_bound < fresh_range[0] and upper_bound >= fresh_range[1])
            or (lower_bound <= fresh_range[0] and upper_bound > fresh_range[1])
            for lower_bound, upper_bound in fresh_ranges
        )
    }


def _shortener(fresh_ranges: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """Shorten ranges to remove parts that overlap with another range."""
    shortened_fresh_ranges = set()
    # Shorten ranges to remove overlapping parts
    while fresh_ranges:
        lower_bound, upper_bound = fresh_ranges.pop()
        if relevant_fresh_ranges := {
            fresh_range
            for fresh_range in fresh_ranges
            if fresh_range[0] <= lower_bound <= fresh_range[1]
        }:
            lower_bound = max(
                fresh_range[1] + 1 for fresh_range in relevant_fresh_ranges
            )
        if relevant_fresh_ranges := {
            fresh_range
            for fresh_range in fresh_ranges
            if fresh_range[0] <= upper_bound <= fresh_range[1]
        }:
            upper_bound = min(
                fresh_range[0] - 1 for fresh_range in relevant_fresh_ranges
            )
        shortened_fresh_ranges.add((lower_bound, upper_bound))
    return shortened_fresh_ranges


def solver(filename: str) -> None:
    fresh_ranges, ingredients = _reader(filename)
    print(
        f"Part 1: {sum(any(left <= ingredient <= right for left, right in fresh_ranges) for ingredient in ingredients)}"
    )
    # Remove ranges that completely overlap with another range
    fresh_ranges = _remover(fresh_ranges)
    fresh_ranges = _shortener(fresh_ranges)
    print(
        f"Part 2: {sum(upper_bound - lower_bound + 1 for lower_bound, upper_bound in fresh_ranges)}"
    )
