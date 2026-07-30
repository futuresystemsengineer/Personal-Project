from twtter import shorten


def test_shorten():
    assert shorten("Hola") == ("Hl")
