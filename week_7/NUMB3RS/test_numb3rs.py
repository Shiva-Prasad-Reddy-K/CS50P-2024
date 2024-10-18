from numb3rs import validate


def test_end_conditions():
    assert validate("000.000.000.000") == True
    assert validate("255.255.255.255") == True

def test_valid():
    assert validate("192.168.122.32") == True
    assert validate("127.0.0.1") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("12.125,125.100") == False
    assert validate("12.125.522.882") == False