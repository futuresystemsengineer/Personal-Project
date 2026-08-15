from shorten import shorten
import pytest

def test_default():
    assert shorten() == ""

def test_arguments():
    assert shorten("Hola") == "Hl"
    assert shorten("Wisdom") == "Wsdm"
    assert shorten("Parallel") == "Prlll"

def test_numbers():
    assert shorten("67") == "67"