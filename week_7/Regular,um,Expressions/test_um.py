from um import count

def test_valid():
    assert count("um...") == 1
    assert count("Um yum") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2