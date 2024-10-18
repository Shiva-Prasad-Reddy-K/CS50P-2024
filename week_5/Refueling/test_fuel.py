from fuel import convert, gauge
import pytest

def test_check():
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")