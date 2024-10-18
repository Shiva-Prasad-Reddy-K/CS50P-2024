from bank import value

def test_lowercase():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("heyy") == 20
    assert value("HEYY") == 20
    assert value("Any help sir") == 100
    assert value("ANY HELP SIR") == 100