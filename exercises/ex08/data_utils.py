"""Dictionary related utility functions."""

__author__ = "730490894"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(not_mutated: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows for each column."""
    result: dict[str, list[str]] = {}
    for column in not_mutated:
        n_values: list[str] = []
        i: int = 0
        if n >= len(not_mutated[column]):
            return not_mutated
        while i < n:
            n_values.append(not_mutated[column][i])
            i += 1
        result[column] = n_values
    return result


def select(not_mutated: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = not_mutated[column]
    return result


def concat(first_not_mutated: dict[str, list[str]], second_not_mutated: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column-based table combining two-column based tables."""
    result: dict[str, list[str]] = {}
    for column in first_not_mutated:
        result[column] = first_not_mutated[column]
    for column in second_not_mutated:
        if column in result:
            for item in second_not_mutated[column]:
                result[column].append(item)
        else:
            result[column] = second_not_mutated[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produces dict that counts the number of times an item appears in a given list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result