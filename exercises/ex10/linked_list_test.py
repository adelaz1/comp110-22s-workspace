"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, is_equal, last, value_at, max, linkify, scale

__author__ = "730490894"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value at an empty list should raise an IndexError."""
    linked_list = Node(10, Node(20, Node(30, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 3) 


def test_value_at_non_empty() -> None:
    """Value at given index should return value at index of a list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_max_at_empty() -> None:
    """Max of empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_at_non_empty() -> None:
    """Max of non-empty list should return maximum value of list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_linkify_at_empty() -> None:
    """Linkify of empty list should return None."""
    assert linkify([]) is None


def test_linkify_at_non_empty() -> None:
    """Linkify of non-empty list should return linked values."""
    assert is_equal(Node(1, Node(2, Node(3, None))), linkify([1, 2, 3]))


def test_scale_at_empty() -> None:
    """Scale of empty list should return None."""
    assert scale(None, 2) is None


def test_scale_at_non_empty() -> None:
    """Scale of non-empty list should return scaled values."""
    assert is_equal(Node(2, Node(4, Node(6, None))), scale(linkify([1, 2, 3]), 2))