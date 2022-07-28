"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730490894"


class Simpy:
    """A utility class for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor definition for initialization of attributes."""
        self.values = values

    def __str__(self) -> str:
        """Produce a str representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, number: int) -> None:
        """Method to fill a Simpy's values with number of repeating values."""
        self.values = []
        for i in range(0, number):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Method to fill values with range of values."""
        assert step != 0
        if start < 0:
            while start > stop:
                self.values.append(start)
                start += step
        else:
            while start < stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Method to compute and return sum of all items in values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Operator overload to use addition operator with Simpy objects and floats."""
        result: list[float] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Operator overload to use power operator with Simpy objects and floats."""
        result: list[float] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Operator overload to return a list[bool] to test equality."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Operator overload to return a list[bool] to test greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overload to use subscription operator with Simpy objects."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)