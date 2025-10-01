import pytest

import running_average

def test_initial_state():
    ra = running_average.RunningAverage()
    assert ra.current_item_count() == 0
    assert ra.current_average() == 0.0

def test_add_single_item():
    ra = running_average.RunningAverage()
    ra.add_item(5.0)
    assert ra.current_item_count() == 1
    assert ra.current_average() == 5.0

def test_add_multiple_items():
    ra = running_average.RunningAverage()
    items = [2.0, 1e30, 4.0, 6.0, 0]
    for item in items:
        ra.add_item(item)

    assert ra.current_item_count() == len(items)
    expected_average = sum(items) / len(items)
    assert ra.current_average() == pytest.approx(expected_average)
