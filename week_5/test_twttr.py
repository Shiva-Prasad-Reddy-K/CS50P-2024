from twttr import shorten

def test_lower():
    assert shorten("shiva") == "shv"
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("SHIVA") == "SHV"
    assert shorten("JASHU") == "JSH"

def test_numbers():
    assert shorten("Shiva14") == "Shv14"

def test_punctuation():
    assert shorten("Shiva,Jashu.") == "Shv,Jsh."