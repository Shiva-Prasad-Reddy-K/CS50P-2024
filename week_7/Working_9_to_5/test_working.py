from working import convert
import pytest

def test_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_value_error():
    with pytest.raises(ValueError):
        convert("8 PM  8 AM")
    with pytest.raises(ValueError):
        convert("Working hours are from 8 PM to 8 AM")
    with pytest.raises(ValueError):
        convert("8 PM-8 AM")
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")