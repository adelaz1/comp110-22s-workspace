"""Function skeletons and implementations of dictionaries exercise."""

__author__ = "730490894"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    dictionary: dict[str, str] = dict()
    for key in xs:
        if xs[key] in dictionary:
            raise KeyError
        dictionary[xs[key]] = key
    return dictionary


def favorite_color(xs: dict[str, str]) -> str:
    """Returns the color that appears most frequently, given dict of names and colors."""
    color: str = ""
    i: int = 0
    dictionary: dict[str, int] = {}
    for key in xs:
        if xs[key] in dictionary:
            dictionary[xs[key]] += 1
        else:
            dictionary[xs[key]] = 1
    for key in dictionary:
        if i < dictionary[key]:
            i = dictionary[key]
            color = key
    return color


def count(xs: list[str]) -> dict[str, int]:
    """Counts the number of times a unique str appears in the list."""
    dictionary: dict[str, int] = {}
    for item in xs:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary