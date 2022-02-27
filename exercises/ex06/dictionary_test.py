"""Tests the dictionaries functions."""

__author__ = "730490894"

from dictionary import invert, favorite_color, count


def test_one_key() -> None:
    """Edge case with only one key."""
    assert invert({'cat': 'apple'}) == {'apple': 'cat'}


def test_many_keys() -> None:
    """Use case with many keys."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_many_keys_again() -> None:
    """Use case with many keys again."""
    assert invert({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}) == {'b': 'a', 'd': 'c', 'f': 'e', 'h': 'g'}


def test_no_keys() -> None:
    """Edge case with no keys for second function."""
    assert favorite_color({}) == ""


def test_many_colors() -> None:
    """Use case with many keys for second function."""
    assert favorite_color({'a': 'blue', 'b': 'yellow', 'c': 'blue', 'd': 'blue'}) == "blue"


def test_many_colors_again() -> None:
    """Another use case with popular colors that tie, but will return first color in dictionary."""
    assert favorite_color({'a': 'green', 'b': 'yellow', 'c': 'blue', 'd': 'red'}) == "green"


def test_empty_list() -> None:
    """Edge case for third function with empty list."""
    assert count([]) == {}


def test_many_items() -> None:
    """Use case for third function."""
    assert count(['a', 'a', 'b', 'c', 'd']) == {'a': 2, 'b': 1, 'c': 1, 'd': 1}


def test_many_items_again() -> None:
    """Use case for third function again."""
    assert count(['blue', 'blue', 'green', 'green', 'red']) == {'blue': 2, 'green': 2, 'red': 1}