"""Tests if the functions pass."""

__author__ = "730490894"

from utils import only_evens, sub, concat


def test_only_evens_odds() -> None:
    """Edge case of only odd numbers."""
    xs: list[int] = [1, 3, 5, 7, 9, 11]
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Use case with many numbers."""
    xs: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [0, 2, 4, 6, 8, 10]


def test_only_evens_many_items_again() -> None:
    """Another use case with many numbers."""
    xs: list[int] = [3, 6, 9, 12, 15, 18, 21, 24]
    assert only_evens(xs) == [6, 12, 18, 24]


def test_sub_empty_list() -> None:
    """Edge case of empty list and random start and end."""
    xs: list[int] = []
    assert sub(xs, 2, 4) == []


def test_sub_list() -> None:
    """Use case with many items in list, start and end are not 'out of length bounds'."""
    xs: list[int] = [10, 20, 30, 40, 50]
    assert sub(xs, 1, 4) == [20, 30, 40]


def test_sub_list_again() -> None:
    """Use case with many items, start is negative, end is greater than length."""
    xs: list[int] = [10, 20, 30, 40, 50]
    assert sub(xs, -1, 8) == [10, 20, 30, 40, 50]


def test_concat_empty_lists() -> None:
    """Edge case of empty lists, should return empty lists."""
    xs = []
    ys = []
    assert concat(xs, ys) == []


def test_concat_many_items() -> None:
    """Use case with many items in both xs and ys."""
    xs = [1, 3, 5, 7, 9]
    ys = [2, 4, 6, 8, 10]
    assert concat(xs, ys) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def test_concat_many_items_again() -> None:
    """Use case with many items again in both xs and ys."""
    xs = [10, 31, 2003]
    ys = [2, 20, 2022]
    assert concat(xs, ys) == [10, 31, 2003, 2, 20, 2022]