from bank import value

def test_default():
    assert value() == 100

def test_arguments():
    assert value("Hola") == 20
    assert value("Hello") == 0
    assert value("Whats up") == 100

def test_numbers():
    assert value("10") == 100
    assert value("67") == 100