from bank import value

def lowercase():
    assert value("heyy, ssup!") == "$20"
    assert value("how are you?") == "$20"

def uppercase():
    assert value("Hello , sir ") == "$100"
    assert value("Hi, sir ") == "$20"

def punctuation():
    assert value("Hello sir. How are you ?") == "$100"
    assert value("Hello sir. How may I help you ?") == "$100"