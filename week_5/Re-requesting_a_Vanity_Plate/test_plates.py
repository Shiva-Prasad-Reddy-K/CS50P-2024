from plates import is_valid

def test_validminlength():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("HELLO") == True

def test_maxlength():
    assert is_valid("HEY") == True
    assert is_valid("HELLOWORLD") == False

def test_zeroplacing():
    assert is_valid("CS05") == False

def test_number():
    assert is_valid("500") == False

def test_numberplacing():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punctuation():
    assert is_valid("CS50!") == False