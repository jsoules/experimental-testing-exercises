# Here's one possible way to rewrite histogram.py to make it easier to test.
from typing import Generator
from unittest.mock import patch
import pytest
import math

def parse_line(line: str) -> Generator[str, None, None]:
    l = line.rstrip()
    yield from l.split()


def parse_lines(line_source: Generator[str, None, None]) -> dict[str, int]:
    data = {}

    for line in line_source:
        for token in parse_line(line):
            if token not in data:
                data[token] = 0
            data[token] += 1
    return data


def read_file(filename: str) -> Generator[str, None, None]:
    with open(filename, 'r') as file:
        yield from file


def compute_zoomed_abundance(count: int, total: int, zoom_factor: int = 9):
    normalized_frequency = zoom_factor * count / total
    return normalized_frequency


def compute_width(normalized_frequency: float, max_width: int = 76) -> int:
    return min(math.floor(max_width * normalized_frequency), max_width)


def report_histogram(data: dict[str, int], max_width: int = 76, top_count: int = 12, zoom: int = 9):
    sorted_data = sorted(data, key=lambda x: data[x], reverse = True)
    total_count = sum(data.values())

    for i in range(top_count):
        element = sorted_data[i]
        count = data[element]
        freq = compute_zoomed_abundance(count, total_count, zoom)
        width = compute_width(freq, max_width)
        label = f"{element}:"
        print(f"{label:<4}{'#' * width}")


def histogram(file, max_width = 76):
    file_handler = read_file(file)
    data = parse_lines(file_handler)
    report_histogram(data, max_width, top_count=12, zoom=9)


if __name__ == '__main__':
    histogram('histogram.data', 100)



## Tests might look like this:

@pytest.mark.parametrize("n,t,zoom,expected",[
    (1, 10, 1, 0.1),
    (10, 10, 1, 1),
    (2, 10, 3, 0.6)
])
def test_compute_zoomed_abundance(n, t, zoom, expected):
    assert compute_zoomed_abundance(n, t, zoom) == pytest.approx(expected)


@pytest.mark.parametrize("freq,max", [
    (0.4, 100),
    (1.2, 100),
    (0.2, 10),
])
def test_compute_width(freq, max):
    expected = freq * max
    if expected > max:
        expected = max
    assert compute_width(freq, max) == expected


def test_report_histogram_prints_correct_number_of_lines():
    top_count = 2
    with patch("builtins.print") as mock_print:
        data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
        assert len(data) > top_count
        report_histogram(data, top_count=top_count)
        assert mock_print.call_count == top_count


def test_report_histogram_respects_max_width():
    max_width = 42
    data = {'a': 50, 'b': 50, 'c': 50, 'd': 50}
    with patch("builtins.print") as mock_print:
        report_histogram(data, max_width, top_count=4)
        # call_args_list gets the list of arguments used to call the mock,
        # in reverse chronological order.
        # Each one of these is a tuple of (positional_arguments, named_arguments)
        calls = mock_print.call_args_list
        assert len(calls) == 4
        for print_call_args in calls:
            # for each call, take the first positional argument.
            # Since this is the print() function, it'll just be the
            # string we wrote to the output.
            assert len(print_call_args[0][0]) == max_width + 4

    
def test_report_histogram_computes_widths():
    with patch("builtins.print") as mock_print:
        ...


def test_report_histogram_sorts_data():
    with patch("builtins.print") as mock_print:
        ...
