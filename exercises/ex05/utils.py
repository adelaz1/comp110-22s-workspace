"""Functions and implementations."""

__author__ = "730490894"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only even numbers in a list."""
    evens: list[int] = list()
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of the given list between start index and end index (not inclusive)."""
    subset: list[int] = list()
    i: int = start
    while i < end:
        if start < 0:
            start = 0
            i = 0
        if end > len(xs):
            end = len(xs)
        if len(xs) == 0 or start >= len(xs) or end <= 0:
            return subset
        subset.append(xs[i])
        i += 1
    return subset


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Returns a list that contains all elements from xs and ys."""
    concat_list: list[int] = list()
    for item in xs:
        concat_list.append(item)
    for items in ys:
        concat_list.append(items)
    return concat_list