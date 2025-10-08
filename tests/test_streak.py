import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Test a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4]) == 4

def test_multiple_streaks_longest_is_last():
    """Test where the longest of multiple streaks is at the end."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks_longest_is_first():
    """Test where the longest of multiple streaks is at the beginning."""
    assert longest_positive_streak([5, 6, 7, 0, 4, -1, 2, 3]) == 3

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4]) == 2

def test_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([0, -1, -2, -3]) == 0

def test_all_same_positive_numbers():
    """Test a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0