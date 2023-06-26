import pytest

from src.phone import Phone

@pytest.fixture
def iphone():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_phone_str(iphone):
    assert str(iphone) == "iPhone 14"

def test_phone_repr(iphone):
    assert repr(iphone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_phone_number_of_sim(iphone):
    assert iphone.number_of_sim == 2

